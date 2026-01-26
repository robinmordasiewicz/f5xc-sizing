# Client-Side Defense Sizing

F5 Distributed Cloud Client-Side Defense provides protection against Magecart, formjacking, digital skimming, and other malicious JavaScript supply chain attacks.

---

## Section 1: Requirements Assessment

### 1.1 Do You Need Client-Side Defense?

- [ ] Yes - We handle sensitive data in web forms
- [ ] No - Skip this section
- [ ] Unsure - We need to assess our client-side risk

### 1.2 Client-Side Security Concerns

What client-side threats are you concerned about?

- [ ] **Magecart attacks** - Credit card skimming via JavaScript
- [ ] **Formjacking** - Credential theft from forms
- [ ] **Digital skimming** - PII harvesting
- [ ] **Supply chain attacks** - Compromised third-party scripts
- [ ] **Data exfiltration** - Unauthorized data transmission
- [ ] **Page tampering** - Unauthorized DOM modifications

Have you experienced client-side attacks?

- [ ] Yes - Describe: _________________
- [ ] No
- [ ] Unknown

---

## Section 2: Application Scope

### 2.1 Pages Requiring Protection

Which pages handle sensitive data and require protection?

| Page Type | URL Pattern | Sensitive Data Type |
|-----------|-------------|---------------------|
| Login pages | _____________ | [ ] Credentials |
| Registration forms | _____________ | [ ] PII |
| Checkout/Payment | _____________ | [ ] Payment card data |
| Account settings | _____________ | [ ] PII [ ] Financial |
| Contact forms | _____________ | [ ] PII |
| Other: _______ | _____________ | _____________ |

### 2.2 Transaction Volume

Estimated monthly transactions on protected pages:

| Metric | Monthly Volume |
|--------|----------------|
| Total page views (protected pages) | _____ |
| Form submissions | _____ |
| Payment transactions | _____ |

!!! note "Base Package"
    Client-Side Defense includes 1 million transactions in the base package.

---

## Section 3: JavaScript Environment

### 3.1 Third-Party Scripts

How many third-party JavaScript resources are loaded on your pages?

| Category | Estimated Count |
|----------|-----------------|
| Analytics (Google Analytics, etc.) | _____ |
| Marketing/Advertising | _____ |
| Social media widgets | _____ |
| Chat/Support widgets | _____ |
| Payment processors | _____ |
| A/B testing tools | _____ |
| Other third-party scripts | _____ |
| **Total third-party scripts** | _____ |

### 3.2 Script Sources

Where do your JavaScript resources come from?

- [ ] First-party (your own domains)
- [ ] CDN-hosted (cdnjs, jsdelivr, etc.)
- [ ] Direct third-party domains
- [ ] Tag managers (Google Tag Manager, etc.)

List critical third-party script sources:

| Script Purpose | Source Domain | Critical? |
|---------------|---------------|-----------|
| _____________ | _____________ | [ ] Yes [ ] No |
| _____________ | _____________ | [ ] Yes [ ] No |
| _____________ | _____________ | [ ] Yes [ ] No |
| _____________ | _____________ | [ ] Yes [ ] No |

### 3.3 Content Security Policy (CSP)

Do you currently have a Content Security Policy?

- [ ] Yes - Strict CSP
- [ ] Yes - Reporting-only mode
- [ ] No - No CSP implemented
- [ ] Unknown

---

## Section 4: Compliance Requirements

### 4.1 PCI-DSS Requirements

Are you subject to PCI-DSS compliance?

- [ ] Yes - PCI-DSS Level 1
- [ ] Yes - PCI-DSS Level 2
- [ ] Yes - PCI-DSS Level 3-4
- [ ] No

!!! info "PCI-DSS 4.0"
    PCI-DSS 4.0 includes requirements (6.4.3 and 11.6.1) for monitoring and controlling client-side scripts on payment pages.

### 4.2 Other Compliance

Which other compliance frameworks apply?

- [ ] GDPR
- [ ] CCPA
- [ ] HIPAA
- [ ] SOC 2
- [ ] Other: _________________

---

## Section 5: Detection and Alerting

### 5.1 Detection Capabilities

What detection capabilities do you need?

- [ ] **Script behavior monitoring** - Detect changes in script behavior
- [ ] **Network request monitoring** - Detect unauthorized data exfiltration
- [ ] **Form field monitoring** - Detect unauthorized form reads
- [ ] **DOM manipulation detection** - Detect unauthorized page changes
- [ ] **Page tamper detection** - Detect payment page modifications

### 5.2 Alerting Requirements

How should you be notified of detected threats?

- [ ] Email alerts
- [ ] F5 XC Console alerts
- [ ] Webhook integration
- [ ] SIEM integration

Alert severity thresholds:

| Alert Type | Severity |
|------------|----------|
| New third-party script detected | [ ] Critical [ ] High [ ] Medium [ ] Low |
| Script behavior change | [ ] Critical [ ] High [ ] Medium [ ] Low |
| Data exfiltration attempt | [ ] Critical [ ] High [ ] Medium [ ] Low |
| Page tampering detected | [ ] Critical [ ] High [ ] Medium [ ] Low |

---

## Section 6: Mitigation Actions

### 6.1 Response Actions

What actions should be taken when threats are detected?

| Threat Type | Action |
|-------------|--------|
| Malicious script detected | [ ] Block [ ] Alert only |
| Data exfiltration attempt | [ ] Block [ ] Alert only |
| Unauthorized form access | [ ] Block [ ] Alert only |
| Page tampering | [ ] Block [ ] Alert only |

### 6.2 Blocking Method

If blocking, how should blocking be implemented?

- [ ] **Block network calls** - Prevent exfiltration to malicious domains
- [ ] **Remove malicious script** - Strip script from page
- [ ] **Redirect to safe page** - Show user a warning

---

## Section 7: Integration

### 7.1 Deployment Method

How will Client-Side Defense be deployed?

- [ ] F5 XC proxy (automatic JavaScript injection)
- [ ] Manual JavaScript tag insertion
- [ ] BIG-IP integration (iApp or native module)
- [ ] CDN integration

### 7.2 Existing BIG-IP

Do you have F5 BIG-IP that could integrate with Client-Side Defense?

- [ ] Yes - BIG-IP version: _____
- [ ] No

---

## Section 8: Page Tamper Protection

### 8.1 Payment Page Monitoring

Do you need Page Tamper Protection for payment pages?

- [ ] Yes - Monitor payment page integrity
- [ ] No

If yes, provide payment page URLs:

| Payment Page URL | Expected Update Frequency |
|-----------------|--------------------------|
| _____________ | [ ] Rarely [ ] Monthly [ ] Weekly [ ] Daily |
| _____________ | [ ] Rarely [ ] Monthly [ ] Weekly [ ] Daily |

### 8.2 Baseline Management

How often do your payment pages legitimately change?

- [ ] Rarely (quarterly or less)
- [ ] Monthly
- [ ] Weekly
- [ ] Frequently (daily or more)

---

## Summary: Client-Side Defense Requirements

| Requirement | Value |
|-------------|-------|
| Number of Protected Pages | _____ |
| Estimated Monthly Transactions | _____ |
| Third-Party Scripts to Monitor | _____ |
| PCI-DSS Compliance Required | [ ] Yes [ ] No |
| Page Tamper Protection Required | [ ] Yes [ ] No |
| Detection Mode | [ ] Monitor [ ] Block |

Critical pages requiring protection:

```
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________
```

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
