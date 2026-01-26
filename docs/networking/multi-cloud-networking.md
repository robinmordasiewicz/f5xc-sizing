# Multi-Cloud Networking Sizing

F5 Distributed Cloud Network Connect provides secure, encrypted connectivity between public clouds, on-premises data centers, and edge sites with centralized management and observability.

---

## Section 1: Multi-Cloud Networking Requirements

### 1.1 Do You Need Multi-Cloud Networking?

- [ ] Yes - Connect multiple cloud environments
- [ ] Yes - Connect cloud to on-premises
- [ ] Yes - Connect distributed edge sites
- [ ] No - Skip this section

### 1.2 Current Multi-Cloud Challenges

What networking challenges are you experiencing?

- [ ] Complex cloud-specific networking configurations
- [ ] Inconsistent security policies across clouds
- [ ] Limited visibility across environments
- [ ] High latency between sites
- [ ] Difficult troubleshooting
- [ ] Manual configuration overhead
- [ ] Other: _________________

---

## Section 2: Site Inventory

### 2.1 Cloud Environments

What cloud environments need connectivity?

| Cloud Provider | Regions | VPCs/VNets | Workloads |
|---------------|---------|------------|-----------|
| AWS | _____ | _____ | _____________ |
| Azure | _____ | _____ | _____________ |
| Google Cloud | _____ | _____ | _____________ |
| Other: _______ | _____ | _____ | _____________ |

### 2.2 On-Premises Data Centers

| Data Center Location | Network Connectivity | Workloads |
|---------------------|---------------------|-----------|
| _____________ | [ ] Internet [ ] MPLS [ ] Direct Connect | _____________ |
| _____________ | [ ] Internet [ ] MPLS [ ] Direct Connect | _____________ |
| _____________ | [ ] Internet [ ] MPLS [ ] Direct Connect | _____________ |

### 2.3 Edge/Branch Sites

| Site Type | Count | Connectivity |
|-----------|-------|--------------|
| Branch offices | _____ | [ ] Internet [ ] MPLS |
| Retail locations | _____ | [ ] Internet [ ] MPLS |
| Manufacturing sites | _____ | [ ] Internet [ ] MPLS |
| Remote workers | _____ | [ ] Internet [ ] VPN |
| Other: _______ | _____ | _____________ |

**Total sites to connect:** _____

---

## Section 3: Connectivity Requirements

### 3.1 Site-to-Site Connectivity

What site-to-site connectivity patterns do you need?

- [ ] **Full Mesh** - Every site connects to every other site
- [ ] **Hub and Spoke** - Sites connect through central hubs
- [ ] **Partial Mesh** - Specific site-to-site connections

Diagram your connectivity requirements:

```
[Draw or describe your target topology]
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

### 3.2 Traffic Patterns

What traffic flows between sites?

| Source | Destination | Traffic Type | Bandwidth |
|--------|-------------|--------------|-----------|
| _____________ | _____________ | _____________ | _____ Mbps |
| _____________ | _____________ | _____________ | _____ Mbps |
| _____________ | _____________ | _____________ | _____ Mbps |
| _____________ | _____________ | _____________ | _____ Mbps |

### 3.3 Bandwidth Requirements

| Metric | Value |
|--------|-------|
| Total inter-site bandwidth | _____ Mbps |
| Peak inter-site bandwidth | _____ Mbps |
| Average latency requirement | < _____ ms |

---

## Section 4: Customer Edge Deployment

### 4.1 CE Site Deployment

Where will F5 Customer Edge (CE) nodes be deployed?

| Site | Deployment Type | Node Count | Size |
|------|-----------------|------------|------|
| _____________ | [ ] Physical [ ] VM [ ] Cloud | _____ | [ ] Small [ ] Medium [ ] Large |
| _____________ | [ ] Physical [ ] VM [ ] Cloud | _____ | [ ] Small [ ] Medium [ ] Large |
| _____________ | [ ] Physical [ ] VM [ ] Cloud | _____ | [ ] Small [ ] Medium [ ] Large |
| _____________ | [ ] Physical [ ] VM [ ] Cloud | _____ | [ ] Small [ ] Medium [ ] Large |

!!! info "CE Node Sizes"
    - **Small**: 8 vCPU, 32GB RAM, 80GB disk
    - **Medium**: 8 vCPU, 32GB RAM, 100GB disk (App Stack)
    - **Large**: 16 vCPU, 64GB RAM, 100GB disk

### 4.2 High Availability

CE high availability requirements:

- [ ] **Single node** - Development/non-critical
- [ ] **3-node cluster** - Production HA (recommended)

---

## Section 5: Network Configuration

### 5.1 IP Addressing

Provide subnet information for connected networks:

| Site | Inside Subnet (CIDR) | Outside Subnet (CIDR) | Gateway |
|------|---------------------|----------------------|---------|
| _____________ | _____/___  | _____/___  | _____________ |
| _____________ | _____/___  | _____/___  | _____________ |
| _____________ | _____/___  | _____/___  | _____________ |

### 5.2 Routing Requirements

What routing is required?

- [ ] **Static routing** - Manually configured routes
- [ ] **BGP** - Dynamic routing with BGP
- [ ] **OSPF** - Dynamic routing with OSPF (via BGP redistribution)

BGP requirements (if applicable):

| Parameter | Value |
|-----------|-------|
| Local ASN | _____ |
| Peer ASN(s) | _____ |
| Advertised prefixes | _____ |

### 5.3 NAT Requirements

What NAT is required?

- [ ] **SNAT** - Source NAT for outbound traffic
- [ ] **No NAT** - Direct routing between sites

---

## Section 6: Security Features

### 6.1 Network Firewall

Do you need network firewall between sites?

- [ ] Yes - L3/L4 firewall policies
- [ ] No

Firewall requirements:

| Source | Destination | Protocol | Port | Action |
|--------|-------------|----------|------|--------|
| _____________ | _____________ | _____ | _____ | [ ] Allow [ ] Deny |
| _____________ | _____________ | _____ | _____ | [ ] Allow [ ] Deny |
| _____________ | _____________ | _____ | _____ | [ ] Allow [ ] Deny |

Number of firewall rules: _____

### 6.2 Micro-Segmentation

Do you need network micro-segmentation?

- [ ] Yes - Segment traffic within sites
- [ ] No

### 6.3 Forward Proxy

Do you need forward proxy for outbound traffic?

- [ ] Yes - HTTP/HTTPS inspection
- [ ] Yes - URL filtering
- [ ] No

### 6.4 Service Insertion

Do you need to insert third-party security services?

- [ ] Yes - F5 BIG-IP integration
- [ ] Yes - Palo Alto Networks
- [ ] Yes - Other: _________________
- [ ] No

---

## Section 7: Cloud Integration

### 7.1 AWS Connectivity

If connecting AWS:

| Parameter | Value |
|-----------|-------|
| AWS regions | _____________ |
| VPCs to connect | _____ |
| Transit Gateway integration | [ ] Yes [ ] No |
| Direct Connect | [ ] Yes [ ] No |

### 7.2 Azure Connectivity

If connecting Azure:

| Parameter | Value |
|-----------|-------|
| Azure regions | _____________ |
| VNets to connect | _____ |
| Virtual WAN integration | [ ] Yes [ ] No |
| ExpressRoute | [ ] Yes [ ] No |

### 7.3 GCP Connectivity

If connecting Google Cloud:

| Parameter | Value |
|-----------|-------|
| GCP regions | _____________ |
| VPCs to connect | _____ |
| Cloud Interconnect | [ ] Yes [ ] No |

---

## Section 8: Observability

### 8.1 Visibility Requirements

What network visibility do you need?

- [ ] Site-to-site tunnel status
- [ ] Latency monitoring
- [ ] Bandwidth utilization
- [ ] Flow logs / traffic analysis
- [ ] Security event logging

### 8.2 Integration

Where should network telemetry be sent?

- [ ] F5 XC Console only
- [ ] SIEM integration: _________________
- [ ] Network monitoring tool: _________________

---

## Section 9: Advanced Features (Advanced Tier)

### 9.1 Advanced Network Connect Features

Do you need advanced features?

- [ ] **Anomaly detection** - ML-based traffic analysis
- [ ] **Integrated WAF/DDoS/Bot** - Security at network edge
- [ ] **Advanced service chaining** - Complex traffic flows

### 9.2 Site Mesh Groups

Do you need site mesh groups?

- [ ] **Full mesh** - Direct connectivity between all sites
- [ ] **Hub-spoke mesh** - Connectivity through hub sites
- [ ] No site mesh required

---

## Summary: Multi-Cloud Networking Requirements

| Requirement | Value |
|-------------|-------|
| Total Sites to Connect | _____ |
| Cloud Environments | _____ |
| On-Premises Data Centers | _____ |
| Edge/Branch Sites | _____ |
| Total Inter-Site Bandwidth | _____ Mbps |
| CE Nodes Required | _____ |
| Network Firewall Rules | _____ |
| Tier Required | [ ] Standard [ ] Advanced |

Network topology diagram attached: [ ] Yes [ ] No

Additional notes:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
