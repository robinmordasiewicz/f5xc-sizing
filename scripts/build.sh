#!/bin/bash
# Unified build script for MkDocs documentation
# Works in both local development and CI/CD environments
#
# Usage:
#   ./scripts/build.sh --serve       # Development with live reload
#   ./scripts/build.sh --test        # Production test with static server
#   ./scripts/build.sh --ci          # CI/CD build (no server)
#   ./scripts/build.sh --output-dir  # Custom output directory

set -e

# Default values
OUTPUT_DIR="site"
DOCS_DIR=""
MODE="build"
SERVE_ADDR="0.0.0.0:8000"
SKIP_PDF=false
VERBOSE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --serve       Build PDF, then start MkDocs dev server (live reload)"
    echo "  --test        Build production site and serve with static server"
    echo "  --ci          Build production site for CI/CD (no server)"
    echo "  --output-dir  Output directory (default: site)"
    echo "  --skip-pdf    Skip PDF generation"
    echo "  --verbose     Enable verbose output"
    echo "  -h, --help    Show this help message"
    exit 0
}

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --serve)
            MODE="serve"
            shift
            ;;
        --test)
            MODE="test"
            shift
            ;;
        --ci)
            MODE="ci"
            shift
            ;;
        --output-dir)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --skip-pdf)
            SKIP_PDF=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            log_error "Unknown option: $1"
            usage
            ;;
    esac
done

# Detect environment (inside Docker or local)
if [ -d "/docs" ] && [ -f "/docs/mkdocs.yml" ]; then
    DOCS_DIR="/docs"
else
    DOCS_DIR="$(cd "$(dirname "$0")/.." && pwd)"
fi

cd "$DOCS_DIR"
log_info "Working directory: $DOCS_DIR"
log_info "Build mode: $MODE"

# Build PDF function (for serve mode - builds PDF to docs/ for live reload)
build_pdf_for_serve() {
    if [ "$SKIP_PDF" = true ]; then
        log_warn "Skipping PDF generation (--skip-pdf)"
        return
    fi

    log_info "Generating PDF documentation..."

    local PDF_BUILD_DIR="/tmp/pdf-build"
    ENABLE_PDF_EXPORT=1 mkdocs build --site-dir "$PDF_BUILD_DIR"

    # Copy PDF to docs directory for live reload access
    mkdir -p "$DOCS_DIR/docs/pdf"
    cp "$PDF_BUILD_DIR/pdf/document.pdf" "$DOCS_DIR/docs/pdf/document.pdf"
    log_info "PDF generated: docs/pdf/document.pdf"

    # Post-process PDF to add interactive form fields
    log_info "Adding interactive form fields to PDF..."
    python3 "$DOCS_DIR/scripts/add_pdf_forms.py" \
        --input "$DOCS_DIR/docs/pdf/document.pdf" \
        --output "$DOCS_DIR/docs/pdf/document.pdf" \
        --markdown-dir "$DOCS_DIR/docs/"
    log_info "Interactive form fields added"

    # Clean up temp build
    rm -rf "$PDF_BUILD_DIR"
}

# Build production site function
build_site() {
    log_info "Building production site to: $OUTPUT_DIR"
    ENABLE_PDF_EXPORT=1 mkdocs build --site-dir "$OUTPUT_DIR"
    log_info "Site built successfully"

    # Count PDFs generated
    local PDF_COUNT
    PDF_COUNT=$(find "$OUTPUT_DIR" -name "*.pdf" -type f | wc -l)
    log_info "Generated $PDF_COUNT PDF files"

    # Post-process ALL PDFs to add interactive form fields
    if [ "$PDF_COUNT" -gt 0 ]; then
        log_info "Adding interactive form fields to all PDFs..."
        python3 "$DOCS_DIR/scripts/add_pdf_forms.py" \
            --input-dir "$OUTPUT_DIR" \
            --markdown-dir "$DOCS_DIR/docs/"
        log_info "All PDFs processed with form fields"
    else
        log_warn "No PDFs found in $OUTPUT_DIR"
    fi
}

# Main execution based on mode
case $MODE in
    serve)
        # Development mode: Build PDF once, then serve with live reload
        build_pdf_for_serve
        log_info "Starting MkDocs development server..."
        echo ""
        echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
        echo -e "${GREEN}  Local development server ready${NC}"
        echo -e "${GREEN}  Preview: ${NC}http://localhost:8000"
        echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
        echo ""
        exec mkdocs serve --dev-addr "$SERVE_ADDR"
        ;;
    test)
        # Test mode: Build production site, serve with static server
        OUTPUT_DIR="/tmp/site"
        build_site
        echo ""
        echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
        echo -e "${GREEN}  Production test server ready${NC}"
        echo -e "${GREEN}  Preview: ${NC}http://localhost:8000"
        echo -e "${GREEN}──────────────────────────────────────────────────────────────${NC}"
        echo -e "  This build includes:"
        echo -e "    • Per-page PDF download buttons"
        echo -e "    • Full PDF document with form fields"
        echo -e "    • All production features"
        echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
        echo ""
        cd "$OUTPUT_DIR"
        exec python -m http.server 8000
        ;;
    ci)
        # CI mode: Build production site, no server
        build_site
        log_info "CI build complete. Output: $OUTPUT_DIR"
        ;;
    build)
        # Default: Just build, no server
        build_site
        ;;
esac
