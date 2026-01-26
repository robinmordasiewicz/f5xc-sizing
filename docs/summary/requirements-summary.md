# Requirements Summary

This page consolidates all sizing requirements from the questionnaires. Review and complete any missing information before submission.

---

## Customer Information

| Field | Value |
|-------|-------|
| Company Name | _________________ |
| Contact Name | _________________ |
| Contact Email | _________________ |
| Contact Phone | _________________ |
| F5 Account Manager | _________________ |
| Date Completed | _________________ |

---

## Security Services Summary

### Web Application Firewall (WAF)

| Requirement | Value |
|-------------|-------|
| Applications to Protect | _____ |
| Estimated Monthly Requests | _____ M |
| Tier | [ ] Standard [ ] Advanced |
| Threat Campaigns Required | [ ] Yes [ ] No |
| Malicious User Detection | [ ] Yes [ ] No |

### API Security

| Requirement | Value |
|-------------|-------|
| API Endpoints | _____ |
| API Discovery Required | [ ] Yes [ ] No |
| Estimated Monthly API Requests | _____ M |
| Schema Validation | [ ] Yes [ ] No |
| Sensitive Data Protection | [ ] Yes [ ] No |
| Tier | [ ] Standard [ ] Advanced |

### Bot Defense

| Requirement | Value |
|-------------|-------|
| FQDNs to Protect | _____ |
| Daily Transactions | _____ |
| Mobile SDK Required | [ ] Yes [ ] No |
| Detection Method | [ ] Signature [ ] Behavioral |
| Tier | [ ] Standard [ ] Advanced [ ] Premium |

### DDoS Protection

| Requirement | Value |
|-------------|-------|
| Customer ASN | [ ] Yes: _______ [ ] No |
| Network Prefixes | _____ |
| Data Centers | _____ |
| Edge Routers | _____ |
| Clean Bandwidth (95th pct) | _____ Mbps |
| Protection Mode | [ ] Always On [ ] On-Demand |
| L7 DDoS Required | [ ] Yes [ ] No |

### Client-Side Defense

| Requirement | Value |
|-------------|-------|
| Pages to Protect | _____ |
| Monthly Transactions | _____ M |
| PCI-DSS Compliance | [ ] Yes [ ] No |
| Page Tamper Protection | [ ] Yes [ ] No |

---

## Networking Services Summary

### HTTP Load Balancing

| Requirement | Value |
|-------------|-------|
| Number of Load Balancers | _____ |
| Total Applications | _____ |
| Peak Requests/Second | _____ |
| TLS Management | [ ] Automatic [ ] Custom |
| WAF Integration | [ ] Yes [ ] No |
| Multi-Region | [ ] Yes [ ] No |

### TCP Load Balancing

| Requirement | Value |
|-------------|-------|
| Number of TCP LBs | _____ |
| Protocols | [ ] TCP [ ] UDP |
| Peak Connections/Second | _____ |
| TLS Required | [ ] Yes [ ] No |

### DNS Services

| Requirement | Value |
|-------------|-------|
| Total DNS Zones | _____ |
| DNS Load Balancer Records | _____ |
| Health Checks | _____ |
| Estimated QPS | _____ |
| DNSSEC Required | [ ] Yes [ ] No |
| Tier | [ ] Standard [ ] Advanced |

### Multi-Cloud Networking

| Requirement | Value |
|-------------|-------|
| Total Sites | _____ |
| Cloud Environments | _____ |
| On-Prem Data Centers | _____ |
| Edge/Branch Sites | _____ |
| Inter-Site Bandwidth | _____ Mbps |
| Tier | [ ] Standard [ ] Advanced |

### App Connect

| Requirement | Value |
|-------------|-------|
| Total Services | _____ |
| Kubernetes Clusters | _____ |
| Service Mesh Required | [ ] Yes [ ] No |
| mTLS Required | [ ] Yes [ ] No |
| Tier | [ ] Standard [ ] Advanced |

---

## Performance Services Summary

### CDN

| Requirement | Value |
|-------------|-------|
| Domains to CDN | _____ |
| Monthly Requests | _____ M |
| Monthly Data Transfer | _____ GB |
| Security Integration | [ ] Yes [ ] No |

### Edge Compute

| Requirement | Value |
|-------------|-------|
| Edge Locations | _____ |
| Container Workloads | _____ |
| App Stack Required | [ ] Yes [ ] No |

---

## Infrastructure Summary

### Customer Edge Sites

| Requirement | Value |
|-------------|-------|
| Total CE Sites | _____ |
| HA Sites (3-node) | _____ |
| Single Node Sites | _____ |
| Total CE Nodes | _____ |
| Total vCPU | _____ |
| Total RAM | _____ GB |
| App Stack Sites | _____ |

### Cloud Sites

| Requirement | Value |
|-------------|-------|
| AWS Sites | _____ |
| Azure Sites | _____ |
| GCP Sites | _____ |
| Total Cloud Sites | _____ |
| Multi-AZ Deployments | _____ |

---

## Service Tier Summary

| Service | Standard | Advanced |
|---------|:--------:|:--------:|
| WAAP | [ ] | [ ] |
| Network Connect | [ ] | [ ] |
| App Connect | [ ] | [ ] |
| DNS | [ ] | [ ] |
| Bot Defense | [ ] Standard [ ] Advanced [ ] Premium | |

---

## Support Requirements

| Requirement | Selection |
|-------------|-----------|
| Support Level | [ ] Standard [ ] Enhanced [ ] Enhanced Plus |
| Managed Services | [ ] Self-Service [ ] Managed [ ] Hybrid |
| SOC Monitoring | [ ] Yes [ ] No |

---

## Compliance Requirements

Applicable compliance frameworks:

- [ ] PCI-DSS
- [ ] HIPAA
- [ ] GDPR
- [ ] SOC 2
- [ ] FedRAMP
- [ ] ISO 27001
- [ ] Other: _________________

---

## Timeline

| Milestone | Target Date |
|-----------|-------------|
| Requirements Finalized | _____________ |
| Proposal Received | _____________ |
| Contract Signed | _____________ |
| Initial Deployment | _____________ |
| Full Production | _____________ |

---

## Additional Notes

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

---

## Attachments Checklist

- [ ] Network topology diagram
- [ ] Application inventory spreadsheet
- [ ] API specification files (OpenAPI/Swagger)
- [ ] Current traffic reports
- [ ] Existing security configurations
- [ ] Cloud infrastructure diagrams

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Customer Technical Contact | _____________ | _____________ | _____________ |
| Customer Business Contact | _____________ | _____________ | _____________ |
| F5 Account Manager | _____________ | _____________ | _____________ |
| F5 Solutions Engineer | _____________ | _____________ | _____________ |
