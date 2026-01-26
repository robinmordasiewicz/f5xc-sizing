# Security Services Overview

F5 Distributed Cloud provides comprehensive security services to protect your applications, APIs, and infrastructure from a wide range of threats.

## Security Services Portfolio

<div class="grid cards" markdown>

-   :material-shield-lock:{ .lg .middle } **Web Application Firewall**

    ---

    Protection against OWASP Top 10, injection attacks, XSS, and advanced web threats with automatic signature tuning.

    [:octicons-arrow-right-24: WAF Questionnaire](waf.md)

-   :material-api:{ .lg .middle } **API Security**

    ---

    Automatic API discovery, schema validation, rate limiting, and behavioral analysis for API protection.

    [:octicons-arrow-right-24: API Security Questionnaire](api-security.md)

-   :material-robot:{ .lg .middle } **Bot Defense**

    ---

    AI/ML-powered detection and mitigation of credential stuffing, account takeover, and automated threats.

    [:octicons-arrow-right-24: Bot Defense Questionnaire](bot-defense.md)

-   :material-shield-alert:{ .lg .middle } **DDoS Protection**

    ---

    Multi-terabit L3-L7 attack mitigation with always-on or on-demand deployment options.

    [:octicons-arrow-right-24: DDoS Questionnaire](ddos.md)

-   :material-language-javascript:{ .lg .middle } **Client-Side Defense**

    ---

    Protection against Magecart, formjacking, and malicious JavaScript supply chain attacks.

    [:octicons-arrow-right-24: Client-Side Defense Questionnaire](client-side-defense.md)

</div>

## Security Assessment Checklist

Before proceeding with detailed questionnaires, assess which security services you need:

| Security Requirement | Service | Priority |
|---------------------|---------|----------|
| Protect web applications from common attacks | WAF | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Discover and protect APIs | API Security | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Block automated/bot traffic | Bot Defense | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Protect against volumetric attacks | DDoS Protection | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Protect against client-side threats | Client-Side Defense | [ ] High [ ] Medium [ ] Low [ ] N/A |

## Compliance Requirements

Which compliance frameworks must your security controls address?

- [ ] PCI-DSS (Payment Card Industry)
- [ ] HIPAA (Healthcare)
- [ ] GDPR (European Data Protection)
- [ ] SOC 2
- [ ] FedRAMP
- [ ] ISO 27001
- [ ] Other: _________________

## Current Security Posture

### Existing Security Solutions

Do you currently have any of the following in place?

| Solution Type | Vendor/Product | Replace or Integrate? |
|--------------|----------------|----------------------|
| WAF | _____________ | [ ] Replace [ ] Integrate |
| Bot Management | _____________ | [ ] Replace [ ] Integrate |
| DDoS Protection | _____________ | [ ] Replace [ ] Integrate |
| API Gateway | _____________ | [ ] Replace [ ] Integrate |
| CDN with Security | _____________ | [ ] Replace [ ] Integrate |

### Attack History

Have you experienced any of the following in the past 12 months?

- [ ] DDoS attacks
- [ ] Bot attacks / Credential stuffing
- [ ] Web application attacks (SQL injection, XSS, etc.)
- [ ] API abuse
- [ ] Account takeover
- [ ] Data breach
- [ ] Supply chain / Client-side attacks

If yes, please describe:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

## Proceed to Detailed Questionnaires

Complete each security service questionnaire that applies to your requirements:

1. [Web Application Firewall (WAF)](waf.md)
2. [API Security](api-security.md)
3. [Bot Defense](bot-defense.md)
4. [DDoS Protection](ddos.md)
5. [Client-Side Defense](client-side-defense.md)
