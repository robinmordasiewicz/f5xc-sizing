# How to Use This Guide

## Overview

This sizing guide is designed to collect all necessary information for accurately scoping your F5 Distributed Cloud deployment. Complete each section that applies to your requirements.

## Guide Structure

### 1. Security Services

Complete these sections if you need:

- [x] Web application protection (WAF)
- [x] API discovery and protection
- [x] Bot detection and mitigation
- [x] DDoS protection
- [x] Client-side JavaScript protection

### 2. Networking Services

Complete these sections if you need:

- [x] Application load balancing
- [x] DNS services and global server load balancing
- [x] Multi-cloud connectivity
- [x] Service mesh capabilities

### 3. Performance Services

Complete these sections if you need:

- [x] Content delivery (CDN)
- [x] Edge computing capabilities

### 4. Infrastructure

Complete these sections if you need:

- [x] On-premises deployments (Customer Edge)
- [x] Cloud-native deployments (AWS, Azure, GCP)

## Response Format

Throughout this guide, you'll encounter different types of questions:

### Yes/No Questions

Indicated by checkboxes:

- [ ] Yes
- [ ] No

### Multiple Choice

Select one or more options as indicated:

- [ ] Option A
- [ ] Option B
- [ ] Option C

### Numeric Values

Enter specific values:

| Field | Value | Unit |
|-------|-------|------|
| Bandwidth | _____ | Mbps |
| Requests | _____ | per second |

### Free-Form Text

Provide detailed information in the designated areas.

## Tips for Completion

!!! tip "Accuracy"
    Provide the most accurate information available. Estimates are acceptable where exact figures are not available.

!!! tip "95th Percentile"
    When providing bandwidth measurements, use 95th percentile values for inbound traffic unless otherwise specified.

!!! tip "Growth Projections"
    Consider 12-24 month growth projections when sizing, not just current state.

!!! tip "Documentation"
    Have network diagrams, traffic reports, and existing security configurations available for reference.

## Saving Your Progress

### Web Browser

Your responses can be:

1. **Printed to PDF** - Use the "Print Site" option for a complete document
2. **Saved as HTML** - Save the page locally for later completion

### Submission

Once complete:

1. Generate PDF using the Print Site feature
2. Review all responses for accuracy
3. Submit to your F5 Account Manager or Sales Engineer

## Need Help?

If you need assistance completing this guide:

| Contact | Details |
|---------|---------|
| F5 Sales | Contact your Account Manager |
| F5 Support | [f5.com/support](https://www.f5.com/support) |
| Documentation | [docs.cloud.f5.com](https://docs.cloud.f5.com) |

## Glossary of Terms

| Term | Definition |
|------|------------|
| **ASN** | Autonomous System Number - unique identifier for a collection of IP networks |
| **BGP** | Border Gateway Protocol - routing protocol for exchanging routing information |
| **CE** | Customer Edge - F5 software deployed at customer sites |
| **CIDR** | Classless Inter-Domain Routing - IP addressing notation (e.g., 10.0.0.0/24) |
| **FQDN** | Fully Qualified Domain Name - complete domain name |
| **GSLB** | Global Server Load Balancing - DNS-based load balancing |
| **mTLS** | Mutual TLS - two-way certificate authentication |
| **PoP** | Point of Presence - F5 regional edge location |
| **RE** | Regional Edge - F5's globally distributed edge infrastructure |
| **WAAP** | Web Application and API Protection |
