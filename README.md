# F5 Distributed Cloud Sizing Guide

A comprehensive sizing questionnaire for F5 Distributed Cloud (F5 XC) deployments, built with Material for MkDocs.

## Overview

This repository contains an interactive sizing guide that helps customers and sales engineers accurately scope F5 Distributed Cloud deployments. The guide covers all major F5 XC service categories:

### Security Services
- **Web Application Firewall (WAF)** - OWASP Top 10 protection, signature tuning
- **API Security** - API discovery, schema validation, rate limiting
- **Bot Defense** - AI/ML-powered bot detection and mitigation
- **DDoS Protection** - L3-L7 attack mitigation, always-on/on-demand
- **Client-Side Defense** - Magecart, formjacking protection

### Networking Services
- **HTTP Load Balancing** - Global application delivery
- **TCP Load Balancing** - Layer 4 load balancing
- **DNS Services** - DNS hosting and GSLB
- **Multi-Cloud Networking** - Site-to-site connectivity
- **App Connect** - Service mesh capabilities

### Performance Services
- **CDN** - Content delivery and caching
- **Edge Compute** - Edge processing capabilities

### Infrastructure
- **Customer Edge Sites** - On-premises deployments
- **Cloud Sites** - AWS, Azure, GCP deployments

## Live Site

Visit the live sizing guide at: https://robinmordasiewicz.github.io/f5xc-sizing/

## Local Development

### Using Docker (Recommended)

```bash
# Serve locally with live reload
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs ghcr.io/robinmordasiewicz/f5xc-mkdocs:latest serve -a 0.0.0.0:8000

# Build static site
docker run --rm -v ${PWD}:/docs ghcr.io/robinmordasiewicz/f5xc-mkdocs:latest build
```

### Using Python

```bash
# Install dependencies
pip install mkdocs-material mkdocs-print-site-plugin

# Serve locally
mkdocs serve

# Build static site
mkdocs build
```

## PDF Export

The guide includes a print-site plugin that allows exporting the entire guide to PDF:

1. Navigate to the "Print Site" page in the navigation
2. Use your browser's print function (Ctrl+P / Cmd+P)
3. Select "Save as PDF"

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Submit a pull request

## Branch Protection

The `main` branch is protected and requires:
- Pull request reviews before merging
- Status checks to pass

## License

Copyright © F5, Inc. All rights reserved.

## Resources

- [F5 Distributed Cloud Documentation](https://docs.cloud.f5.com)
- [F5 Community](https://community.f5.com)
- [F5 DevCentral](https://devcentral.f5.com)
