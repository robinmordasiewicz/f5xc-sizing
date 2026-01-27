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
| Production Applications | ___ |
| Staging/QA Applications | ___ |
| Development Applications | ___ |
| **Total Applications** | ___ |

### Application Details

For each major application, provide the following:

| Application Name | Domain/FQDN | Environment | Protocol | Criticality |
| --- | --- | --- | --- | --- |
| ___ | ___ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| ___ | ___ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| ___ | ___ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| ___ | ___ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |
| ___ | ___ | [ ] Prod [ ] Stage [ ] Dev | [ ] HTTP [ ] HTTPS | [ ] Critical [ ] High [ ] Medium [ ] Low |

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
- [ ] Other: ___

---

## Traffic Volume

### Request Volume

Provide estimated request volumes:

| Metric | Average | Peak |
| --- | --- | --- |
| Requests per Second (RPS) | ___ | ___ |
| Requests per Day | ___ | ___ |
| Requests per Month | ___ | ___ |

!!! note "Base Package Includes"
    Standard tier includes 30 million requests per month from Regional Edges.

### Bandwidth

| Metric | Value | Unit |
| --- | --- | --- |
| Average Inbound Bandwidth | ___ | Mbps |
| Peak Inbound Bandwidth | ___ | Mbps |
| Average Response Size | ___ | KB |

### Geographic Distribution

Where are your users located?

| Region | Percentage of Traffic |
| --- | --- |
| North America | ___ % |
| Europe | ___ % |
| Asia-Pacific | ___ % |
| South America | ___ % |
| Middle East / Africa | ___ % |
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

Tuning period preference: ___ days/weeks

---

## Origin Infrastructure

### Origin Server Locations

Where are your application origin servers hosted?

| Location | Count | Provider |
| --- | --- | --- |
| AWS | ___ | Region(s): ___ |
| Azure | ___ | Region(s): ___ |
| Google Cloud | ___ | Region(s): ___ |
| On-Premises Data Center | ___ | Location(s): ___ |
| Other Cloud | ___ | Provider: ___ |

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

Number of origin servers per application: ___

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
| ___ | [ ] Single [ ] Wildcard [ ] SAN | ___ | ___ |
| ___ | [ ] Single [ ] Wildcard [ ] SAN | ___ | ___ |
| ___ | [ ] Single [ ] Wildcard [ ] SAN | ___ | ___ |

### TLS Requirements

- Minimum TLS version required: [ ] TLS 1.2 [ ] TLS 1.3
- Do you require mTLS (Mutual TLS)? [ ] Yes [ ] No
- Cipher suite requirements: ___

---

## Service Policies

### Access Control Requirements

- [ ] IP Allowlisting (only allow specific IPs)
- [ ] IP Denylisting (block specific IPs)
- [ ] Geographic restrictions (block certain countries)

Number of IP prefixes to manage: ___

### Rate Limiting

- [ ] Yes
- [ ] No

If yes, provide requirements:

| Scope | Limit | Time Window |
| --- | --- | --- |
| Per IP Address | ___ requests | ___ seconds |
| Per User | ___ requests | ___ seconds |
| Per API Endpoint | ___ requests | ___ seconds |

### Geographic Blocking (OFAC Compliance)

- [ ] Yes - OFAC sanctioned countries
- [ ] Yes - Custom country list
- [ ] No

Countries to block: ___

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
- [ ] Other SIEM: ___

### Retention Requirements

Log retention period required: ___ days

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
| Number of Applications | ___ |
| Estimated Monthly Requests | ___ |
| Tier Required | [ ] Standard [ ] Advanced |
| Support Level | [ ] Standard [ ] Enhanced [ ] Enhanced Plus |
| Primary Deployment Region | ___ |

Additional notes or special requirements:

```text
___
```
