# DDoS Protection Sizing

F5 Distributed Cloud DDoS Mitigation provides multi-terabit protection against L3/L4 volumetric attacks and L7 application-layer attacks with always-on or on-demand deployment options.

---

## Section 1: DDoS Requirements Assessment

### 1.1 Do You Need DDoS Protection?

- [ ] Yes - We need DDoS protection
- [ ] No - Skip this section

### 1.2 DDoS Attack History

Have you experienced DDoS attacks in the past?

- [ ] Yes - Frequent attacks (monthly or more)
- [ ] Yes - Occasional attacks (quarterly)
- [ ] Yes - Rare attacks (annually or less)
- [ ] No - But we want proactive protection
- [ ] Unknown

If yes, describe recent attacks:

| Date | Attack Type | Peak Size | Duration | Impact |
|------|-------------|-----------|----------|--------|
| _____ | _____________ | _____ Gbps | _____ min | _____________ |
| _____ | _____________ | _____ Gbps | _____ min | _____________ |
| _____ | _____________ | _____ Gbps | _____ min | _____________ |

---

## Section 2: Network Infrastructure

### 2.1 Customer ASN

!!! question "What is an ASN?"
    An Autonomous System Number (ASN) is a unique identifier assigned by an Internet authority that identifies a collection of IP networks under a single administrative domain.

Does your company have an Autonomous System Number (ASN) assigned by an Internet Authority?

- [ ] **YES** - ASN: _________________
- [ ] **NO**

!!! warning "No ASN"
    If you do not have an Autonomous System Number, please inform your F5 Sales Specialist immediately as this affects BGP-based DDoS mitigation options.

### 2.2 BGP Network Prefix

!!! question "What is a Network Prefix?"
    A network prefix is a range of network addresses (e.g., 192.0.2.0/24) assigned by your ISP or Internet authority that you can announce via BGP.

Have you been assigned a network prefix by your ISP or Internet authority to announce via BGP using your ASN?

- [ ] **YES**
- [ ] **NO**

!!! note "Prefix Size Requirements"
    The network prefix size must be a /24 or shorter (/23, /22, /21, etc.). If you do not have a network prefix assigned and under control of your ASN, please inform your F5 Sales Specialist immediately.

If yes, list your network prefixes:

| Prefix (CIDR) | Size | Announced via BGP? |
|---------------|------|-------------------|
| _____/___ | /___  | [ ] Yes [ ] No |
| _____/___ | /___  | [ ] Yes [ ] No |
| _____/___ | /___  | [ ] Yes [ ] No |
| _____/___ | /___  | [ ] Yes [ ] No |

Total number of prefixes: _____

---

## Section 3: Data Center Infrastructure

### 3.1 Data Centers

!!! question "What is a Data Center?"
    For DDoS protection sizing, F5 XC quantifies a data center as a physical or virtual hosting location with a minimum of one to two routers.

How many data centers do you need to protect from DDoS attacks?

| Data Center Location | Provider | Router Count |
|---------------------|----------|--------------|
| _____________ | [ ] On-Prem [ ] Colo [ ] Cloud | _____ |
| _____________ | [ ] On-Prem [ ] Colo [ ] Cloud | _____ |
| _____________ | [ ] On-Prem [ ] Colo [ ] Cloud | _____ |
| _____________ | [ ] On-Prem [ ] Colo [ ] Cloud | _____ |

**Total Data Centers:** _____

### 3.2 Edge Routers

!!! question "What is an Edge Router?"
    Edge/Core/Border routers are the routers at the edge of your network that F5 will monitor for DDoS attack detection.

How many EDGE/CORE/BORDER routers do you want F5 to monitor for DDoS attack detection?

| Router Location | Router Type | Vendor/Model |
|-----------------|-------------|--------------|
| _____________ | [ ] Edge [ ] Core [ ] Border | _____________ |
| _____________ | [ ] Edge [ ] Core [ ] Border | _____________ |
| _____________ | [ ] Edge [ ] Core [ ] Border | _____________ |
| _____________ | [ ] Edge [ ] Core [ ] Border | _____________ |

**Total Edge Routers:** _____

---

## Section 4: Bandwidth Requirements

### 4.1 Clean Bandwidth

!!! question "What is Clean Bandwidth?"
    Clean bandwidth is the amount of legitimate traffic (after DDoS mitigation) that flows to your network prefixes. Measured using 95th percentile for INBOUND TRAFFIC ONLY.

Please provide the amount of **CLEAN BANDWIDTH** utilized by the network prefixes you would like to protect:

| Metric | Value |
|--------|-------|
| 95th Percentile Inbound Bandwidth | _____ Mbps |
| Peak Inbound Bandwidth | _____ Mbps |
| Average Inbound Bandwidth | _____ Mbps |

!!! note "Measurement"
    The bandwidth measurement should be provided in Mbps, calculated using 95th percentile usage, for **INBOUND TRAFFIC ONLY**.

### 4.2 Current Internet Connectivity

What is your total internet connectivity capacity?

| Metric | Value |
|--------|-------|
| Total uplink capacity | _____ Gbps |
| Number of ISP connections | _____ |
| ISP providers | _____________ |

---

## Section 5: Protection Mode

### 5.1 Mode of Protection

!!! question "Protection Modes"
    - **ALWAYS ON (Continuous)**: All traffic continuously routes through F5 scrubbing infrastructure. Immediate protection with no detection delay.
    - **ALWAYS AVAILABLE (On-Demand)**: Protection activates when attacks are detected. Traffic diverts to F5 scrubbing during attacks.

Please select your preferred protection mode:

- [ ] **CONTINUOUS (Always On)**
    - All traffic routed through F5 at all times
    - Zero detection/mitigation delay
    - Best for high-value, frequently-targeted assets

- [ ] **ON-DEMAND (Always Available)**
    - Traffic routes normally until attack detected
    - Mitigation activates upon detection
    - Cost-effective for less frequently attacked assets

### 5.2 Activation Method (On-Demand Only)

If On-Demand, how should mitigation be activated?

- [ ] Automatic (F5 detects attack and activates)
- [ ] Manual (Customer initiates activation)
- [ ] Hybrid (Auto-detect with manual confirmation)

Acceptable time to mitigate after detection: _____ minutes

---

## Section 6: Attack Types

### 6.1 L3/L4 Volumetric Attacks

Do you need protection against network-layer volumetric attacks?

- [ ] Yes - Included in base package
- [ ] No

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

### 6.2 L7 Application-Layer Attacks

Do you need protection against application-layer DDoS?

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
    Layer 7 DDoS mitigation with ML-based anomaly detection requires the Advanced WAAP tier.

---

## Section 7: Detection and Alerting

### 7.1 Detection Requirements

How should DDoS attacks be detected?

- [ ] Traffic analysis on edge routers (NetFlow/sFlow)
- [ ] Inline detection (Always On mode)
- [ ] External monitoring integration

### 7.2 Alerting Requirements

How do you want to be notified of attacks?

- [ ] Email alerts
- [ ] SMS/Text alerts
- [ ] Phone call (24x7 SOC)
- [ ] Webhook/API integration
- [ ] SIEM integration

Alert contacts:

| Name | Role | Email | Phone |
|------|------|-------|-------|
| _____________ | Primary | _____________ | _____________ |
| _____________ | Secondary | _____________ | _____________ |
| _____________ | Escalation | _____________ | _____________ |

### 7.3 Reporting Requirements

What DDoS reporting do you need?

- [ ] Real-time attack dashboard
- [ ] Post-attack reports
- [ ] Monthly summary reports
- [ ] Custom reporting

---

## Section 8: Integration Requirements

### 8.1 BGP Integration

Will you establish BGP sessions with F5 for traffic diversion?

- [ ] Yes - Direct BGP peering
- [ ] Yes - Through IX (Internet Exchange)
- [ ] No - DNS-based diversion only

BGP session details (if applicable):

| Peer Location | Your Router IP | F5 Peer IP |
|--------------|----------------|------------|
| _____________ | _____________ | TBD |
| _____________ | _____________ | TBD |

### 8.2 GRE Tunnel Requirements

Do you need GRE tunnels for clean traffic return?

- [ ] Yes - GRE tunnels to our routers
- [ ] No - Direct routing

Number of GRE tunnel endpoints: _____

### 8.3 Existing DDoS Solutions

Do you have existing DDoS protection?

| Solution | Provider | Replace or Layer? |
|----------|----------|-------------------|
| _____________ | _____________ | [ ] Replace [ ] Layer |

---

## Section 9: Service Level Requirements

### 9.1 SLA Requirements

What SLA requirements do you have?

| Metric | Requirement |
|--------|-------------|
| Time to Detect | < _____ minutes |
| Time to Mitigate | < _____ minutes |
| Uptime SLA | _____% |
| False Positive Rate | < _____% |

### 9.2 Support Level

What level of DDoS support do you need?

- [ ] **Standard** - Business hours support
- [ ] **Enhanced** - 24x7 SOC monitoring
- [ ] **Enhanced Plus** - Dedicated SOC resources

---

## Summary: DDoS Protection Requirements

| Requirement | Value |
|-------------|-------|
| Customer ASN | [ ] Yes: _______ [ ] No |
| Number of Prefixes | _____ |
| Number of Data Centers | _____ |
| Number of Edge Routers | _____ |
| Clean Bandwidth (95th percentile) | _____ Mbps |
| Protection Mode | [ ] Always On [ ] On-Demand |
| L3/L4 Protection | [ ] Yes [ ] No |
| L7 Protection | [ ] Yes [ ] No |
| Support Level | [ ] Standard [ ] Enhanced [ ] Enhanced Plus |

Network diagram attached: [ ] Yes [ ] No

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
