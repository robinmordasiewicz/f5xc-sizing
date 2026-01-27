# DDoS Protection Sizing

F5 Distributed Cloud DDoS Mitigation provides multi-terabit protection against
L3/L4 volumetric attacks and L7 application-layer attacks with always-on or
on-demand deployment options.

---

## DDoS Requirements Assessment

### DDoS Attack History

Have you experienced DDoS attacks in the past?

- [ ] Yes - Frequent attacks (monthly or more)
- [ ] Yes - Occasional attacks (quarterly)
- [ ] Yes - Rare attacks (annually or less)
- [ ] No - But we want proactive protection
- [ ] Unknown

If yes, describe recent attacks:

| Date | Attack Type | Peak Size | Duration | Impact |
| --- | --- | --- | --- | --- |
| ___ | ___ | ___ Gbps | ___ min | ___ |
| ___ | ___ | ___ Gbps | ___ min | ___ |
| ___ | ___ | ___ Gbps | ___ min | ___ |

---

## Network Infrastructure

### Customer ASN

Does your company have an Autonomous System Number (ASN) assigned by an Internet
Authority?

- [ ] **YES** - ASN: ___
- [ ] **NO**

!!! warning "No ASN"
    If you do not have an Autonomous System Number, please inform your F5 Sales
    Specialist immediately as this affects BGP-based DDoS mitigation options.

### BGP Network Prefix

Have you been assigned a network prefix by your ISP or Internet authority to
announce via BGP using your ASN?

- [ ] **YES**
- [ ] **NO**

!!! note "Prefix Size Requirements"
    The network prefix size must be a /24 or shorter (/23, /22, /21, etc.). If
    you do not have a network prefix assigned and under control of your ASN, please
    inform your F5 Sales Specialist immediately.

If yes, list your network prefixes:

| Prefix (CIDR) | Size | Announced via BGP? |
| --- | --- | --- |
| ___ | /___ | ( ) Yes ( ) No |
| ___ | /___ | ( ) Yes ( ) No |
| ___ | /___ | ( ) Yes ( ) No |
| ___ | /___ | ( ) Yes ( ) No |

Total number of prefixes: ___

---

## Data Center Infrastructure

### Data Centers

How many data centers do you need to protect from DDoS attacks?

| Data Center Location | Provider | Router Count |
| --- | --- | --- |
| ___ | ( ) On-Prem ( ) Colo ( ) Cloud | ___ |
| ___ | ( ) On-Prem ( ) Colo ( ) Cloud | ___ |
| ___ | ( ) On-Prem ( ) Colo ( ) Cloud | ___ |
| ___ | ( ) On-Prem ( ) Colo ( ) Cloud | ___ |

**Total Data Centers:** ___

### Edge Routers

How many EDGE/CORE/BORDER routers do you want F5 to monitor for DDoS attack
detection?

| Router Location | Router Type | Vendor/Model |
| --- | --- | --- |
| ___ | ( ) Edge ( ) Core ( ) Border | ___ |
| ___ | ( ) Edge ( ) Core ( ) Border | ___ |
| ___ | ( ) Edge ( ) Core ( ) Border | ___ |
| ___ | ( ) Edge ( ) Core ( ) Border | ___ |

**Total Edge Routers:** ___

---

## Bandwidth Requirements

### Clean Bandwidth

Please provide the amount of **CLEAN BANDWIDTH** utilized by the network
prefixes you would like to protect:

| Metric | Value |
| --- | --- |
| 95th Percentile Inbound Bandwidth | ___ Mbps |
| Peak Inbound Bandwidth | ___ Mbps |
| Average Inbound Bandwidth | ___ Mbps |

!!! note "Measurement"
    The bandwidth measurement should be provided in Mbps, calculated using 95th
    percentile usage, for **INBOUND TRAFFIC ONLY**.

### Current Internet Connectivity

What is your total internet connectivity capacity?

| Metric | Value |
| --- | --- |
| Total uplink capacity | ___ Gbps |
| Number of ISP connections | ___ |
| ISP providers | ___ |

---

## Protection Mode

### Mode of Protection

Please select your preferred protection mode:

- [ ] **CONTINUOUS (Always On)**
  - All traffic routed through F5 at all times
  - Zero detection/mitigation delay
  - Best for high-value, frequently-targeted assets

- [ ] **ON-DEMAND (Always Available)**
  - Traffic routes normally until attack detected
  - Mitigation activates upon detection
  - Cost-effective for less frequently attacked assets

### Activation Method (On-Demand Only)

If On-Demand, how should mitigation be activated?

- [ ] Automatic (F5 detects attack and activates)
- [ ] Manual (Customer initiates activation)
- [ ] Hybrid (Auto-detect with manual confirmation)

Acceptable time to mitigate after detection: ___ minutes

---

## Attack Types

### L3/L4 Volumetric Attacks

Attack types to protect against:

- [ ] UDP Floods
- [ ] TCP SYN Floods
- [ ] TCP ACK Floods
- [ ] ICMP Floods
- [ ] DNS Amplification
- [ ] NTP Amplification
- [ ] SSDP Amplification
- [ ] Memcached Amplification
- [ ] Fragmentation Attacks
- [ ] Teardrop Attacks
- [ ] Smurf Attacks

### L7 Application-Layer Attacks

- [ ] Yes - Requires Advanced tier or WAF
- [ ] No

Attack types to protect against:

- [ ] HTTP Floods
- [ ] Slowloris
- [ ] Slow POST
- [ ] DNS Query Floods
- [ ] SSL/TLS Exhaustion
- [ ] API Abuse
- [ ] Login Page Attacks

!!! warning "L7 DDoS"
    Layer 7 DDoS mitigation with ML-based anomaly detection requires the
    Advanced WAAP tier.

---

## Detection and Alerting

### Detection Requirements

How should DDoS attacks be detected?

- [ ] Traffic analysis on edge routers (NetFlow/sFlow)
- [ ] Inline detection (Always On mode)
- [ ] External monitoring integration

### Alerting Requirements

How do you want to be notified of attacks?

- [ ] Email alerts
- [ ] SMS/Text alerts
- [ ] Phone call (24x7 SOC)
- [ ] Webhook/API integration
- [ ] SIEM integration

Alert contacts:

| Name | Role | Email | Phone |
| --- | --- | --- | --- |
| ___ | Primary | ___ | ___ |
| ___ | Secondary | ___ | ___ |
| ___ | Escalation | ___ | ___ |

### Reporting Requirements

What DDoS reporting do you need?

- [ ] Real-time attack dashboard
- [ ] Post-attack reports
- [ ] Monthly summary reports
- [ ] Custom reporting

---

## Integration Requirements

### BGP Integration

Will you establish BGP sessions with F5 for traffic diversion?

- [ ] Yes - Direct BGP peering
- [ ] Yes - Through IX (Internet Exchange)
- [ ] No - DNS-based diversion only

BGP session details (if applicable):

| Peer Location | Your Router IP | F5 Peer IP |
| --- | --- | --- |
| ___ | ___ | TBD |
| ___ | ___ | TBD |

### GRE Tunnel Requirements

- [ ] Yes - GRE tunnels to our routers
- [ ] No - Direct routing

Number of GRE tunnel endpoints: ___

### Existing DDoS Solutions

Do you have existing DDoS protection?

| Solution | Provider | Replace or Layer? |
| --- | --- | --- |
| ___ | ___ | ( ) Replace ( ) Layer |

---

## Service Level Requirements

### SLA Requirements

What SLA requirements do you have?

| Metric | Requirement |
| --- | --- |
| Time to Detect | < ___ minutes |
| Time to Mitigate | < ___ minutes |
| Uptime SLA | ___ % |
| False Positive Rate | < ___ % |

### Support Level

What level of DDoS support do you need?

- [ ] **Standard** - Business hours support
- [ ] **Enhanced** - 24x7 SOC monitoring
- [ ] **Enhanced Plus** - Dedicated SOC resources

---

## Summary: DDoS Protection Requirements

| Requirement | Value |
| --- | --- |
| Customer ASN | ( ) Yes ( ) No |
| Number of Prefixes | ___ |
| Number of Data Centers | ___ |
| Number of Edge Routers | ___ |
| Clean Bandwidth (95th percentile) | ___ Mbps |
| Protection Mode | ( ) Always On ( ) On-Demand |
| L3/L4 Protection | ( ) Yes ( ) No |
| L7 Protection | ( ) Yes ( ) No |
| Support Level | ( ) Standard ( ) Enhanced ( ) Enhanced Plus |

Network diagram attached: [ ] Yes [ ] No

Additional notes or special requirements:

```text
___
```
