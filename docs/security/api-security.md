# API Security Sizing

F5 Distributed Cloud API Security provides comprehensive protection for your APIs including automatic discovery, schema validation, rate limiting, and behavioral analysis.

---

## Section 1: API Inventory

### 1.1 Do You Need API Security?

- [ ] Yes - We have APIs that need protection
- [ ] No - Skip this section
- [ ] Unsure - We need API discovery to understand our API landscape

### 1.2 API Discovery Requirements

Do you have complete documentation of all your APIs?

- [ ] Yes - All APIs are documented with OpenAPI/Swagger specs
- [ ] Partial - Some APIs are documented
- [ ] No - We need to discover our API landscape

!!! info "Shadow API Discovery"
    F5 XC can automatically discover APIs in your traffic, including undocumented "shadow" APIs that may pose security risks.

### 1.3 Known API Count

If you know your API landscape, provide details:

| Category | Count |
|----------|-------|
| Public APIs (internet-facing) | _____ |
| Partner APIs (B2B) | _____ |
| Internal APIs | _____ |
| **Total API Endpoints** | _____ |

### 1.4 API Details

For major API services, provide:

| API Name/Service | Base Path | Protocol | Auth Method | Documentation |
|-----------------|-----------|----------|-------------|---------------|
| _____________ | /api/v1/... | [ ] REST [ ] GraphQL [ ] gRPC | [ ] API Key [ ] OAuth [ ] JWT [ ] None | [ ] OpenAPI [ ] None |
| _____________ | /api/v1/... | [ ] REST [ ] GraphQL [ ] gRPC | [ ] API Key [ ] OAuth [ ] JWT [ ] None | [ ] OpenAPI [ ] None |
| _____________ | /api/v1/... | [ ] REST [ ] GraphQL [ ] gRPC | [ ] API Key [ ] OAuth [ ] JWT [ ] None | [ ] OpenAPI [ ] None |
| _____________ | /api/v1/... | [ ] REST [ ] GraphQL [ ] gRPC | [ ] API Key [ ] OAuth [ ] JWT [ ] None | [ ] OpenAPI [ ] None |

---

## Section 2: API Traffic Volume

### 2.1 Request Volume

| Metric | Average | Peak |
|--------|---------|------|
| API Requests per Second | _____ | _____ |
| API Requests per Day | _____ | _____ |
| API Requests per Month | _____ | _____ |

!!! note "Base Package"
    Standard includes up to 500,000 API requests per month for API protection.

### 2.2 API Consumer Distribution

Who consumes your APIs?

| Consumer Type | Percentage | Estimated Daily Requests |
|--------------|------------|-------------------------|
| Web Applications (browsers) | _____% | _____ |
| Mobile Applications | _____% | _____ |
| Partner Integrations (B2B) | _____% | _____ |
| Internal Services (M2M) | _____% | _____ |
| Third-Party Developers | _____% | _____ |
| **Total** | 100% | _____ |

---

## Section 3: API Security Features Required

### 3.1 API Discovery

Do you need automatic API discovery?

- [ ] **Yes - Critical** - We need to discover all APIs in our traffic
- [ ] **Yes - Nice to have** - We have docs but want validation
- [ ] **No** - We have complete API documentation

Discovery scope:
- [ ] Production traffic only
- [ ] All environments (Prod, Stage, Dev)

### 3.2 API Schema Validation

Do you need schema-based validation?

- [ ] Yes - Enforce requests match OpenAPI specification
- [ ] No - Skip schema validation

If yes, what actions should be taken on violations?

| Violation Type | Action |
|---------------|--------|
| Unknown endpoints | [ ] Block [ ] Log Only [ ] Allow |
| Invalid request parameters | [ ] Block [ ] Log Only [ ] Allow |
| Invalid request body | [ ] Block [ ] Log Only [ ] Allow |
| Missing required fields | [ ] Block [ ] Log Only [ ] Allow |
| Wrong data types | [ ] Block [ ] Log Only [ ] Allow |

### 3.3 API Rate Limiting

Do you need API-specific rate limiting?

- [ ] Yes
- [ ] No

If yes, provide requirements:

| Rate Limit Type | Limit | Time Window | Action |
|----------------|-------|-------------|--------|
| Per API Key | _____ requests | [ ] second [ ] minute [ ] hour | [ ] Block [ ] Throttle |
| Per User/Token | _____ requests | [ ] second [ ] minute [ ] hour | [ ] Block [ ] Throttle |
| Per Endpoint | _____ requests | [ ] second [ ] minute [ ] hour | [ ] Block [ ] Throttle |
| Per IP Address | _____ requests | [ ] second [ ] minute [ ] hour | [ ] Block [ ] Throttle |
| Global (all traffic) | _____ requests | [ ] second [ ] minute [ ] hour | [ ] Block [ ] Throttle |

### 3.4 Sensitive Data Protection

Do you need sensitive data detection and protection?

- [ ] Yes
- [ ] No

If yes, what data types need detection?

- [ ] Credit Card Numbers (PCI-DSS)
- [ ] Social Security Numbers
- [ ] Email Addresses
- [ ] Phone Numbers
- [ ] Healthcare Data (HIPAA)
- [ ] Custom Patterns: _________________

What action should be taken when sensitive data is detected?

- [ ] Block the request/response
- [ ] Mask the data in transit
- [ ] Log and alert only
- [ ] Allow (detection only)

---

## Section 4: API Authentication and Authorization

### 4.1 Authentication Methods

What authentication methods do your APIs use?

- [ ] API Keys (header or query parameter)
- [ ] OAuth 2.0 / OpenID Connect
- [ ] JWT (JSON Web Tokens)
- [ ] Basic Authentication
- [ ] Mutual TLS (mTLS)
- [ ] Custom authentication
- [ ] No authentication (public APIs)

### 4.2 JWT Validation

If using JWT, do you need F5 XC to validate tokens?

- [ ] Yes - Validate JWT signatures
- [ ] Yes - Validate JWT claims (expiration, audience, etc.)
- [ ] No - Application handles JWT validation

JWT issuer (if applicable): _________________

### 4.3 Authorization Requirements

Do you need authorization enforcement at the API gateway level?

- [ ] Yes - Enforce role-based access to API endpoints
- [ ] No - Application handles authorization

---

## Section 5: API Security Threats

### 5.1 OWASP API Security Top 10

Which API-specific threats are you concerned about?

- [ ] **API1** - Broken Object Level Authorization
- [ ] **API2** - Broken Authentication
- [ ] **API3** - Broken Object Property Level Authorization
- [ ] **API4** - Unrestricted Resource Consumption
- [ ] **API5** - Broken Function Level Authorization
- [ ] **API6** - Unrestricted Access to Sensitive Business Flows
- [ ] **API7** - Server Side Request Forgery (SSRF)
- [ ] **API8** - Security Misconfiguration
- [ ] **API9** - Improper Inventory Management
- [ ] **API10** - Unsafe Consumption of APIs

### 5.2 Historical API Attacks

Have you experienced any API-specific attacks?

- [ ] API scraping / data harvesting
- [ ] Credential stuffing on login APIs
- [ ] Abuse of business logic
- [ ] Inventory/pricing manipulation
- [ ] Enumeration attacks
- [ ] None / Unknown

Describe any specific concerns:

```
_____________________________________________________________
_____________________________________________________________
```

---

## Section 6: OpenAPI Specification Import

### 6.1 Existing Specifications

Do you have OpenAPI/Swagger specifications for your APIs?

- [ ] Yes - OpenAPI 3.x
- [ ] Yes - OpenAPI 2.0 (Swagger)
- [ ] Partial - Some APIs only
- [ ] No - We need to generate specs

### 6.2 Specification Management

How will you manage API specifications?

- [ ] Upload static files to F5 XC
- [ ] Automatic sync from API gateway/management platform
- [ ] Generate from live traffic discovery
- [ ] CI/CD pipeline integration

Number of specification files: _____

### 6.3 Specification Source

Where are your API specifications stored?

- [ ] Git repository
- [ ] API management platform (Apigee, Kong, etc.)
- [ ] Internal documentation system
- [ ] AWS API Gateway
- [ ] Azure API Management
- [ ] Other: _________________

---

## Section 7: Advanced API Security (Advanced Tier)

### 7.1 Behavioral API Security

Do you need behavioral analysis for API traffic?

- [ ] Yes - Detect anomalies in API usage patterns
- [ ] No - Schema validation is sufficient

!!! warning "Advanced Tier Required"
    Behavioral API security with ML-based anomaly detection requires the Advanced tier.

### 7.2 API Posture Management

Do you need API risk scoring and posture assessment?

- [ ] Yes - Score APIs based on security risk
- [ ] No

### 7.3 Data Intelligence Tier

What level of data intelligence do you need?

- [ ] **Basic** - Standard PII detection
- [ ] **Advanced** - Custom patterns + compliance data types
- [ ] **Premium** - Full data classification + custom policies

---

## Section 8: Integration Requirements

### 8.1 Existing API Infrastructure

Do you have existing API management infrastructure?

| Platform | In Use | Integration Needed |
|----------|--------|-------------------|
| AWS API Gateway | [ ] | [ ] |
| Azure API Management | [ ] | [ ] |
| Google Apigee | [ ] | [ ] |
| Kong | [ ] | [ ] |
| MuleSoft | [ ] | [ ] |
| Other: _________ | [ ] | [ ] |

### 8.2 CI/CD Integration

Do you need CI/CD pipeline integration for API security?

- [ ] Yes - Scan API specs before deployment
- [ ] Yes - Security gates in deployment pipeline
- [ ] No

CI/CD platforms in use:
- [ ] Jenkins
- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] Azure DevOps
- [ ] Other: _________________

---

## Summary: API Security Requirements

| Requirement | Value |
|-------------|-------|
| Number of API Endpoints | _____ |
| API Discovery Required | [ ] Yes [ ] No |
| Estimated Monthly API Requests | _____ |
| Schema Validation Required | [ ] Yes [ ] No |
| Sensitive Data Protection Required | [ ] Yes [ ] No |
| Tier Required | [ ] Standard [ ] Advanced |

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
