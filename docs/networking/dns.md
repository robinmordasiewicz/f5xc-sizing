# DNS Services Sizing

F5 Distributed Cloud DNS provides geo-distributed DNS services with global server load balancing (GSLB), automatic failover, health checking, and DDoS protection.

---

## Section 1: DNS Requirements Assessment

### 1.1 Do You Need F5 DNS Services?

- [ ] Yes - Primary DNS hosting
- [ ] Yes - Secondary DNS (backup)
- [ ] Yes - DNS Load Balancing (GSLB) only
- [ ] No - Skip this section

### 1.2 Current DNS Provider

Who is your current DNS provider?

| Current Provider | Keep or Migrate |
|-----------------|-----------------|
| _____________ | [ ] Migrate to F5 [ ] Keep as primary [ ] Keep as secondary |

---

## Section 2: DNS Zone Configuration

### 2.1 Zone Count

How many DNS zones do you need?

| Zone Type | Count |
|-----------|-------|
| Primary zones | _____ |
| Secondary zones | _____ |
| **Total zones** | _____ |

!!! note "Base Package"
    Standard includes 250 primary or secondary zones.

### 2.2 Zone Details

List your primary domains/zones:

| Domain | Zone Type | Records (est.) | Query Volume |
|--------|-----------|---------------|--------------|
| _____________ | [ ] Primary [ ] Secondary | _____ | _____ qps |
| _____________ | [ ] Primary [ ] Secondary | _____ | _____ qps |
| _____________ | [ ] Primary [ ] Secondary | _____ | _____ qps |
| _____________ | [ ] Primary [ ] Secondary | _____ | _____ qps |
| _____________ | [ ] Primary [ ] Secondary | _____ | _____ qps |

### 2.3 Record Types

What DNS record types do you use?

- [ ] A (IPv4 address)
- [ ] AAAA (IPv6 address)
- [ ] CNAME (Canonical name)
- [ ] MX (Mail exchange)
- [ ] TXT (Text records)
- [ ] SRV (Service records)
- [ ] NS (Nameserver)
- [ ] CAA (Certificate Authority Authorization)
- [ ] PTR (Reverse DNS)
- [ ] Other: _________________

Total estimated DNS records: _____

---

## Section 3: DNS Load Balancing (GSLB)

### 3.1 Do You Need DNS Load Balancing?

- [ ] Yes - Distribute traffic across multiple locations
- [ ] No - Basic DNS hosting only

!!! note "Base Package"
    Standard includes 50 DNS load balancer records and 200 health checks.

### 3.2 Load Balancing Use Cases

What DNS load balancing capabilities do you need?

- [ ] **Geographic proximity** - Route users to nearest data center
- [ ] **Active/Standby failover** - Automatic failover to backup site
- [ ] **Weighted distribution** - Distribute traffic by percentage
- [ ] **Performance-based** - Route based on health/latency
- [ ] **Disaster recovery** - Manual failover capability

### 3.3 DNS Load Balancer Records

How many DNS load balancer records do you need?

| Record/Domain | Type | Locations |
|--------------|------|-----------|
| _____________ | [ ] Geo [ ] Failover [ ] Weighted | _____ |
| _____________ | [ ] Geo [ ] Failover [ ] Weighted | _____ |
| _____________ | [ ] Geo [ ] Failover [ ] Weighted | _____ |
| _____________ | [ ] Geo [ ] Failover [ ] Weighted | _____ |

Total DNS LB records needed: _____

---

## Section 4: Health Checking

### 4.1 Health Check Requirements

Do you need health checks for DNS failover?

- [ ] Yes
- [ ] No

Health check details:

| Target | Check Type | Interval |
|--------|------------|----------|
| _____________ | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | _____ sec |
| _____________ | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | _____ sec |
| _____________ | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | _____ sec |
| _____________ | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | _____ sec |

Total health checks needed: _____

### 4.2 Failover Configuration

| Parameter | Value |
|-----------|-------|
| Health check interval | _____ seconds |
| Failure threshold | _____ consecutive failures |
| Recovery threshold | _____ consecutive successes |
| TTL during failover | _____ seconds |

---

## Section 5: DNS Security

### 5.1 DNSSEC

Do you need DNSSEC (DNS Security Extensions)?

- [ ] Yes - Sign DNS responses cryptographically
- [ ] No

!!! info "DNSSEC"
    DNSSEC provides authentication of DNS responses, preventing DNS spoofing and cache poisoning attacks.

### 5.2 DNS DDoS Protection

Do you need DNS-specific DDoS protection?

- [ ] Yes - Standard DNS DDoS protection (included)
- [ ] Yes - Advanced DNS DDoS protection
- [ ] No

Have you experienced DNS attacks?

- [ ] Yes - DNS floods
- [ ] Yes - DNS amplification
- [ ] Yes - NXDOMAIN attacks
- [ ] No

### 5.3 Access Control

Do you need DNS access control?

- [ ] TSIG authentication for zone transfers
- [ ] IP-based access restrictions
- [ ] Rate limiting per client

---

## Section 6: Zone Management

### 6.1 Zone Transfer

Do you need zone transfers?

- [ ] Yes - F5 as primary, transfer to secondary
- [ ] Yes - External primary, F5 as secondary
- [ ] No

External DNS servers for zone transfer:

| Server | IP Address | Direction |
|--------|-----------|-----------|
| _____________ | _____________ | [ ] To F5 [ ] From F5 |
| _____________ | _____________ | [ ] To F5 [ ] From F5 |

### 6.2 Zone Import

Do you have existing zone files to import?

- [ ] Yes - Standard zone file format
- [ ] Yes - BIND format
- [ ] No - Creating zones from scratch

Number of zone files to import: _____

### 6.3 DNS Management Integration

How will DNS be managed?

- [ ] F5 XC Console (UI)
- [ ] Terraform / Infrastructure as Code
- [ ] API integration
- [ ] CI/CD pipeline

---

## Section 7: Query Volume

### 7.1 DNS Query Metrics

| Metric | Value |
|--------|-------|
| Average queries per second | _____ |
| Peak queries per second | _____ |
| Daily query volume | _____ |
| Monthly query volume | _____ |

### 7.2 Query Sources

Where do DNS queries originate?

| Region | Percentage |
|--------|------------|
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Other | _____% |

---

## Section 8: Advanced Features

### 8.1 Split-Horizon DNS

Do you need split-horizon (split-brain) DNS?

- [ ] Yes - Different responses for internal vs external
- [ ] No

### 8.2 Dynamic DNS

Do you need dynamic DNS updates?

- [ ] Yes - Programmatic record updates
- [ ] No

### 8.3 GeoDNS Customization

Do you need custom geographic routing rules?

- [ ] Yes - By country
- [ ] Yes - By region/continent
- [ ] Yes - By ASN (ISP)
- [ ] Yes - By client subnet
- [ ] No - Standard geo-proximity

---

## Section 9: Domain Delegation

### 9.1 Domain Registrar

Will you delegate domains to F5 nameservers?

- [ ] Yes - Update NS records at registrar
- [ ] No - Using F5 as secondary only

Current registrar: _________________

### 9.2 Nameserver Configuration

Nameserver preference:

- [ ] F5 provided nameservers
- [ ] Custom/vanity nameservers: _________________

---

## Summary: DNS Requirements

| Requirement | Value |
|-------------|-------|
| Total DNS Zones | _____ |
| Primary Zones | _____ |
| Secondary Zones | _____ |
| DNS LB Records | _____ |
| Health Checks | _____ |
| Estimated QPS | _____ |
| DNSSEC Required | [ ] Yes [ ] No |
| Tier Required | [ ] Standard [ ] Advanced |

Domains to migrate:

```
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________
```

Additional notes:

```
_____________________________________________________________
_____________________________________________________________
```
