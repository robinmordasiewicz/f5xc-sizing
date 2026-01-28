# F5 XC Sizing - Claude Code Instructions

## Build & Verification

### MANDATORY: Single Verification Command

```bash
./scripts/verify.sh
```

This command:
1. Runs CI build (identical to GitHub Actions)
2. Cleans up any previous containers
3. Starts verification server at http://localhost:8001

### Script Options

| Command | Purpose |
|---------|---------|
| `./scripts/verify.sh` | Full verification (build + serve) |
| `./scripts/verify.sh --build` | CI build only, no server |
| `./scripts/verify.sh --serve` | Start server only |
| `./scripts/verify.sh --stop` | Stop all services |
| `./scripts/verify.sh --help` | Show usage help |

### FORBIDDEN

- ❌ Running docker commands directly
- ❌ Running `mkdocs` commands directly
- ❌ Ad-hoc workarounds for port conflicts
- ❌ Any command not in this document

## Success Criteria

After running `./scripts/verify.sh --build`:
- Exit code 0
- No ERROR messages in output
- PDF count reported (e.g., "Generated 15 PDF files")
- Form fields added (e.g., "All PDFs processed with form fields")
- Output: "CI build complete. Output: /docs/site"

## Failure Handling

If build fails:
1. Read the full error output
2. Fix the root cause in source files
3. Re-run `./scripts/verify.sh --build`
4. Never work around failures with manual commands

## Project Structure

```
f5xc-sizing/
├── scripts/
│   ├── build.sh              # Unified build orchestrator
│   ├── verify.sh             # Local verification (this doc)
│   └── add_pdf_forms.py      # PDF form field injection
├── docs/                     # Source documentation
├── site/                     # Build output (CI mode)
├── docker-compose.yml        # Local development services
├── mkdocs.yml               # MkDocs configuration
└── CLAUDE.md                # This file
```

## CI/CD Parity

The `verify.sh` script runs the **exact same build** as `.github/workflows/deploy.yml`:
- Same Docker image: `ghcr.io/robinmordasiewicz/f5xc-mkdocs:latest`
- Same build script: `/docs/scripts/build.sh --ci`
- Same output directory: `/docs/site`
- Same user permissions
