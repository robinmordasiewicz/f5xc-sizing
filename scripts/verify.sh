#!/bin/bash
# Local verification script - 100% idempotent
# Works identically for Claude Code and human users
#
# Usage:
#   ./scripts/verify.sh           # Full verification (build + serve)
#   ./scripts/verify.sh --build   # CI build only (no server)
#   ./scripts/verify.sh --serve   # Start dev server only
#   ./scripts/verify.sh --stop    # Stop all services
#   ./scripts/verify.sh --clean   # Full cleanup

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

ACTION="${1:-full}"

cleanup() {
    echo "[INFO] Cleaning up containers..."
    docker-compose down --remove-orphans 2>/dev/null || true
}

build_ci() {
    echo "[INFO] Running CI build verification..."
    docker run --rm \
        --entrypoint /bin/bash \
        -v "${PWD}:/docs" \
        -u "$(id -u):$(id -g)" \
        ghcr.io/robinmordasiewicz/f5xc-mkdocs:latest \
        /docs/scripts/build.sh --ci --output-dir /docs/site

    if [ $? -eq 0 ]; then
        echo "[SUCCESS] CI build completed successfully"
    else
        echo "[ERROR] CI build failed"
        exit 1
    fi
}

serve() {
    cleanup
    echo "[INFO] Starting verification server..."
    docker-compose --profile test up mkdocs-test -d
    echo "[INFO] Server ready at http://localhost:8001"
    echo "[INFO] Use './scripts/verify.sh --stop' to stop the server"
}

case "$ACTION" in
    full|--full)
        build_ci
        serve
        echo ""
        echo "[INFO] Verification complete. Review at http://localhost:8001"
        ;;
    build|--build)
        build_ci
        ;;
    serve|--serve)
        serve
        ;;
    stop|--stop|clean|--clean)
        cleanup
        echo "[INFO] All services stopped"
        ;;
    help|--help|-h)
        echo "Local verification script for f5xc-sizing"
        echo ""
        echo "Usage: $0 [OPTION]"
        echo ""
        echo "Options:"
        echo "  (none), --full    Full verification (build + serve)"
        echo "  --build           CI build only, no server"
        echo "  --serve           Start server only (assumes build exists)"
        echo "  --stop, --clean   Stop all services and cleanup"
        echo "  --help            Show this help message"
        echo ""
        echo "Examples:"
        echo "  ./scripts/verify.sh           # Build and start server"
        echo "  ./scripts/verify.sh --build   # Just run CI build"
        echo "  ./scripts/verify.sh --stop    # Stop running services"
        exit 0
        ;;
    *)
        echo "Unknown option: $ACTION"
        echo "Usage: $0 [--full|--build|--serve|--stop|--clean|--help]"
        exit 1
        ;;
esac
