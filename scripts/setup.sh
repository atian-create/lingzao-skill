#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
WRAPPER_PATH="$HOME/.lingzao/bin/lingzao"
API_KEY=""
BASE_URL=""
SKIP_DOCTOR="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --api-key)
      API_KEY="${2:-}"
      shift 2
      ;;
    --base-url)
      BASE_URL="${2:-}"
      shift 2
      ;;
    --skip-doctor)
      SKIP_DOCTOR="true"
      shift
      ;;
    -h|--help)
      cat <<'EOF'
Usage: bash scripts/setup.sh [--api-key lgz_xxx] [--base-url https://your-domain] [--skip-doctor]

Config is saved to ~/.lingzao/config.json with 0600 permissions.
Environment variables LINGZAO_API_KEY and LINGZAO_BASE_URL override saved config.
The command wrapper is installed to ~/.lingzao/bin/lingzao.
EOF
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

"$PYTHON_BIN" - <<'PY'
import sys

if sys.version_info < (3, 8):
    raise SystemExit("Lingzao skill requires Python 3.8 or newer.")
PY

CONFIG_ARGS=()
if [[ -n "$API_KEY" ]]; then
  CONFIG_ARGS+=(--api-key "$API_KEY")
fi
if [[ -n "$BASE_URL" ]]; then
  CONFIG_ARGS+=(--base-url "$BASE_URL")
fi

if [[ ${#CONFIG_ARGS[@]} -gt 0 ]]; then
  "$PYTHON_BIN" "$ROOT_DIR/scripts/configure.py" "${CONFIG_ARGS[@]}"
else
  "$PYTHON_BIN" "$ROOT_DIR/scripts/configure.py"
fi

mkdir -p "$(dirname "$WRAPPER_PATH")"
ROOT_DIR_ESCAPED="$(printf '%q' "$ROOT_DIR")"
cat > "$WRAPPER_PATH" <<EOF
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$ROOT_DIR_ESCAPED
PYTHON_BIN="\${PYTHON_BIN:-python3}"
exec "\$PYTHON_BIN" "\$ROOT_DIR/scripts/lingzao_client.py" "\$@"
EOF
chmod +x "$WRAPPER_PATH"
echo "Lingzao command installed to $WRAPPER_PATH"

if [[ "$SKIP_DOCTOR" != "true" ]]; then
  "$WRAPPER_PATH" doctor
fi
