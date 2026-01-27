# HTTP Load Balancer Sizing

F5 Distributed Cloud HTTP Load Balancer provides global application delivery
with intelligent routing, health checks, TLS termination, and integration with
security services.

---

## Load Balancer Requirements

### Application Inventory

How many HTTP/HTTPS applications need load balancing?

| Environment | Application Count |
| --- | --- |
| Production | _____ |
| Staging/QA | _____ |
| Development | _____ |
| **Total** | _____ |

### Virtual Host Details

For each application, provide virtual host information:

| Application Name | Domain(s) | Port(s) | Protocol |
| --- | --- | --- | --- |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |

!!! note "Base Package"
    The base package includes 1 load balancer. Additional load balancers are
available as add-ons.

---

## Traffic Volume

### Request Metrics

| Metric | Average | Peak |
| --- | --- | --- |
| Requests per second | _____ | _____ |
| Concurrent connections | _____ | _____ |
| Bandwidth (Mbps) | _____ | _____ |

### Traffic Patterns

What are your traffic patterns?

- [ ] Steady throughout the day
- [ ] Business hours peaks
- [ ] Seasonal peaks (specify): _________________
- [ ] Event-driven spikes
- [ ] Unpredictable

Geographic distribution of users:

| Region | Traffic Percentage |
| --- | --- |
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Other | _____% |

---

## Origin Pool Configuration

### Origin Server Details

For each application, describe origin servers:

| Application | Origin Type | Count | Location |
| --- | --- | --- | --- |
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |

### Origin Connectivity

How will F5 XC reach your origin servers?

- [ ] **Public Internet** - Origins have public IP addresses
- [ ] **Customer Edge** - Via F5 CE deployed in your environment
- [ ] **Cloud Site** - Via F5 site in AWS/Azure/GCP
- [ ] **Private Link** - Direct cloud connectivity

### Origin Protocol

What protocol to use when connecting to origins?

| Application | Origin Protocol | Origin Port |
| --- | --- | --- |
| _____________ | [ ] HTTP [ ] HTTPS | _____ |
| _____________ | [ ] HTTP [ ] HTTPS | _____ |
| _____________ | [ ] HTTP [ ] HTTPS | _____ |

---

## Load Balancing Configuration

### Load Balancing Algorithm

Preferred load balancing algorithm:

- [ ] **Round Robin** - Distribute evenly across origins
- [ ] **Least Connections** - Send to origin with fewest active connections
- [ ] **Random** - Random selection
- [ ] **Source IP Hash** - Consistent routing based on client IP
- [ ] **Ring Hash** - Consistent hashing for cache efficiency

### Session Persistence

- [ ] Yes - Source IP based
- [ ] Yes - Cookie based
- [ ] Yes - Header based
- [ ] No - Stateless application

Persistence timeout: _____ seconds

### Health Checks

Health check requirements:

| Parameter | Value |
| --- | --- |
| Health check type | [ ] HTTP [ ] HTTPS [ ] TCP |
| Check interval | _____ seconds |
| Check path (HTTP) | _____________ |
| Expected response code | [ ] 200 [ ] 2xx [ ] Custom: ___ |
| Healthy threshold | _____ consecutive checks |
| Unhealthy threshold | _____ consecutive checks |

---

## TLS Configuration

### TLS Termination

Where should TLS be terminated?

- [ ] **At F5 XC** - F5 terminates TLS, connects to origin over HTTP/HTTPS
- [ ] **End-to-End** - F5 terminates and re-encrypts to origin
- [ ] **Pass-Through** - TLS passes through to origin (TCP LB only)

### Certificate Management

How will TLS certificates be managed?

- [ ] **Automatic** - F5 XC provisions via Let's Encrypt
- [ ] **Custom** - We provide our own certificates
- [ ] **Mixed** - Different per application

Custom certificate details:

| Domain | Certificate Type | Key Type |
| --- | --- | --- |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | [ ] RSA 2048 [ ] RSA 4096 [ ] ECC |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | [ ] RSA 2048 [ ] RSA 4096 [ ] ECC |

### TLS Requirements

| Requirement | Value |
| --- | --- |
| Minimum TLS version | [ ] TLS 1.2 [ ] TLS 1.3 |
| Cipher suite preference | [ ] Default [ ] Custom |
| HSTS enabled | [ ] Yes [ ] No |
| HTTP to HTTPS redirect | [ ] Yes [ ] No |

### Mutual TLS (mTLS)

Do you require mTLS client authentication?

- [ ] Yes - Clients must present certificates
- [ ] No

If yes:

- Client CA certificate source: _________________
- XFCC header forwarding needed: [ ] Yes [ ] No

---

## Traffic Management

### Routing Rules

- [ ] **Path-based routing** - Route based on URL path
- [ ] **Header-based routing** - Route based on HTTP headers
- [ ] **Query parameter routing** - Route based on query strings
- [ ] **Method-based routing** - Route based on HTTP method

Example routing requirements:

| Condition | Destination |
| --- | --- |
| Path: /api/* | API origin pool |
| Header: X-Version: v2 | V2 origin pool |
| _____________ | _____________ |

### Traffic Policies

- [ ] Request header insertion/modification
- [ ] Response header insertion/modification
- [ ] URL rewriting
- [ ] Request body buffering
- [ ] Response compression

### Timeouts and Limits

| Parameter | Value |
| --- | --- |
| Request timeout | _____ seconds |
| Idle timeout | _____ seconds |
| Maximum request body size | _____ MB |

---

## High Availability

### Multi-Region Deployment

- [ ] Yes - Active/Active across regions
- [ ] Yes - Active/Standby failover
- [ ] No - Single region

Regions required:

- [ ] North America
- [ ] Europe
- [ ] Asia-Pacific
- [ ] South America

### Origin Failover

Do you have multiple origin pools for failover?

- [ ] Yes - Automatic failover between pools
- [ ] No - Single origin pool

Failover configuration:

| Primary Pool | Secondary Pool | Failover Condition |
| --- | --- | --- |
| _____________ | _____________ | [ ] Health check [ ] Manual |

---

## Security Integration

### WAF Integration

Should WAF be enabled on this load balancer?

- [ ] Yes - Apply WAF policy
- [ ] No - Load balancing only

### Bot Defense Integration

Should Bot Defense be enabled?

- [ ] Yes - Apply bot defense
- [ ] No

### Service Policies

- [ ] IP allowlist/denylist
- [ ] Geo-blocking
- [ ] Rate limiting
- [ ] Custom rules

Number of service policy rules: _____

---

## Observability

### Logging Requirements

What logging do you need?

- [ ] Access logs (all requests)
- [ ] Security event logs
- [ ] Error logs only
- [ ] Custom log format

### Log Destinations

Where should logs be sent?

- [ ] F5 XC Console (default)
- [ ] External SIEM: _________________
- [ ] Cloud storage (S3, etc.): _________________

### Metrics and Monitoring

What metrics do you need?

- [ ] Request rate
- [ ] Response time / latency
- [ ] Error rates
- [ ] Origin health status
- [ ] Bandwidth utilization

---

## Summary: HTTP Load Balancer Requirements

| Requirement | Value |
| --- | --- |
| Number of Load Balancers | _____ |
| Total Applications | _____ |
| Estimated Peak RPS | _____ |
| TLS Certificate Management | [ ] Automatic [ ] Custom [ ] Mixed |
| WAF Integration | [ ] Yes [ ] No |
| Multi-Region | [ ] Yes [ ] No |
| Session Persistence | [ ] Yes [ ] No |

Additional notes or special requirements:

```text
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
