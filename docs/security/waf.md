# Web Application Firewall (WAF) Sizing

The F5 Distributed Cloud WAF provides comprehensive protection against web
application attacks including OWASP Top 10 vulnerabilities, injection attacks,
cross-site scripting, and advanced threats.

---

## Application Inventory

### Application Count

How many web applications require WAF protection?

| Category | Count |
| --- | --- |
| Production Applications | _____ |
| Staging/QA Applications | _____ |
| Development Applications | _____ |
| **Total Applications** | _____ |

### Application Details

For each major application, provide the following:

| Application Name | Domain/FQDN | Environment | Protocol | Criticality |
| --- | --- | --- | --- | --- |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| _____________ | _____________ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |

!!! info "Additional Applications"
    If you have more than 5 applications, please attach a separate spreadsheet
with complete details.

### Application Architecture

What types of applications are you protecting?

- [ ] Traditional web applications (server-rendered HTML)
- [ ] Single Page Applications (SPA) - React, Angular, Vue
- [ ] Mobile application backends
- [ ] API-only services (covered in API Security section)
- [ ] Legacy applications
- [ ] Microservices
- [ ] Other: _________________

---

## Traffic Volume

### Request Volume

Provide estimated request volumes:

| Metric | Average | Peak |
| --- | --- | --- |
| Requests per Second (RPS) | _____ | _____ |
| Requests per Day | _____ | _____ |
| Requests per Month | _____ | _____ |

!!! note "Base Package Includes"
    Standard tier includes 30 million requests per month from Regional Edges.

### Bandwidth

| Metric | Value | Unit |
| --- | --- | --- |
| Average Inbound Bandwidth | _____ | Mbps |
| Peak Inbound Bandwidth | _____ | Mbps |
| Average Response Size | _____ | KB |

### Geographic Distribution

Where are your users located?

| Region | Percentage of Traffic |
| --- | --- |
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Middle East / Africa | _____% |
| **Total** | 100% |

---

## WAF Features Required

### Core Protection

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

### Advanced Features

Do you require the following advanced features?

| Feature | Required | Notes |
| --- | --- | --- |
| Automatic Signature Tuning | [ ] Yes [ ] No | Reduces false positives automatically |
| Threat Campaigns | [ ] Yes [ ] No | Advanced tier - vetted attack signatures |
| Malicious User Detection | [ ] Yes [ ] No | Advanced tier - behavioral scoring |
| Data Masking | [ ] Yes [ ] No | Mask sensitive data in logs |
| Custom Rules | [ ] Yes [ ] No | Organization-specific signatures |

### Operating Mode

What WAF operating mode do you prefer?

- [ ] **Blocking Mode** - Block malicious requests immediately
- [ ] **Monitoring Mode** - Log but don't block (for initial deployment)
- [ ] **Start in Monitoring, transition to Blocking** after tuning period

Tuning period preference: _____ days/weeks

---

## Origin Infrastructure

### Origin Server Locations

Where are your application origin servers hosted?

| Location | Count | Provider |
| --- | --- | --- |
| AWS | _____ | Region(s): _____________ |
| Azure | _____ | Region(s): _____________ |
| Google Cloud | _____ | Region(s): _____________ |
| On-Premises Data Center | _____ | Location(s): _____________ |
| Other Cloud | _____ | Provider: _____________ |

### Origin Connectivity

How will F5 XC connect to your origin servers?

- [ ] Public Internet (origin servers have public IPs)
- [ ] Private connectivity via Customer Edge sites
- [ ] Direct cloud connectivity (AWS Direct Connect, Azure ExpressRoute, etc.)
- [ ] VPN tunnels

### High Availability

Do you have multiple origin servers per application?

- [ ] Yes - Active/Active load balancing
- [ ] Yes - Active/Standby failover
- [ ] No - Single origin server

Number of origin servers per application: _____

---

## TLS/SSL Configuration

### Certificate Management

How do you want to manage TLS certificates?

- [ ] **Automatic** - F5 XC provisions and manages certificates
- [ ] **Custom** - We will provide our own certificates
- [ ] **Mixed** - Automatic for some, custom for others

### Certificate Details (if Custom)

| Domain | Certificate Type | Expiration | Notes |
| --- | --- | --- | --- |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | _________ | _____ |

### TLS Requirements

- Minimum TLS version required: [ ] TLS 1.2 [ ] TLS 1.3
- Do you require mTLS (Mutual TLS)? [ ] Yes [ ] No
- Cipher suite requirements: _________________

---

## Service Policies

### Access Control Requirements

- [ ] IP Allowlisting (only allow specific IPs)
- [ ] IP Denylisting (block specific IPs)
- [ ] Geographic restrictions (block certain countries)

Number of IP prefixes to manage: _____

### Rate Limiting

- [ ] Yes
- [ ] No

If yes, provide requirements:

| Scope | Limit | Time Window |
| --- | --- | --- |
| Per IP Address | _____ requests | _____ seconds |
| Per User | _____ requests | _____ seconds |
| Per API Endpoint | _____ requests | _____ seconds |

### Geographic Blocking (OFAC Compliance)

- [ ] Yes - OFAC sanctioned countries
- [ ] Yes - Custom country list
- [ ] No

Countries to block: _________________

---

## Logging and Observability

### Log Requirements

What logging capabilities do you need?

- [ ] Security event logging (blocked requests)
- [ ] All request logging
- [ ] Performance metrics
- [ ] Custom log formats

### Log Destinations

Where should logs be sent?

- [ ] F5 XC Console (included)
- [ ] Splunk
- [ ] Datadog
- [ ] AWS S3
- [ ] Azure Blob Storage
- [ ] Sumo Logic
- [ ] Other SIEM: _________________

### Retention Requirements

Log retention period required: _____ days

---

## Support and Management

### Support Requirements

What level of support do you need?

- [ ] **Standard** - Business hours support
- [ ] **Enhanced** - 24x7 support with named resources
- [ ] **Enhanced Plus** - 24x7 support with dedicated resources + SOC

### Managed Services

Do you want F5 to manage WAF policies?

- [ ] **Self-Service** - We will manage policies ourselves
- [ ] **Managed** - F5 SOC manages policies with our input
- [ ] **Hybrid** - Shared responsibility

---

## Summary: WAF Requirements

| Requirement | Value |
| --- | --- |
| Number of Applications | _____ |
| Estimated Monthly Requests | _____ |
| Tier Required | [ ] Standard [ ] Advanced |
| Support Level | [ ] Standard [ ] Enhanced [ ] Enhanced Plus |
| Primary Deployment Region | _____ |

Additional notes or special requirements:

```text
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
