#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional


CONFIG_FILE = Path.home() / ".lingzao" / "config.json"
DEFAULT_TIMEOUT = 180
GENERATE_IMAGE_POLL_TIMEOUT = 300
GENERATE_IMAGE_DOWNLOAD_TIMEOUT_BUFFER = 60
SKILL_ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = SKILL_ROOT / "VERSION"
DEFAULT_SKILL_BASE_URL = "https://assets-tian.midao.site/skills/lingzao"
FIXED_TIME_SAVED_MINUTES = {
    "search-notes": 20,
    "search-suggestions": 10,
    "search-users": 20,
    "get-user-info": 5,
    "get-user-posted-notes": 15,
    "get-note-detail": 8,
    "get-note-comments": 12,
    "get-article-detail": 8,
    "get-article-stats": 5,
    "get-related-articles": 15,
    "generate-image": 40,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Lingzao API client for agent skills.")
    parser.add_argument("--base-url", help="Override Lingzao API base URL")
    parser.add_argument("--api-key", help="Override Lingzao API key")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument(
        "--skill-base-url",
        default=os.environ.get("LINGZAO_SKILL_BASE_URL", DEFAULT_SKILL_BASE_URL),
        help="Lingzao Skill package base URL for version checks",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    check_version_parser = subparsers.add_parser("check-version", help="Check whether the Lingzao skill has an update")
    check_version_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    doctor_parser = subparsers.add_parser("doctor", help="Validate config and API key without billing")
    doctor_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    search_notes_parser = subparsers.add_parser("search-notes", help="Search public content notes")
    search_notes_parser.add_argument("--platform", required=True)
    search_notes_parser.add_argument("--keyword", required=True)
    search_notes_parser.add_argument("--limit", type=int, default=20)
    search_notes_parser.add_argument(
        "--sort",
        choices=["general", "most_liked", "popularity_descending", "comment_descending", "collect_descending"],
        default="general",
    )
    search_notes_parser.add_argument("--note-type", choices=["不限", "视频笔记", "图文笔记", "直播笔记"], default="不限")
    search_notes_parser.add_argument("--time-filter", choices=["不限", "一天内", "一周内", "半年内"], default="不限")
    search_notes_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    search_suggestions_parser = subparsers.add_parser(
        "search-suggestions",
        help="Get public search suggestions",
    )
    search_suggestions_parser.add_argument("--platform", required=True)
    search_suggestions_parser.add_argument("--keyword", default="")
    search_suggestions_parser.add_argument("--limit", type=int, default=10)
    search_suggestions_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    search_users_parser = subparsers.add_parser("search-users", help="Search public creators")
    search_users_parser.add_argument("--platform", required=True)
    search_users_parser.add_argument("--keyword", required=True)
    search_users_parser.add_argument("--limit", type=int, default=20)
    search_users_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    user_info_parser = subparsers.add_parser("get-user-info", help="Get public creator profile info")
    user_info_parser.add_argument("--platform")
    user_info_parser.add_argument("--url")
    user_info_parser.add_argument("--user-id")
    user_info_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    user_notes_parser = subparsers.add_parser(
        "get-user-posted-notes",
        help="Get recent public notes from a creator profile",
    )
    user_notes_parser.add_argument("--platform")
    user_notes_parser.add_argument("--url")
    user_notes_parser.add_argument("--user-id")
    user_notes_parser.add_argument("--limit", type=int, default=20)
    user_notes_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    analyze_user_profile_parser = subparsers.add_parser(
        "analyze-user-profile",
        help="Get deeper creator profile post data",
    )
    analyze_user_profile_parser.add_argument("--platform")
    analyze_user_profile_parser.add_argument("--url")
    analyze_user_profile_parser.add_argument("--user-id")
    analyze_user_profile_parser.add_argument("--limit", type=int, default=20)
    analyze_user_profile_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    note_detail_parser = subparsers.add_parser("get-note-detail", help="Get one public note detail")
    note_detail_parser.add_argument("--platform")
    note_detail_parser.add_argument("--url")
    note_detail_parser.add_argument("--note-id")
    note_detail_parser.add_argument("--xhs-note-type", choices=["image", "video"])
    note_detail_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    note_comments_parser = subparsers.add_parser("get-note-comments", help="Get top-level comments for one public note")
    note_comments_parser.add_argument("--platform")
    note_comments_parser.add_argument("--url")
    note_comments_parser.add_argument("--note-id")
    note_comments_parser.add_argument("--cursor")
    note_comments_parser.add_argument("--sort", choices=["latest", "most_liked"], default="latest")
    note_comments_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    article_detail_parser = subparsers.add_parser(
        "get-article-detail",
        help="Get one public WeChat official-account article detail",
    )
    article_detail_parser.add_argument("--platform")
    article_detail_parser.add_argument("--url", required=True)
    article_detail_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    article_stats_parser = subparsers.add_parser(
        "get-article-stats",
        help="Get public metrics for one WeChat official-account article",
    )
    article_stats_parser.add_argument("--platform")
    article_stats_parser.add_argument("--url", required=True)
    article_stats_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    related_articles_parser = subparsers.add_parser(
        "get-related-articles",
        help="Get related public WeChat official-account articles",
    )
    related_articles_parser.add_argument("--platform")
    related_articles_parser.add_argument("--url", required=True)
    related_articles_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    extract_video_copy_parser = subparsers.add_parser(
        "extract-video-copy",
        help="Extract spoken copy/transcript from short video links",
    )
    extract_video_copy_parser.add_argument("--url", action="append", required=True)
    extract_video_copy_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    generate_image_parser = subparsers.add_parser(
        "generate-image",
        help="Generate creator image assets from a prompt",
    )
    generate_image_parser.add_argument("--prompt", required=True)
    generate_image_parser.add_argument(
        "--size",
        default="1024x1024",
        help="Image size, for example auto, 1024x1024, 1024x1536, 1536x2048, or 9:16.",
    )
    generate_image_parser.add_argument("--count", type=int, default=1, help="Number of images to create, 1-5.")
    generate_image_parser.add_argument("--output-format", choices=["png", "jpeg", "webp"], default="png")
    generate_image_parser.add_argument(
        "--image",
        action="append",
        help="Optional reference image path. Repeat for multiple reference images.",
    )
    generate_image_parser.add_argument("--output", help="Optional path to write the generated image file")
    generate_image_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    args = parser.parse_args()

    if args.command == "check-version":
        payload = check_skill_version(args.skill_base_url, timeout=args.timeout)
        if args.format == "json":
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(render_version_check(payload))
        return 0

    validation_error = validate_args(args)
    if validation_error:
        print(validation_error, file=sys.stderr)
        return 2

    config = resolve_config(args)

    try:
        if args.command == "doctor":
            payload = request_json(config, "GET", "/api/v1/me", timeout=args.timeout)
        elif args.command == "search-notes":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/search-notes",
                {
                    "platform": args.platform,
                    "query": args.keyword,
                    "limit": args.limit,
                    "sort": args.sort,
                    "note_type": args.note_type,
                    "time_filter": args.time_filter,
                },
                timeout=args.timeout,
            )
        elif args.command == "search-users":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/search-users",
                {"platform": args.platform, "query": args.keyword, "limit": args.limit},
                timeout=args.timeout,
            )
        elif args.command == "search-suggestions":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/search-suggestions",
                {"platform": args.platform, "query": args.keyword, "limit": args.limit},
                timeout=args.timeout,
            )
        elif args.command == "get-user-info":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-user-info",
                compact({"platform": args.platform, "url": args.url, "user_id": args.user_id}),
                timeout=args.timeout,
            )
        elif args.command == "get-user-posted-notes":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-user-posted-notes",
                compact({
                    "platform": getattr(args, "platform", None),
                    "url": args.url,
                    "user_id": getattr(args, "user_id", None),
                    "limit": args.limit,
                }),
                timeout=args.timeout,
            )
        elif args.command == "analyze-user-profile":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/analyze-user-profile",
                compact({
                    "platform": getattr(args, "platform", None),
                    "url": args.url,
                    "user_id": getattr(args, "user_id", None),
                    "limit": args.limit,
                }),
                timeout=args.timeout,
            )
        elif args.command == "get-note-detail":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-note-detail",
                compact({
                    "platform": getattr(args, "platform", None),
                    "url": args.url,
                    "note_id": getattr(args, "note_id", None),
                    "xhs_note_type": getattr(args, "xhs_note_type", None),
                }),
                timeout=args.timeout,
            )
        elif args.command == "get-note-comments":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-note-comments",
                compact({
                    "platform": getattr(args, "platform", None),
                    "url": args.url,
                    "note_id": getattr(args, "note_id", None),
                    "cursor": getattr(args, "cursor", None),
                    "sort": getattr(args, "sort", None),
                }),
                timeout=args.timeout,
            )
        elif args.command == "get-article-detail":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-article-detail",
                compact({"platform": getattr(args, "platform", None), "url": args.url}),
                timeout=args.timeout,
            )
        elif args.command == "get-article-stats":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-article-stats",
                compact({"platform": getattr(args, "platform", None), "url": args.url}),
                timeout=args.timeout,
            )
        elif args.command == "get-related-articles":
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/get-related-articles",
                compact({"platform": getattr(args, "platform", None), "url": args.url}),
                timeout=args.timeout,
            )
        elif args.command == "extract-video-copy":
            urls = [url for url in (getattr(args, "url", None) or []) if url]
            body = {"url": urls[0]} if len(urls) == 1 else {"urls": urls}
            payload = request_json(
                config,
                "POST",
                "/api/v1/research/extract-video-copy",
                body,
                timeout=args.timeout,
            )
        elif args.command == "generate-image":
            body = {
                "prompt": args.prompt,
                "size": args.size,
                "output_format": args.output_format,
                "count": args.count,
            }
            image_paths = getattr(args, "image", None) or []
            try:
                if image_paths:
                    payload = request_multipart(
                        config,
                        "POST",
                        "/api/v1/research/generate-image",
                        body,
                        image_paths,
                        timeout=args.timeout,
                    )
                else:
                    payload = request_json(
                        config,
                        "POST",
                        "/api/v1/research/generate-image",
                        body,
                        timeout=args.timeout,
                    )
            except LingzaoApiError as error:
                payload = active_generate_image_batch_payload_from_error(error, requested_count=args.count)
                if not payload:
                    raise
                data = as_dict(payload.get("data"))
                print(f"检测到已有图片生成批次，继续轮询：{data.get('batch_id')}", file=sys.stderr)
            payload = wait_for_generate_image_batch(config, payload, timeout=args.timeout)
            ensure_generate_image_success(payload)
        else:
            raise RuntimeError(f"Unsupported command: {args.command}")
    except LingzaoError as error:
        print(str(error), file=sys.stderr)
        return 1

    local_outputs: List[str] = []
    try:
        if args.command == "generate-image" and getattr(args, "output", None):
            local_outputs = write_generated_images(payload, args.output)
    except LingzaoError as error:
        print(str(error), file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if local_outputs:
            payload = {**payload, "_local_output": local_outputs[0], "_local_outputs": local_outputs}
        print(to_markdown(args.command, payload))
    return 0


class LingzaoError(Exception):
    pass


class LingzaoApiError(LingzaoError):
    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        code: Optional[str] = None,
        error_id: Optional[str] = None,
        payload: Optional[dict] = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.error_id = error_id
        self.payload = payload or {}


def validate_args(args: argparse.Namespace) -> Optional[str]:
    if args.command == "generate-image":
        count = getattr(args, "count", 1)
        if count < 1 or count > 5:
            return "generate-image --count must be between 1 and 5."
        if getattr(args, "format", "markdown") == "markdown" and not getattr(args, "output", None):
            return (
                "generate-image markdown output requires --output so generated images are saved. "
                "Use --format json for raw image payloads."
            )

    if args.command == "get-note-comments" and getattr(args, "sort", None) == "most_liked":
        platform = (getattr(args, "platform", None) or "").strip().lower()
        url = (getattr(args, "url", None) or "").strip().lower()
        if platform in {"douyin", "dy"} or "douyin.com" in url or "iesdouyin.com" in url:
            return (
                "Douyin get-note-comments supports only --sort latest. "
                "Do not pass --sort most_liked for Douyin comments."
            )

    return None


def check_skill_version(skill_base_url: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    local_version = read_local_version()
    remote_version = None
    error = None
    base_url = str(skill_base_url or DEFAULT_SKILL_BASE_URL).strip().rstrip("/")
    version_url = f"{base_url}/VERSION"

    try:
        request = urllib.request.Request(
            version_url,
            headers={
                "accept": "text/plain",
                "user-agent": "LingzaoSkill/1.0",
            },
            method="GET",
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            remote_version = response.read().decode("utf-8").strip()
    except (OSError, UnicodeDecodeError, TimeoutError) as exc:
        error = str(exc)

    update_available = (
        bool(local_version and remote_version)
        and compare_versions(remote_version, local_version) > 0
    )
    return {
        "ok": error is None,
        "local_version": local_version,
        "remote_version": remote_version,
        "update_available": update_available,
        "version_url": version_url,
        "error": error,
    }


def read_local_version() -> str:
    try:
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return "unknown"


def compare_versions(left: str, right: str) -> int:
    left_parts = version_parts(left)
    right_parts = version_parts(right)
    width = max(len(left_parts), len(right_parts))
    left_parts.extend([0] * (width - len(left_parts)))
    right_parts.extend([0] * (width - len(right_parts)))
    if left_parts > right_parts:
        return 1
    if left_parts < right_parts:
        return -1
    return 0


def version_parts(value: str) -> List[int]:
    parts: List[int] = []
    for raw_part in value.strip().lstrip("v").split("."):
        number = ""
        for char in raw_part:
            if char.isdigit():
                number += char
            else:
                break
        parts.append(int(number or "0"))
    return parts


def resolve_config(args: argparse.Namespace) -> dict:
    saved = load_config()
    api_key = args.api_key or os.environ.get("LINGZAO_API_KEY") or saved.get("api_key")
    base_url = (
        args.base_url
        or os.environ.get("LINGZAO_BASE_URL")
        or os.environ.get("LINGZAO_API_BASE_URL")
        or saved.get("base_url")
    )

    if not api_key:
        raise LingzaoError(
            "Missing Lingzao API key. Lingzao Skill can be installed for free, "
            "but public-content lookup, deep research, and image generation require credits "
            "and an API key. "
            "Open https://lingzao.atian.vip for tutorials on setup, Agent usage, and "
            "self-media workflows; when you need lookup access, recharge/get your API key, "
            "then run setup or set LINGZAO_API_KEY."
        )
    if not base_url:
        raise LingzaoError(
            "Missing Lingzao base URL. Open https://lingzao.atian.vip for the current "
            "web dashboard, tutorials, and API setup instructions, then run setup or "
            "set LINGZAO_BASE_URL."
        )

    return {"api_key": str(api_key).strip(), "base_url": str(base_url).strip().rstrip("/")}


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {}
    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def request_json(
    config: dict,
    method: str,
    path: str,
    body: Optional[Dict[str, Any]] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:
    url = config["base_url"] + path
    data = None
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {config['api_key']}",
    }
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["content-type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        record_timeout_probe(method, path, timeout)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return parse_json_response(response.read())
    except urllib.error.HTTPError as error:
        payload = parse_json_response(error.read())
        raise build_lingzao_api_error(error.code, payload) from error
    except urllib.error.URLError as error:
        raise LingzaoError(f"Lingzao API network error: {error.reason}") from error
    except (TimeoutError, socket.timeout) as error:
        raise LingzaoError("Lingzao API request timed out.") from error


def request_multipart(
    config: dict,
    method: str,
    path: str,
    fields: Dict[str, Any],
    image_paths: List[str],
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:
    boundary = f"----LingzaoSkill{uuid.uuid4().hex}"
    data = encode_multipart_body(boundary, fields, image_paths)
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {config['api_key']}",
        "content-type": f"multipart/form-data; boundary={boundary}",
    }
    request = urllib.request.Request(config["base_url"] + path, data=data, headers=headers, method=method)
    try:
        record_timeout_probe(method, path, timeout)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return parse_json_response(response.read())
    except urllib.error.HTTPError as error:
        payload = parse_json_response(error.read())
        raise build_lingzao_api_error(error.code, payload) from error
    except urllib.error.URLError as error:
        raise LingzaoError(f"Lingzao API network error: {error.reason}") from error
    except (TimeoutError, socket.timeout) as error:
        raise LingzaoError("Lingzao API request timed out.") from error


def wait_for_generate_image_batch(config: dict, payload: dict, timeout: int = DEFAULT_TIMEOUT) -> dict:
    data = as_dict(payload.get("data"))
    batch_id = data.get("batch_id")
    if not isinstance(batch_id, str) or not batch_id:
        return payload

    per_image_timeout = max(generate_image_poll_timeout(), timeout)
    batch_get_timeout = generate_image_batch_get_timeout(per_image_timeout)
    requested_count = max(1, generate_image_progress_signature(data)[0])
    total_timeout = generate_image_total_poll_timeout(per_image_timeout, requested_count)
    deadline = time.time() + total_timeout
    current = payload
    last_progress: Optional[tuple[int, int, int, int]] = None
    while True:
        current_data = as_dict(current.get("data"))
        status = str(current_data.get("status") or "").lower()
        pending_count = to_positive_int(current_data.get("pending_count")) or 0
        if status in {"completed", "failed"} or (status == "partial" and pending_count == 0):
            return current

        blocked_codes = non_retryable_generate_image_pending_errors(current_data)
        if blocked_codes:
            if first_generated_image(current):
                return current
            raise LingzaoError(f"Image generation cannot continue: {', '.join(blocked_codes)}.")

        progress = generate_image_progress_signature(current_data)
        if progress != last_progress:
            print(format_generate_image_progress(progress), file=sys.stderr)
            last_progress = progress

        remaining = deadline - time.time()
        if remaining <= 0:
            if first_generated_image(current):
                return current
            raise LingzaoError(generate_image_timeout_message(batch_id, total_timeout, current_data))
        time.sleep(min(1.0, max(0.2, remaining)))
        remaining = deadline - time.time()
        if remaining <= 0:
            if first_generated_image(current):
                return current
            raise LingzaoError(generate_image_timeout_message(batch_id, total_timeout, current_data))
        try:
            current = request_json(
                config,
                "GET",
                f"/api/v1/research/generate-image/batches/{batch_id}",
                timeout=batch_get_timeout,
            )
        except LingzaoError as error:
            if is_lingzao_request_timeout(error) and first_generated_image(current):
                return current
            raise


def generate_image_poll_timeout() -> int:
    override = os.environ.get("LINGZAO_TEST_GENERATE_IMAGE_POLL_TIMEOUT")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return parsed
        except ValueError:
            pass
    return GENERATE_IMAGE_POLL_TIMEOUT


def generate_image_batch_get_timeout(per_image_timeout: int) -> int:
    return per_image_timeout + generate_image_download_timeout_buffer()


def generate_image_total_poll_timeout(per_image_timeout: int, requested_count: int) -> int:
    per_image_worker_timeout = per_image_timeout + generate_image_download_timeout_buffer()
    return per_image_worker_timeout * max(1, requested_count)


def generate_image_download_timeout_buffer() -> int:
    override = os.environ.get("LINGZAO_TEST_GENERATE_IMAGE_DOWNLOAD_TIMEOUT_BUFFER")
    if override is not None:
        try:
            parsed = int(override)
            if parsed >= 0:
                return parsed
        except ValueError:
            pass
    return GENERATE_IMAGE_DOWNLOAD_TIMEOUT_BUFFER


def active_generate_image_batch_payload_from_error(error: LingzaoApiError, requested_count: int) -> Optional[dict]:
    if error.code != "GENERATION_IN_PROGRESS":
        return None

    error_payload = as_dict(as_dict(error.payload).get("error"))
    batch_id = first_non_empty_str(error_payload.get("active_batch_id"), error_payload.get("batch_id"))
    if not batch_id:
        return None

    status = first_non_empty_str(error_payload.get("status")) or "queued"
    poll_url = first_non_empty_str(error_payload.get("poll_url")) or f"/api/v1/research/generate-image/batches/{batch_id}"
    poll_interval = to_positive_int(error_payload.get("recommended_poll_interval_seconds"))
    expires_at = first_non_empty_str(error_payload.get("expires_at"))
    active_count = to_positive_int(error_payload.get("requested_count")) or requested_count
    count = max(1, active_count)

    return {
        "ok": True,
        "request_id": batch_id,
        "cost_credits": 0,
        "data": compact({
            "type": "generate-image",
            "mode": "async",
            "batch_id": batch_id,
            "poll_url": poll_url,
            "recommended_poll_interval_seconds": poll_interval,
            "status": status,
            "expires_at": expires_at,
            "requested_count": count,
            "succeeded_count": 0,
            "failed_count": 0,
            "pending_count": count,
            "images": [{"index": index, "status": status} for index in range(count)],
        }),
    }


def is_lingzao_request_timeout(error: LingzaoError) -> bool:
    return str(error) == "Lingzao API request timed out."


def generate_image_timeout_message(batch_id: str, total_timeout: int, data: dict) -> str:
    errors = generate_image_item_error_summaries(data)
    suffix = f" ({', '.join(errors)})" if errors else ""
    return f"Image batch {batch_id} did not finish within {total_timeout} seconds{suffix}."


def record_timeout_probe(method: str, path: str, timeout: int) -> None:
    probe_path = os.environ.get("LINGZAO_TEST_TIMEOUT_PROBE")
    if not probe_path:
        return
    try:
        with open(probe_path, "a", encoding="utf-8") as handle:
            handle.write(json.dumps({"method": method, "path": path, "timeout": timeout}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def ensure_generate_image_success(payload: dict) -> None:
    data = as_dict(payload.get("data"))
    if data.get("type") != "generate-image" or first_generated_image(payload):
        return

    status = str(data.get("status") or "").strip().lower()
    pending = to_non_negative_int(data.get("pending_count"))
    terminal = status in {"completed", "failed"} or (status == "partial" and pending == 0)
    if not terminal:
        return

    errors = generate_image_item_error_summaries(data)
    suffix = f" ({', '.join(errors)})" if errors else ""
    raise LingzaoError(f"Image generation failed: no successful image was produced{suffix}.")


def non_retryable_generate_image_pending_errors(data: dict) -> List[str]:
    codes: List[str] = []
    for item in as_list(data.get("images")):
        record = as_dict(item)
        status = str(record.get("status") or "").strip().lower()
        error_code = record.get("error_code")
        if status not in {"queued", "running"} or error_code != "INSUFFICIENT_CREDITS":
            continue
        if error_code not in codes:
            codes.append(error_code)
    return codes


def generate_image_item_error_summaries(data: dict) -> List[str]:
    errors: List[str] = []
    for item in as_list(data.get("images")):
        record = as_dict(item)
        error_code = record.get("error_code")
        error_id = record.get("error_id")
        parts: List[str] = []
        if isinstance(error_code, str) and error_code:
            parts.append(error_code)
        if isinstance(error_id, str) and error_id:
            parts.append(f"error_id={error_id}")
        if not parts:
            continue
        summary = " ".join(parts)
        if summary not in errors:
            errors.append(summary)
    return errors


def generate_image_progress_signature(data: dict) -> tuple[int, int, int, int]:
    requested = to_non_negative_int(data.get("requested_count"))
    succeeded = to_non_negative_int(data.get("succeeded_count"))
    failed = to_non_negative_int(data.get("failed_count"))
    pending = to_non_negative_int(data.get("pending_count"))
    if requested <= 0:
        requested = max(1, succeeded + failed + pending)
    return (requested, succeeded, failed, pending)


def format_generate_image_progress(progress: tuple[int, int, int, int]) -> str:
    requested, succeeded, failed, pending = progress
    message = f"正在等待图片生成：{succeeded}/{requested} 已完成，{pending} 张仍在生成中"
    if failed > 0:
        message += f"，{failed} 张失败"
    return message + "..."


def encode_multipart_body(boundary: str, fields: Dict[str, Any], image_paths: List[str]) -> bytes:
    chunks: List[bytes] = []
    for key, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"),
                f"{value}\r\n".encode("utf-8"),
            ]
        )

    for image_path in image_paths:
        path = Path(image_path).expanduser()
        if not path.is_file():
            raise LingzaoError(f"Reference image not found: {path}")
        mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        if mime_type not in {"image/png", "image/jpeg", "image/webp"}:
            raise LingzaoError("Reference images must be png, jpeg, or webp files.")
        image_bytes = path.read_bytes()
        chunks.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                (
                    'Content-Disposition: form-data; name="image"; '
                    f'filename="{escape_multipart_header(path.name)}"\r\n'
                ).encode("utf-8"),
                f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"),
                image_bytes,
                b"\r\n",
            ]
        )

    chunks.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(chunks)


def escape_multipart_header(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\r", "").replace("\n", "")


def parse_json_response(raw: bytes) -> dict:
    if not raw:
        return {}
    try:
        value = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as error:
        raise LingzaoError("Lingzao API returned invalid JSON.") from error
    if not isinstance(value, dict):
        raise LingzaoError("Lingzao API returned unexpected JSON.")
    return value


def extract_error_message(payload: dict) -> Optional[str]:
    error = payload.get("error")
    if isinstance(error, dict) and isinstance(error.get("message"), str):
        return error["message"]
    if isinstance(payload.get("message"), str):
        return payload["message"]
    return None


def extract_error_code(payload: dict) -> Optional[str]:
    error = payload.get("error")
    if isinstance(error, dict) and isinstance(error.get("code"), str):
        return error["code"]
    if isinstance(payload.get("code"), str):
        return payload["code"]
    return None


def extract_error_id(payload: dict) -> Optional[str]:
    error = payload.get("error")
    if isinstance(error, dict) and isinstance(error.get("error_id"), str):
        return error["error_id"]
    if isinstance(payload.get("error_id"), str):
        return payload["error_id"]
    return None


def build_lingzao_api_error(status_code: int, payload: dict) -> LingzaoApiError:
    message = extract_error_message(payload) or f"HTTP {status_code}"
    code = extract_error_code(payload)
    code_label = f" [{code}]" if code else ""
    error_id = extract_error_id(payload)
    error_id_label = f" error_id={error_id}" if error_id else ""
    return LingzaoApiError(
        f"Lingzao API error{code_label}{error_id_label}: {message}",
        status_code=status_code,
        code=code,
        error_id=error_id,
        payload=payload,
    )


def first_non_empty_str(*values: Any) -> Optional[str]:
    for value in values:
        if isinstance(value, str) and value:
            return value
    return None


def compact(value: Dict[str, Any]) -> Dict[str, Any]:
    return {key: item for key, item in value.items() if item is not None}


def write_generated_images(payload: dict, output_path: str) -> List[str]:
    records = generated_image_records(payload)
    if not records:
        raise LingzaoError("Lingzao API returned no generated image data.")

    target = Path(output_path).expanduser()
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        raise LingzaoError(f"Failed to prepare generated image output path: {target.parent}: {error}") from error

    written_paths: List[str] = []
    for record in records:
        image = as_dict(record.get("image"))
        image_bytes = decode_generated_image(image)
        image_target = generated_image_output_path(
            target,
            image,
            to_non_negative_int(record.get("index")),
            max(1, to_non_negative_int(record.get("total"))),
        )
        try:
            image_target.write_bytes(image_bytes)
        except OSError as error:
            raise LingzaoError(f"Failed to write generated image output: {image_target}: {error}") from error
        written_paths.append(str(image_target))
    return written_paths


def write_generated_image(payload: dict, output_path: str) -> str:
    paths = write_generated_images(payload, output_path)
    if not paths:
        raise LingzaoError("Lingzao API returned no generated image data.")
    return paths[0]


def decode_generated_image(image: dict) -> bytes:
    b64_json = image.get("b64_json")
    if not isinstance(b64_json, str) or not b64_json.strip():
        raise LingzaoError("Lingzao API returned no generated image data.")

    try:
        return base64.b64decode(b64_json, validate=True)
    except ValueError as error:
        raise LingzaoError("Lingzao API returned invalid image base64.") from error


def generated_image_output_path(target: Path, image: dict, index: int, total: int) -> Path:
    if total == 1:
        return target
    suffix = target.suffix or generated_image_extension(image)
    stem = target.stem if target.suffix else target.name
    return target.with_name(f"{stem}-{index + 1}{suffix}")


def generated_image_extension(image: dict) -> str:
    mime_type = image.get("mime_type")
    if isinstance(mime_type, str):
        if mime_type == "image/jpeg":
            return ".jpg"
        extension = mimetypes.guess_extension(mime_type)
        if extension:
            return extension
    return ".png"


def generated_images(payload: dict) -> List[dict]:
    return [as_dict(record.get("image")) for record in generated_image_records(payload)]


def generated_image_records(payload: dict) -> List[dict]:
    data = as_dict(payload.get("data"))
    items = as_list(data.get("images"))
    requested_count = to_non_negative_int(data.get("requested_count"))
    total = max(requested_count, len(items), 1)
    records: List[dict] = []
    for fallback_index, item in enumerate(items):
        record = as_dict(item)
        image = as_dict(record.get("image"))
        if image:
            item_index = to_optional_non_negative_int(record.get("index"))
            records.append({
                "image": image,
                "index": item_index if item_index is not None else fallback_index,
                "total": total,
            })
    if records:
        return records

    image = as_dict(data.get("image"))
    if image:
        return [{"image": image, "index": 0, "total": max(requested_count, 1)}]
    return []


def first_generated_image(payload: dict) -> dict:
    data = as_dict(payload.get("data"))
    image = as_dict(data.get("image"))
    if image:
        return image
    for item in as_list(data.get("images")):
        record = as_dict(item)
        image = as_dict(record.get("image"))
        if image:
            return image
    return {}


def to_markdown(command: str, payload: dict) -> str:
    if command == "doctor":
        return render_doctor(payload)
    rendered = None
    if command == "search-notes":
        rendered = render_search_notes(payload)
    elif command == "search-suggestions":
        rendered = render_search_suggestions(payload)
    elif command == "search-users":
        rendered = render_search_users(payload)
    elif command == "get-user-info":
        rendered = render_user_info(payload)
    elif command == "get-user-posted-notes":
        rendered = render_user_posted_notes(payload)
    elif command == "analyze-user-profile":
        rendered = render_analyze_user_profile(payload)
    elif command == "get-note-detail":
        rendered = render_note(payload)
    elif command == "get-note-comments":
        rendered = render_note_comments(payload)
    elif command == "get-article-detail":
        rendered = render_article_detail(payload)
    elif command == "get-article-stats":
        rendered = render_article_stats(payload)
    elif command == "get-related-articles":
        rendered = render_related_articles(payload)
    elif command == "extract-video-copy":
        rendered = render_extract_video_copy(payload)
    elif command == "generate-image":
        rendered = render_generate_image(payload)
    else:
        return "```json\n" + json.dumps(payload, ensure_ascii=False, indent=2) + "\n```"

    footer = render_time_saved_footer(command, payload)
    if footer:
        return f"{rendered}\n\n{footer}"
    return rendered


def render_time_saved_footer(command: str, payload: dict) -> Optional[str]:
    if payload.get("ok") is not True:
        return None

    minutes = estimate_time_saved_minutes(command, payload)
    if minutes is None or minutes <= 0:
        return None
    return f"本次灵造调用预计节省约 {minutes} 分钟手动搜索与整理时间。"


def estimate_time_saved_minutes(command: str, payload: dict) -> Optional[int]:
    if command in FIXED_TIME_SAVED_MINUTES:
        return FIXED_TIME_SAVED_MINUTES[command]
    if command == "analyze-user-profile":
        data = as_dict(payload.get("data"))
        page = as_dict(data.get("page"))
        limit = to_positive_int(page.get("limit"))
        if limit is None:
            limit = to_positive_int(page.get("returned_count"))
        if limit is None:
            limit = len(as_list(data.get("items"))) or 20
        return 60 if limit <= 20 else 100
    if command == "extract-video-copy":
        data = as_dict(payload.get("data"))
        total = 0
        for item in as_list(data.get("items")):
            record = as_dict(item)
            status = str(record.get("status") or "").strip().lower()
            if status and status != "success":
                continue
            if not status and not record.get("content"):
                continue
            seconds = to_positive_int(record.get("duration_seconds")) or 0
            video_minutes = (seconds + 59) // 60
            total += max(8, video_minutes * 6)
        return total or None
    return None


def to_positive_int(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value > 0:
        return value
    if isinstance(value, float) and value > 0:
        return int(value)
    if isinstance(value, str):
        try:
            parsed = int(float(value))
        except ValueError:
            return None
        return parsed if parsed > 0 else None
    return None


def to_non_negative_int(value: Any) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, float):
        return max(0, int(value))
    if isinstance(value, str):
        try:
            return max(0, int(float(value)))
        except ValueError:
            return 0
    return 0


def to_optional_non_negative_int(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value if value >= 0 else None
    if isinstance(value, float):
        parsed = int(value)
        return parsed if parsed >= 0 else None
    if isinstance(value, str):
        try:
            parsed = int(float(value))
        except ValueError:
            return None
        return parsed if parsed >= 0 else None
    return None


def render_doctor(payload: dict) -> str:
    user = as_dict(payload.get("user"))
    api_key = as_dict(payload.get("api_key"))
    return "\n".join(
        [
            "# Lingzao 连接检查",
            "",
            f"- 状态: {'正常' if payload.get('ok') else '异常'}",
            f"- API Key: {api_key.get('key_prefix', '-')}",
            f"- 用户: {render_user_identity(user)}",
        ]
    )


def render_search_notes(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    items = as_list(data.get("items"))
    lines = [
        f"# {platform_label(data)}关键词线索：{data.get('query') or '-'}",
        "",
    ]
    for index, item in enumerate(items, start=1):
        note = as_dict(item)
        lines.extend(render_note_item(index, note))
    if not items:
        lines.append("未返回公开内容线索。")
    return "\n".join(lines).strip()


def render_search_suggestions(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    suggestions = as_list(data.get("suggestions"))
    query = data.get("query")
    title_keyword = str(query) if query else "热门推荐"
    lines = [
        f"# {platform_label(data)}搜索联想词：{title_keyword}",
        "",
    ]
    for index, item in enumerate(suggestions, start=1):
        suggestion = as_dict(item)
        lines.extend(
            [
                f"### {index}. {suggestion.get('text') or '-'}",
                f"- 搜索类型: {suggestion.get('search_type') or '-'}",
                f"- 类型标记: {suggestion.get('kind') or '-'}",
                "",
            ]
        )
    if not suggestions:
        lines.append("未返回公开搜索联想词。")
    return "\n".join(lines).strip()


def render_search_users(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    users = as_list(data.get("users"))
    platform = str(data.get("platform") or "").lower()
    lines = [
        f"# {platform_label(data)}创作者搜索：{data.get('query') or '-'}",
        "",
    ]
    for index, item in enumerate(users, start=1):
        profile = as_dict(item)
        stats = as_dict(profile.get("stats"))
        lines.extend(
            [
                f"### {index}. {profile.get('name') or profile.get('id') or '-'}",
                f"- 主页链接: {profile_public_url(platform, profile)}",
                f"- 简介: {profile.get('bio') or '-'}",
                f"- 粉丝: {stats.get('fans', '-')}",
                f"- 获赞: {stats.get('liked', '-')}",
                "",
            ]
        )
    if not users:
        lines.append("未返回公开创作者候选。")
    return "\n".join(lines).strip()


def render_user_info(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    profile = as_dict(data.get("profile"))
    stats = as_dict(profile.get("stats"))
    platform = str(data.get("platform") or "").lower()
    lines = [
        f"# {platform_label(data)}主页资料：{profile.get('name') or profile.get('id') or '-'}",
        "",
        f"- 主页链接: {profile_public_url(platform, profile)}",
        f"- 简介: {profile.get('bio') or '-'}",
        f"- 粉丝: {stats.get('fans', '-')}",
        f"- 获赞: {stats.get('liked', '-')}",
        f"- 收藏: {stats.get('collected', '-')}",
    ]
    return "\n".join(lines).strip()


def render_user_posted_notes(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    notes = as_list(data.get("items"))
    lines = [
        f"# {platform_label(data)}主页近期公开内容",
        "",
        "## 近期笔记",
    ]
    for index, item in enumerate(notes, start=1):
        lines.extend(render_note_item(index, as_dict(item)))
    if not notes:
        lines.append("未返回近期公开笔记。")
    followup = (
        "如需继续查看主页作品结构、商业信号、内容热词和相似创作者，可继续请求 analyze-user-profile；"
        "如需抖音单条视频口播文案，使用 extract-video-copy；我不会自动调用。"
        if str(data.get("platform") or "").lower() == "douyin"
        else "如需继续查看主页作品正文、中文字幕、封面和商单/商品信号，可继续请求 analyze-user-profile；我不会自动调用。"
    )
    lines.extend(
        [
            "",
            "基础主页分析通常不需要再调用 get-user-info；只有用户明确需要简介、粉丝数、关注数、总获赞、总收藏或总笔记数时才补充调用。",
            followup,
        ]
    )
    return "\n".join(lines).strip()


def render_note_comments(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    comments = as_list(data.get("comments"))
    page = as_dict(data.get("page"))
    lines = [
        f"# {platform_label(data)}内容评论：{data.get('note_id') or '-'}",
        "",
        f"- 排序: {data.get('sort') or 'latest'}",
        f"- 返回: {page.get('returned_count', len(comments))}",
        f"- 总数: {page.get('total') if page.get('total') is not None else '-'}",
        f"- 还有下一页: {page.get('has_more', False)}",
        f"- 下一页 Cursor: {page.get('next_cursor') or '-'}",
        "",
    ]
    for index, item in enumerate(comments, start=1):
        comment = as_dict(item)
        author = as_dict(comment.get("author"))
        lines.extend(
            [
                f"### {index}. {author.get('name') or author.get('id') or '-'}",
                f"- 评论: {comment.get('text') or '-'}",
                f"- 点赞: {comment.get('liked_count', '-')}",
                f"- 回复数: {comment.get('reply_count', '-')}",
                f"- 时间: {comment.get('created_at') or '-'}",
                "",
            ]
        )
    if not comments:
        lines.append("未返回公开评论。")
    return "\n".join(lines).strip()


def render_analyze_user_profile(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    user = as_dict(data.get("user"))
    page = as_dict(data.get("page"))
    items = as_list(data.get("items"))
    artifacts = as_dict(data.get("artifacts"))
    subtitle_markdown = as_dict(artifacts.get("subtitle_markdown"))
    lines = [
        f"# {platform_label(data)}深度主页数据：{user.get('nickname') or user.get('id') or '-'}",
        "",
        f"- 主页链接: {profile_public_url(str(data.get('platform') or '').lower(), user)}",
        f"- 返回: {page.get('returned_count', len(items))} / {page.get('limit', '-')}",
        f"- 下一页 Cursor: {page.get('next_cursor') or '-'}",
        "",
    ]
    if subtitle_markdown.get("status") == "ready" and subtitle_markdown.get("url"):
        url = str(subtitle_markdown.get("url"))
        lines.extend(
            [
                "## 完整字幕 Markdown",
                "",
                "- 字段路径: data.artifacts.subtitle_markdown.url",
                "- 注意: 这是整个 analyze-user-profile 的顶层 artifact，不是 items[] 里的单条字幕链接。",
                f"- URL: {url}",
                "- 下载到临时文件后再做深度分析：",
                "",
                "```bash",
                f"curl -L {shell_quote(url)} -o /tmp/lingzao-profile-subtitles.md",
                "```",
                "",
            ]
        )
    elif subtitle_markdown.get("status") == "unsupported":
        lines.extend(
            [
                "## 主页字幕",
                "",
                "- 状态: unsupported",
                "- 当前平台主页解析不提取字幕；如需口播文案，请对具体视频使用 extract-video-copy。",
                "",
            ]
        )
    elif subtitle_markdown:
        lines.extend(
            [
                "## 完整字幕 Markdown",
                "",
                f"- 状态: {subtitle_markdown.get('status') or '-'}",
                "",
            ]
        )
    lines.extend(render_profile_insights(data))
    for index, item in enumerate(items, start=1):
        note = as_dict(item)
        metrics = as_dict(note.get("metrics"))
        media = as_dict(note.get("media"))
        text = as_dict(note.get("text"))
        subtitle = as_dict(text.get("subtitle"))
        monetization = as_dict(note.get("monetization"))
        collaboration = as_dict(monetization.get("collaboration"))
        commerce_note = as_dict(monetization.get("commerce_note"))
        plain_text = str(subtitle.get("plain_text_preview") or subtitle.get("plain_text") or "")
        preview = plain_text[:240] + ("..." if len(plain_text) > 240 else "")
        item_lines = [
            f"### {index}. {note.get('title') or note.get('id') or '未命名笔记'}",
            f"- 链接: {note.get('url') or '-'}",
            f"- 类型: {note.get('type') or '-'}",
            f"- 详情参数: xhs_note_type={note.get('xhs_note_type')}" if note.get("xhs_note_type") else "- 详情参数: -",
            f"- 指标: 点赞 {metrics.get('liked', 0)} / 收藏 {metrics.get('collected', 0)} / 评论 {metrics.get('commented', 0)} / 分享 {metrics.get('shared', 0)}",
            f"- 封面: {media.get('cover_large_url') or '-'}",
            f"- 时长: {media.get('video_duration_seconds') or '-'} 秒",
        ]
        if str(data.get("platform") or "").lower() == "douyin":
            item_lines.append("- 商业信号: 当前平台未提供")
        else:
            item_lines.append(
                f"- 商单: {collaboration.get('likely_collaboration', False)} / 商品笔记: {commerce_note.get('likely_goods_note', False)}"
            )
        item_lines.extend(
            [
                f"- 字幕: {subtitle.get('status') or '-'} / {subtitle.get('language') or '-'} / truncated={subtitle.get('truncated', False)}",
                f"- 摘要: {text.get('desc') or '-'}",
                f"- 字幕预览: {preview or '-'}",
                "",
            ]
        )
        lines.extend(item_lines)
    if not items:
        lines.append("未返回深度主页数据。")
    return "\n".join(lines).strip()


def render_profile_insights(data: dict) -> List[str]:
    insights = as_dict(data.get("profile_insights"))
    if not insights:
        return []

    hot_keywords = as_dict(insights.get("content_hot_keywords"))
    hot_keyword_items = as_list(hot_keywords.get("items"))
    similar_creators = as_dict(insights.get("similar_creators"))
    similar_creator_items = as_list(similar_creators.get("items"))
    if not hot_keywords and not similar_creators:
        return []

    lines = ["## 主页洞察", ""]
    if hot_keywords:
        lines.append(f"- 内容热词: {hot_keywords.get('status') or '-'} / {len(hot_keyword_items)}")
        for item in hot_keyword_items[:8]:
            keyword = as_dict(item)
            details = [
                f"score={value_or_dash(keyword.get('score'))}",
                f"rank={value_or_dash(keyword.get('rank'))}",
                f"category={value_or_dash(keyword.get('category'))}",
            ]
            lines.append(f"  - {keyword.get('text') or '-'} ({', '.join(details)})")
        lines.append("")

    if similar_creators:
        lines.append(f"- 相似创作者: {similar_creators.get('status') or '-'} / {len(similar_creator_items)}")
        for item in similar_creator_items[:5]:
            creator = as_dict(item)
            tags = as_list(creator.get("tags"))
            reasons = as_list(creator.get("recommend_reasons"))
            lines.append(
                "  - "
                + f"{creator.get('name') or creator.get('id') or '-'}"
                + f" / 粉丝 {value_or_dash(creator.get('fans'))}"
                + f" / 预期播放 {value_or_dash(creator.get('expected_play_count'))}"
                + f" / 相似度 {value_or_dash(creator.get('similarity'))}"
                + f" / 标签 {', '.join(str(tag) for tag in tags) if tags else '-'}"
                + f" / 推荐原因 {', '.join(str(reason) for reason in reasons) if reasons else '-'}"
            )
        lines.append("")

    return lines


def value_or_dash(value: Any) -> str:
    if value is None or value == "":
        return "-"
    return str(value)


def shell_quote(value: str) -> str:
    return "'" + value.replace("'", "'\"'\"'") + "'"


def render_note(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    note = as_dict(data.get("item"))
    lines = [
        f"# {platform_label(data)}内容：{note.get('title') or note.get('id') or '-'}",
        "",
    ]
    lines.extend(render_note_item(1, note, include_index=False))
    return "\n".join(lines).strip()


def render_article_detail(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    article = as_dict(data.get("article"))
    title = article.get("title") or "未命名文章"
    lines = [
        f"# {platform_label(data)}文章：{title}",
        "",
        f"- 链接: {article.get('url') or '-'}",
        f"- 公众号: {article.get('account_name') or '-'}",
        f"- 作者: {article.get('author') or '-'}",
        f"- 发布时间: {article.get('published_at') or '-'}",
        f"- 封面: {article.get('cover_url') or '-'}",
        f"- 摘要: {article.get('digest') or '-'}",
        "",
        "## 正文预览",
        "",
        article_text_preview(str(article.get("content_text") or "")),
    ]
    return "\n".join(lines).strip()


def render_article_stats(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    metrics = as_dict(data.get("metrics"))
    lines = [
        f"# {platform_label(data)}文章数据",
        "",
        f"- 链接: {data.get('article_url') or '-'}",
        f"- 阅读: {metrics.get('read_count', '-')}",
        f"- 点赞: {metrics.get('like_count', '-')}",
        f"- 在看: {metrics.get('wow_count', '-')}",
        f"- 分享: {metrics.get('share_count', '-')}",
        f"- 收藏: {metrics.get('collect_count', '-')}",
        f"- 评论: {metrics.get('comment_count', '-')}",
        f"- 星标: {metrics.get('star_count', '-')}",
    ]
    return "\n".join(lines).strip()


def render_related_articles(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    page = as_dict(data.get("page"))
    articles = as_list(data.get("articles"))
    lines = [
        f"# {platform_label(data)}相关文章",
        "",
        f"- 原文链接: {data.get('article_url') or '-'}",
        f"- 返回: {page.get('returned_count', len(articles))}",
        f"- 总数: {page.get('total') if page.get('total') is not None else '-'}",
        "",
    ]
    for index, item in enumerate(articles, start=1):
        article = as_dict(item)
        lines.extend(
            [
                f"### {index}. {article.get('title') or '未命名文章'}",
                f"- 链接: {article.get('url') or '-'}",
                f"- 公众号: {article.get('account_name') or '-'}",
                f"- 发布时间: {article.get('published_at') or '-'}",
                f"- 摘要: {article.get('digest') or '-'}",
                "",
            ]
        )
    if not articles:
        lines.append("未返回相关文章。")
    return "\n".join(lines).strip()


def article_text_preview(value: str, limit: int = 1200) -> str:
    text = " ".join(value.split())
    if not text:
        return "未返回正文文本。"
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def render_extract_video_copy(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    batch = as_dict(data.get("batch"))
    items = as_list(data.get("items"))
    lines = [
        "# 短视频文案提取",
        "",
        f"- Batch ID: {batch.get('batch_id', '-')}",
        f"- 成功: {batch.get('success_count', 0)} / {batch.get('total_count', len(items))}",
        "",
    ]
    for index, item in enumerate(items, start=1):
        record = as_dict(item)
        lines.extend(
            [
                f"### {index}. {record.get('title') or record.get('origin_url') or '-'}",
                f"- 平台: {record.get('platform') or '-'}",
                f"- 链接: {record.get('origin_url') or record.get('input_url') or '-'}",
                f"- 状态: {record.get('status') or '-'}",
                f"- 错误: {record.get('error_code') or '-'} / {record.get('message') or '-'}",
                f"- 时长: {record.get('duration_seconds') or '-'} 秒",
                "",
                str(record.get("content") or "未返回文案。"),
                "",
            ]
        )
    if not items:
        lines.append("未返回文案提取结果。")
    return "\n".join(lines).strip()


def render_generate_image(payload: dict) -> str:
    data = as_dict(payload.get("data"))
    image = first_generated_image(payload)
    local_output = payload.get("_local_output")
    local_outputs = [item for item in as_list(payload.get("_local_outputs")) if isinstance(item, str) and item]
    blocked_codes = non_retryable_generate_image_pending_errors(data)
    item_errors = generate_image_item_error_summaries(data)
    lines = [
        "# 图片生成结果",
        "",
        f"- Batch: {data.get('batch_id') or '-'}",
        f"- 状态: {data.get('status') or '-'}",
        f"- 数量: {data.get('succeeded_count', 0)} 成功 / {data.get('requested_count', 1)} 请求",
        f"- 尺寸: {data.get('size') or '-'}",
        f"- 格式: {data.get('output_format') or '-'}",
        f"- 参考图: {data.get('reference_image_count') if data.get('reference_image_count') is not None else 0}",
        f"- MIME: {image.get('mime_type') or '-'}",
        f"- SHA256: {image.get('sha256') or '-'}",
    ]
    if len(local_outputs) > 1:
        lines.append("- 文件:")
        lines.extend(f"  - {path}" for path in local_outputs)
    elif local_outputs:
        lines.append(f"- 文件: {local_outputs[0]}")
    elif local_output:
        lines.append(f"- 文件: {local_output}")
    else:
        lines.append("- 文件: 未保存；下次可加 `--output /tmp/lingzao-image.png`")
    if blocked_codes:
        lines.append(f"- 未完成: {', '.join(blocked_codes)}")
    if item_errors:
        lines.append(f"- 错误: {', '.join(item_errors)}")
    lines.extend(
        [
            "",
            "Base64 字段路径：`data.images[].image.b64_json`",
        ]
    )
    return "\n".join(lines).strip()


def render_version_check(payload: dict) -> str:
    local_version = payload.get("local_version") or "unknown"
    remote_version = payload.get("remote_version") or "unknown"
    if payload.get("update_available"):
        return "\n".join(
            [
                "# Lingzao Skill 更新可用",
                "",
                f"- 当前版本: {local_version}",
                f"- 最新版本: {remote_version}",
                "",
                "必须先更新到最新版本，再继续处理用户的灵造搜索、主页分析、字幕或文案提取请求。",
                "请告诉用户：灵造技能有新版本，我需要先更新后再继续。",
                "",
                "更新时执行：",
                "",
                "```bash",
                "npx skills add https://assets-tian.midao.site/skills/lingzao --skill lingzao -g --copy",
                "```",
                "",
                "更新会保留 ~/.lingzao/config.json 里的 API 配置，通常不需要重新设置 API key。",
                "",
                "如果更新后 ~/.lingzao/bin/lingzao 不存在或命令入口失效，再运行 setup.sh --skip-doctor 修复命令入口。",
            ]
        )
    if payload.get("ok"):
        return "\n".join(
            [
                "# Lingzao Skill 已是最新",
                "",
                f"- 当前版本: {local_version}",
            ]
        )
    return "\n".join(
        [
            "# Lingzao Skill 版本检查未完成",
            "",
            f"- 当前版本: {local_version}",
            "- 可以继续使用灵造技能。",
        ]
    )


def platform_label(data: dict) -> str:
    platform = str(data.get("platform") or "xhs").lower()
    if platform == "xhs":
        return "小红书"
    if platform == "douyin":
        return "抖音"
    if platform == "wechat_mp":
        return "微信公众号"
    return platform


def render_note_item(index: int, note: dict, include_index: bool = True) -> List[str]:
    metrics = as_dict(note.get("metrics"))
    author = as_dict(note.get("author"))
    title_prefix = f"{index}. " if include_index else ""
    tags = as_list(note.get("tags"))
    lines = [
        f"### {title_prefix}{note.get('title') or note.get('id') or '未命名笔记'}",
        f"- 链接: {note.get('url') or '-'}",
        f"- 作者: {author.get('name') or author.get('id') or '-'}",
        f"- 类型: {note.get('type') or '-'}",
    ]
    if note.get("xhs_note_type"):
        lines.append(f"- 详情参数: xhs_note_type={note.get('xhs_note_type')}")
    lines.extend(
        [
            f"- 指标: 点赞 {metrics.get('liked', 0)} / 收藏 {metrics.get('collected', 0)} / 评论 {metrics.get('commented', 0)} / 分享 {metrics.get('shared', 0)}",
            f"- 标签: {', '.join(str(tag) for tag in tags) if tags else '-'}",
            f"- 摘要: {note.get('summary') or '-'}",
            "",
        ]
    )
    return lines


def render_user_identity(user: dict) -> str:
    if user.get("name"):
        return str(user["name"])
    if user.get("email"):
        return mask_email(str(user["email"]))
    if user.get("id"):
        return str(user["id"])
    return "-"


def profile_public_url(platform: str, profile: dict) -> str:
    for key in ("url", "profile_url", "homepage_url", "share_url", "link"):
        value = profile.get(key)
        if value:
            return str(value)
    profile_id = profile.get("id") or profile.get("user_id") or profile.get("userid")
    if platform in {"xhs", "xiaohongshu", ""} and profile_id:
        return f"https://www.xiaohongshu.com/user/profile/{quote_path_segment(str(profile_id))}"
    if platform in {"douyin", "dy"} and profile_id:
        return f"https://www.douyin.com/user/{quote_path_segment(str(profile_id))}"
    return "-"


def quote_path_segment(value: str) -> str:
    return urllib.parse.quote(value, safe="")


def mask_email(value: str) -> str:
    if "@" not in value:
        return value[:2] + "***" if len(value) > 2 else "***"
    local, domain = value.split("@", 1)
    if not local:
        return "***@" + domain
    return local[:1] + "***@" + domain


def as_dict(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list:
    return value if isinstance(value, list) else []


if __name__ == "__main__":
    raise SystemExit(main())
