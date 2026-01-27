#!/bin/sh
# Build and serve production-like site for testing
# Includes PDF generation and per-page PDF download buttons

set -e

echo "Building production-like site with all features enabled..."
ENABLE_PDF_EXPORT=1 mkdocs build --site-dir /tmp/site

echo "Site built successfully at /tmp/site"
echo "Serving on http://localhost:8000 (mapped to host port 8001)"
echo ""
echo "This build includes:"
echo "  - Per-page PDF download buttons"
echo "  - Full PDF document generation"
echo "  - All production features"
echo ""

cd /tmp/site
exec python -m http.server 8000
