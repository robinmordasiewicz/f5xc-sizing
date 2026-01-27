# DNS Services Sizing

F5 Distributed Cloud DNS provides geo-distributed DNS services with global
server load balancing (GSLB), automatic failover, health checking, and DDoS
protection.

---

## DNS Requirements Assessment

- [ ] Yes - Primary DNS hosting
- [ ] Yes - Secondary DNS (backup)
- [ ] Yes - DNS Load Balancing (GSLB) only

### Current DNS Provider

Who is your current DNS provider?

| Current Provider | Keep or Migrate |
| --- | --- |
|  | [ ] Migrate to F5 [ ] Keep as primary [ ] Keep as secondary |

---

## DNS Zone Configuration

### Zone Count

How many DNS zones do you need?

| Zone Type | Count |
| --- | --- |
| Primary zones |  |
| Secondary zones |  |
| **Total zones** |  |

!!! note "Base Package"
    Standard includes 250 primary or secondary zones.

### Zone Details

List your primary domains/zones:

| Domain | Zone Type | Records (est.) | Query Volume |
| --- | --- | --- | --- |
|  | [ ] Primary [ ] Secondary |  | qps |
|  | [ ] Primary [ ] Secondary |  | qps |
|  | [ ] Primary [ ] Secondary |  | qps |
|  | [ ] Primary [ ] Secondary |  | qps |
|  | [ ] Primary [ ] Secondary |  | qps |

### Record Types

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
- [ ] Other:

Total estimated DNS records:

---

## DNS Load Balancing (GSLB)

- [ ] Yes - Distribute traffic across multiple locations
- [ ] No - Basic DNS hosting only

!!! note "Base Package"
    Standard includes 50 DNS load balancer records and 200 health checks.

### Load Balancing Use Cases

What DNS load balancing capabilities do you need?

- [ ] **Geographic proximity** - Route users to nearest data center
- [ ] **Active/Standby failover** - Automatic failover to backup site
- [ ] **Weighted distribution** - Distribute traffic by percentage
- [ ] **Performance-based** - Route based on health/latency
- [ ] **Disaster recovery** - Manual failover capability

### DNS Load Balancer Records

How many DNS load balancer records do you need?

| Record/Domain | Type | Locations |
| --- | --- | --- |
|  | [ ] Geo [ ] Failover [ ] Weighted |  |
|  | [ ] Geo [ ] Failover [ ] Weighted |  |
|  | [ ] Geo [ ] Failover [ ] Weighted |  |
|  | [ ] Geo [ ] Failover [ ] Weighted |  |

Total DNS LB records needed:

---

## Health Checking

### Health Check Requirements

- [ ] Yes
- [ ] No

Health check details:

| Target | Check Type | Interval |
| --- | --- | --- |
|  | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | sec |
|  | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | sec |
|  | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | sec |
|  | [ ] HTTP [ ] HTTPS [ ] TCP [ ] ICMP | sec |

Total health checks needed:

### Failover Configuration

| Parameter | Value |
| --- | --- |
| Health check interval | seconds |
| Failure threshold | consecutive failures |
| Recovery threshold | consecutive successes |
| TTL during failover | seconds |

---

## DNS Security

### DNSSEC

- [ ] Yes - Sign DNS responses cryptographically
- [ ] No

!!! info "DNSSEC"
    DNSSEC provides authentication of DNS responses, preventing DNS spoofing and
    cache poisoning attacks.

### DNS DDoS Protection

- [ ] Yes - Standard DNS DDoS protection (included)
- [ ] Yes - Advanced DNS DDoS protection
- [ ] No

Have you experienced DNS attacks?

- [ ] Yes - DNS floods
- [ ] Yes - DNS amplification
- [ ] Yes - NXDOMAIN attacks
- [ ] No

### Access Control

- [ ] TSIG authentication for zone transfers
- [ ] IP-based access restrictions
- [ ] Rate limiting per client

---

## Zone Management

### Zone Transfer

- [ ] Yes - F5 as primary, transfer to secondary
- [ ] Yes - External primary, F5 as secondary
- [ ] No

External DNS servers for zone transfer:

| Server | IP Address | Direction |
| --- | --- | --- |
|  |  | [ ] To F5 [ ] From F5 |
|  |  | [ ] To F5 [ ] From F5 |

### Zone Import

Do you have existing zone files to import?

- [ ] Yes - Standard zone file format
- [ ] Yes - BIND format
- [ ] No - Creating zones from scratch

Number of zone files to import:

### DNS Management Integration

How will DNS be managed?

- [ ] F5 XC Console (UI)
- [ ] Terraform / Infrastructure as Code
- [ ] API integration
- [ ] CI/CD pipeline

---

## Query Volume

### DNS Query Metrics

| Metric | Value |
| --- | --- |
| Average queries per second |  |
| Peak queries per second |  |
| Daily query volume |  |
| Monthly query volume |  |

### Query Sources

Where do DNS queries originate?

| Region | Percentage |
| --- | --- |
| North America | % |
| Europe | % |
| Asia-Pacific | % |
| South America | % |
| Other | % |

---

## Advanced Features

### Split-Horizon DNS

- [ ] Yes - Different responses for internal vs external
- [ ] No

### Dynamic DNS

- [ ] Yes - Programmatic record updates
- [ ] No

### GeoDNS Customization

- [ ] Yes - By country
- [ ] Yes - By region/continent
- [ ] Yes - By ASN (ISP)
- [ ] Yes - By client subnet
- [ ] No - Standard geo-proximity

---

## Domain Delegation

### Domain Registrar

Will you delegate domains to F5 nameservers?

- [ ] Yes - Update NS records at registrar
- [ ] No - Using F5 as secondary only

Current registrar:

### Nameserver Configuration

Nameserver preference:

- [ ] F5 provided nameservers
- [ ] Custom/vanity nameservers:

---

## Summary: DNS Requirements

| Requirement | Value |
| --- | --- |
| Total DNS Zones |  |
| Primary Zones |  |
| Secondary Zones |  |
| DNS LB Records |  |
| Health Checks |  |
| Estimated QPS |  |
| DNSSEC Required | [ ] Yes [ ] No |
| Tier Required | [ ] Standard [ ] Advanced |

Domains to migrate:

```text
1.
2.
3.
```

Additional notes:

```text


```
