#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path


CONFIG_DIR = Path.home() / ".lingzao"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_BASE_URL = "http://localhost:3080"


def main() -> int:
    parser = argparse.ArgumentParser(description="Configure Lingzao API credentials.")
    parser.add_argument("--api-key", help="Lingzao API key, starts with lgz_")
    parser.add_argument("--base-url", default=None, help="Lingzao API base URL")
    parser.add_argument("--show", action="store_true", help="Show current config without revealing the full key")
    parser.add_argument("--reset", action="store_true", help="Remove saved config")
    args = parser.parse_args()

    if args.reset:
        if CONFIG_FILE.exists():
            CONFIG_FILE.unlink()
        print("Lingzao config removed.")
        return 0

    if args.show:
        config = load_config()
        print(json.dumps(mask_config(config), ensure_ascii=False, indent=2))
        return 0

    api_key = args.api_key or os.environ.get("LINGZAO_API_KEY")
    base_url = args.base_url or os.environ.get("LINGZAO_BASE_URL") or os.environ.get("LINGZAO_API_BASE_URL")

    if not api_key:
        api_key = input("Lingzao API Key: ").strip()
    if not base_url:
        entered = input(f"Lingzao Base URL [{DEFAULT_BASE_URL}]: ").strip()
        base_url = entered or DEFAULT_BASE_URL

    config = validate_config({"api_key": api_key, "base_url": base_url})
    save_config(config)
    print(f"Lingzao config saved to {CONFIG_FILE}")
    print(json.dumps(mask_config(config), ensure_ascii=False, indent=2))
    return 0


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {}
    with CONFIG_FILE.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_config(config: dict) -> None:
    CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    with CONFIG_FILE.open("w", encoding="utf-8") as handle:
        json.dump(config, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    CONFIG_FILE.chmod(0o600)


def validate_config(config: dict) -> dict:
    api_key = str(config.get("api_key", "")).strip()
    base_url = str(config.get("base_url", "")).strip().rstrip("/")

    if not api_key.startswith("lgz_"):
        raise SystemExit("Invalid Lingzao API key. It should start with lgz_.")
    if not base_url.startswith(("http://", "https://")):
        raise SystemExit("Invalid Lingzao base URL. It should start with http:// or https://.")

    return {"api_key": api_key, "base_url": base_url}


def mask_config(config: dict) -> dict:
    api_key = str(config.get("api_key", ""))
    return {
        "api_key": mask_key(api_key) if api_key else None,
        "base_url": config.get("base_url"),
        "config_file": str(CONFIG_FILE),
    }


def mask_key(value: str) -> str:
    if len(value) <= 12:
        return value[:4] + "..."
    return value[:12] + "..." + value[-4:]


if __name__ == "__main__":
    raise SystemExit(main())
