# Web Application Firewall (WAF) Sizing

The F5 Distributed Cloud WAF provides comprehensive protection against web application attacks including OWASP Top 10 vulnerabilities, injection attacks, cross-site scripting, and advanced threats.

---

## Section 1: Application Inventory

### 1.1 Application Count

How many web applications require WAF protection?

| Category | Count |
|----------|-------|
| Production Applications | _____ |
| Staging/QA Applications | _____ |
| Development Applications | _____ |
| **Total Applications** | _____ |

### 1.2 Application Details

For each major application, provide the following:

| Application Name | Domain/FQDN | Environment | Protocol | Criticality |
|-----------------|-------------|-------------|----------|-------------|
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |

!!! info "Additional Applications"
    If you have more than 5 applications, please attach a separate spreadsheet with complete details.

### 1.3 Application Architecture

What types of applications are you protecting?

- [ ] Traditional web applications (server-rendered HTML)
- [ ] Single Page Applications (SPA) - React, Angular, Vue
- [ ] Mobile application backends
- [ ] API-only services (covered in API Security section)
- [ ] Legacy applications
- [ ] Microservices
- [ ] Other: _________________

---

## Section 2: Traffic Volume

### 2.1 Request Volume

Provide estimated request volumes:

| Metric | Average | Peak |
|--------|---------|------|
| Requests per Second (RPS) | _____ | _____ |
| Requests per Day | _____ | _____ |
| Requests per Month | _____ | _____ |

!!! note "Base Package Includes"
    Standard tier includes 30 million requests per month from Regional Edges.

### 2.2 Bandwidth

| Metric | Value | Unit |
|--------|-------|------|
| Average Inbound Bandwidth | _____ | Mbps |
| Peak Inbound Bandwidth | _____ | Mbps |
| Average Response Size | _____ | KB |

### 2.3 Geographic Distribution

Where are your users located?

| Region | Percentage of Traffic |
|--------|----------------------|
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Middle East / Africa | _____% |
| **Total** | 100% |

---

## Section 3: WAF Features Required

### 3.1 Core Protection

Which attack types do you need to protect against?

- [ ] SQL Injection
- [ ] Cross-Site Scripting (XSS)
- [ ] Cross-Site Request Forgery (CSRF)
- [ ] Remote File Inclusion (RFI)
- [ ] Local File Inclusion (LFI)
- [ ] Command Injection
- [ ] XML External Entity (XXE)
- [ ] Server-Side Request Forgery (SSRF)
- [ ] HTTP Protocol Violations
- [ ] HTTP Request Smuggling
- [ ] All OWASP Top 10

### 3.2 Advanced Features

Do you require the following advanced features?

| Feature | Required | Notes |
|---------|----------|-------|
| Automatic Signature Tuning | [ ] Yes [ ] No | Reduces false positives automatically |
| Threat Campaigns | [ ] Yes [ ] No | Advanced tier - vetted attack signatures |
| Malicious User Detection | [ ] Yes [ ] No | Advanced tier - behavioral scoring |
| Data Masking | [ ] Yes [ ] No | Mask sensitive data in logs |
| Custom Rules | [ ] Yes [ ] No | Organization-specific signatures |

### 3.3 Operating Mode

What WAF operating mode do you prefer?

- [ ] **Blocking Mode** - Block malicious requests immediately
- [ ] **Monitoring Mode** - Log but don't block (for initial deployment)
- [ ] **Start in Monitoring, transition to Blocking** after tuning period

Tuning period preference: _____ days/weeks

---

## Section 4: Origin Infrastructure

### 4.1 Origin Server Locations

Where are your application origin servers hosted?

| Location | Count | Provider |
|----------|-------|----------|
| AWS | _____ | Region(s): _____________ |
| Azure | _____ | Region(s): _____________ |
| Google Cloud | _____ | Region(s): _____________ |
| On-Premises Data Center | _____ | Location(s): _____________ |
| Other Cloud | _____ | Provider: _____________ |

### 4.2 Origin Connectivity

How will F5 XC connect to your origin servers?

- [ ] Public Internet (origin servers have public IPs)
- [ ] Private connectivity via Customer Edge sites
- [ ] Direct cloud connectivity (AWS Direct Connect, Azure ExpressRoute, etc.)
- [ ] VPN tunnels

### 4.3 High Availability

Do you have multiple origin servers per application?

- [ ] Yes - Active/Active load balancing
- [ ] Yes - Active/Standby failover
- [ ] No - Single origin server

Number of origin servers per application: _____

---

## Section 5: TLS/SSL Configuration

### 5.1 Certificate Management

How do you want to manage TLS certificates?

- [ ] **Automatic** - F5 XC provisions and manages certificates
- [ ] **Custom** - We will provide our own certificates
- [ ] **Mixed** - Automatic for some, custom for others

### 5.2 Certificate Details (if Custom)

| Domain | Certificate Type | Expiration | Notes |
|--------|-----------------|------------|-------|
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |

### 5.3 TLS Requirements

- Minimum TLS version required: [ ] TLS 1.2 [ ] TLS 1.3
- Do you require mTLS (Mutual TLS)? [ ] Yes [ ] No
- Cipher suite requirements: _________________

---

## Section 6: Service Policies

### 6.1 Access Control Requirements

Do you need IP-based access controls?

- [ ] IP Allowlisting (only allow specific IPs)
- [ ] IP Denylisting (block specific IPs)
- [ ] Geographic restrictions (block certain countries)

Number of IP prefixes to manage: _____

### 6.2 Rate Limiting

Do you need rate limiting?

- [ ] Yes
- [ ] No

If yes, provide requirements:

| Scope | Limit | Time Window |
|-------|-------|-------------|
| Per IP Address | _____ requests | _____ seconds |
| Per User | _____ requests | _____ seconds |
| Per API Endpoint | _____ requests | _____ seconds |

### 6.3 Geographic Blocking (OFAC Compliance)

Do you need to block traffic from specific countries?

- [ ] Yes - OFAC sanctioned countries
- [ ] Yes - Custom country list
- [ ] No

Countries to block: _________________

---

## Section 7: Logging and Observability

### 7.1 Log Requirements

What logging capabilities do you need?

- [ ] Security event logging (blocked requests)
- [ ] All request logging
- [ ] Performance metrics
- [ ] Custom log formats

### 7.2 Log Destinations

Where should logs be sent?

- [ ] F5 XC Console (included)
- [ ] Splunk
- [ ] Datadog
- [ ] AWS S3
- [ ] Azure Blob Storage
- [ ] Sumo Logic
- [ ] Other SIEM: _________________

### 7.3 Retention Requirements

Log retention period required: _____ days

---

## Section 8: Support and Management

### 8.1 Support Requirements

What level of support do you need?

- [ ] **Standard** - Business hours support
- [ ] **Enhanced** - 24x7 support with named resources
- [ ] **Enhanced Plus** - 24x7 support with dedicated resources + SOC

### 8.2 Managed Services

Do you want F5 to manage WAF policies?

- [ ] **Self-Service** - We will manage policies ourselves
- [ ] **Managed** - F5 SOC manages policies with our input
- [ ] **Hybrid** - Shared responsibility

---

## Summary: WAF Requirements

| Requirement | Value |
|-------------|-------|
| Number of Applications | _____ |
| Estimated Monthly Requests | _____ |
| Tier Required | [ ] Standard [ ] Advanced |
| Support Level | [ ] Standard [ ] Enhanced [ ] Enhanced Plus |
| Primary Deployment Region | _____ |

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
