# HTTP Load Balancer Sizing

F5 Distributed Cloud HTTP Load Balancer provides global application delivery with intelligent routing, health checks, TLS termination, and integration with security services.

---

## Section 1: Load Balancer Requirements

### 1.1 Application Inventory

How many HTTP/HTTPS applications need load balancing?

| Environment | Application Count |
|-------------|------------------|
| Production | _____ |
| Staging/QA | _____ |
| Development | _____ |
| **Total** | _____ |

### 1.2 Virtual Host Details

For each application, provide virtual host information:

| Application Name | Domain(s) | Port(s) | Protocol |
|-----------------|-----------|---------|----------|
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |
| _____________ | _____________ | [ ] 80 [ ] 443 [ ] Other: ___ | [ ] HTTP [ ] HTTPS [ ] Both |

!!! note "Base Package"
    The base package includes 1 load balancer. Additional load balancers are available as add-ons.

---

## Section 2: Traffic Volume

### 2.1 Request Metrics

| Metric | Average | Peak |
|--------|---------|------|
| Requests per second | _____ | _____ |
| Concurrent connections | _____ | _____ |
| Bandwidth (Mbps) | _____ | _____ |

### 2.2 Traffic Patterns

What are your traffic patterns?

- [ ] Steady throughout the day
- [ ] Business hours peaks
- [ ] Seasonal peaks (specify): _________________
- [ ] Event-driven spikes
- [ ] Unpredictable

Geographic distribution of users:

| Region | Traffic Percentage |
|--------|-------------------|
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Other | _____% |

---

## Section 3: Origin Pool Configuration

### 3.1 Origin Server Details

For each application, describe origin servers:

| Application | Origin Type | Count | Location |
|-------------|-------------|-------|----------|
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |
| _____________ | [ ] IP [ ] FQDN [ ] K8s Service | _____ | _____________ |

### 3.2 Origin Connectivity

How will F5 XC reach your origin servers?

- [ ] **Public Internet** - Origins have public IP addresses
- [ ] **Customer Edge** - Via F5 CE deployed in your environment
- [ ] **Cloud Site** - Via F5 site in AWS/Azure/GCP
- [ ] **Private Link** - Direct cloud connectivity

### 3.3 Origin Protocol

What protocol to use when connecting to origins?

| Application | Origin Protocol | Origin Port |
|-------------|-----------------|-------------|
| _____________ | [ ] HTTP [ ] HTTPS | _____ |
| _____________ | [ ] HTTP [ ] HTTPS | _____ |
| _____________ | [ ] HTTP [ ] HTTPS | _____ |

---

## Section 4: Load Balancing Configuration

### 4.1 Load Balancing Algorithm

Preferred load balancing algorithm:

- [ ] **Round Robin** - Distribute evenly across origins
- [ ] **Least Connections** - Send to origin with fewest active connections
- [ ] **Random** - Random selection
- [ ] **Source IP Hash** - Consistent routing based on client IP
- [ ] **Ring Hash** - Consistent hashing for cache efficiency

### 4.2 Session Persistence

Do you need session persistence (sticky sessions)?

- [ ] Yes - Source IP based
- [ ] Yes - Cookie based
- [ ] Yes - Header based
- [ ] No - Stateless application

Persistence timeout: _____ seconds

### 4.3 Health Checks

Health check requirements:

| Parameter | Value |
|-----------|-------|
| Health check type | [ ] HTTP [ ] HTTPS [ ] TCP |
| Check interval | _____ seconds |
| Check path (HTTP) | _____________ |
| Expected response code | [ ] 200 [ ] 2xx [ ] Custom: ___ |
| Healthy threshold | _____ consecutive checks |
| Unhealthy threshold | _____ consecutive checks |

---

## Section 5: TLS Configuration

### 5.1 TLS Termination

Where should TLS be terminated?

- [ ] **At F5 XC** - F5 terminates TLS, connects to origin over HTTP/HTTPS
- [ ] **End-to-End** - F5 terminates and re-encrypts to origin
- [ ] **Pass-Through** - TLS passes through to origin (TCP LB only)

### 5.2 Certificate Management

How will TLS certificates be managed?

- [ ] **Automatic** - F5 XC provisions via Let's Encrypt
- [ ] **Custom** - We provide our own certificates
- [ ] **Mixed** - Different per application

Custom certificate details:

| Domain | Certificate Type | Key Type |
|--------|-----------------|----------|
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | [ ] RSA 2048 [ ] RSA 4096 [ ] ECC |
| _____________ | [ ] Single [ ] Wildcard [ ] SAN | [ ] RSA 2048 [ ] RSA 4096 [ ] ECC |

### 5.3 TLS Requirements

| Requirement | Value |
|-------------|-------|
| Minimum TLS version | [ ] TLS 1.2 [ ] TLS 1.3 |
| Cipher suite preference | [ ] Default [ ] Custom |
| HSTS enabled | [ ] Yes [ ] No |
| HTTP to HTTPS redirect | [ ] Yes [ ] No |

### 5.4 Mutual TLS (mTLS)

Do you require mTLS client authentication?

- [ ] Yes - Clients must present certificates
- [ ] No

If yes:
- Client CA certificate source: _________________
- XFCC header forwarding needed: [ ] Yes [ ] No

---

## Section 6: Traffic Management

### 6.1 Routing Rules

Do you need advanced routing?

- [ ] **Path-based routing** - Route based on URL path
- [ ] **Header-based routing** - Route based on HTTP headers
- [ ] **Query parameter routing** - Route based on query strings
- [ ] **Method-based routing** - Route based on HTTP method

Example routing requirements:

| Condition | Destination |
|-----------|-------------|
| Path: /api/* | API origin pool |
| Header: X-Version: v2 | V2 origin pool |
| _____________ | _____________ |

### 6.2 Traffic Policies

Do you need traffic manipulation?

- [ ] Request header insertion/modification
- [ ] Response header insertion/modification
- [ ] URL rewriting
- [ ] Request body buffering
- [ ] Response compression

### 6.3 Timeouts and Limits

| Parameter | Value |
|-----------|-------|
| Request timeout | _____ seconds |
| Idle timeout | _____ seconds |
| Maximum request body size | _____ MB |

---

## Section 7: High Availability

### 7.1 Multi-Region Deployment

Do you need load balancers in multiple regions?

- [ ] Yes - Active/Active across regions
- [ ] Yes - Active/Standby failover
- [ ] No - Single region

Regions required:

- [ ] North America
- [ ] Europe
- [ ] Asia-Pacific
- [ ] South America

### 7.2 Origin Failover

Do you have multiple origin pools for failover?

- [ ] Yes - Automatic failover between pools
- [ ] No - Single origin pool

Failover configuration:

| Primary Pool | Secondary Pool | Failover Condition |
|--------------|----------------|-------------------|
| _____________ | _____________ | [ ] Health check [ ] Manual |

---

## Section 8: Security Integration

### 8.1 WAF Integration

Should WAF be enabled on this load balancer?

- [ ] Yes - Apply WAF policy
- [ ] No - Load balancing only

### 8.2 Bot Defense Integration

Should Bot Defense be enabled?

- [ ] Yes - Apply bot defense
- [ ] No

### 8.3 Service Policies

Do you need service policies on this load balancer?

- [ ] IP allowlist/denylist
- [ ] Geo-blocking
- [ ] Rate limiting
- [ ] Custom rules

Number of service policy rules: _____

---

## Section 9: Observability

### 9.1 Logging Requirements

What logging do you need?

- [ ] Access logs (all requests)
- [ ] Security event logs
- [ ] Error logs only
- [ ] Custom log format

### 9.2 Log Destinations

Where should logs be sent?

- [ ] F5 XC Console (default)
- [ ] External SIEM: _________________
- [ ] Cloud storage (S3, etc.): _________________

### 9.3 Metrics and Monitoring

What metrics do you need?

- [ ] Request rate
- [ ] Response time / latency
- [ ] Error rates
- [ ] Origin health status
- [ ] Bandwidth utilization

---

## Summary: HTTP Load Balancer Requirements

| Requirement | Value |
|-------------|-------|
| Number of Load Balancers | _____ |
| Total Applications | _____ |
| Estimated Peak RPS | _____ |
| TLS Certificate Management | [ ] Automatic [ ] Custom [ ] Mixed |
| WAF Integration | [ ] Yes [ ] No |
| Multi-Region | [ ] Yes [ ] No |
| Session Persistence | [ ] Yes [ ] No |

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
