# Customer Edge Sites Sizing

Customer Edge (CE) sites are F5 software deployments in your environment that
provide private connectivity, local security enforcement, and edge compute
capabilities.

---

## CE Site Requirements

### CE Use Cases

Why do you need Customer Edge sites?

- [ ] **Private connectivity** - Access applications on private networks
- [ ] **Local security enforcement** - WAF/security at the edge
- [ ] **Multi-cloud networking** - Site-to-site connectivity
- [ ] **Edge compute** - Run workloads locally
- [ ] **Low latency** - Local processing requirements
- [ ] **Data residency** - Keep data local
- [ ] Other: _________________

---

## Site Inventory

### Site Locations

Where will CE sites be deployed?

| Site Name | Location | Environment | Purpose |
| --- | --- | --- | --- |
| _____________ | _____________ | [ ] DC [ ] Branch [ ] Edge [ ] Cloud | _____________ |
| _____________ | _____________ | [ ] DC [ ] Branch [ ] Edge [ ] Cloud | _____________ |
| _____________ | _____________ | [ ] DC [ ] Branch [ ] Edge [ ] Cloud | _____________ |
| _____________ | _____________ | [ ] DC [ ] Branch [ ] Edge [ ] Cloud | _____________ |
| _____________ | _____________ | [ ] DC [ ] Branch [ ] Edge [ ] Cloud | _____________ |

Total CE sites: _____

### Site Criticality

| Site | Criticality | High Availability Required |
| --- | --- | --- |
| _____________ | [ ] Critical [ ] High [ ] Medium [ ] Low | [ ] Yes (3-node) [ ] No (1-node) |
| _____________ | [ ] Critical [ ] High [ ] Medium [ ] Low | [ ] Yes (3-node) [ ] No (1-node) |
| _____________ | [ ] Critical [ ] High [ ] Medium [ ] Low | [ ] Yes (3-node) [ ] No (1-node) |

---

## Infrastructure Requirements

### Deployment Platform

How will CE sites be deployed?

| Site | Platform | Hypervisor/OS |
| --- | --- | --- |
| _____________ | [ ] VM [ ] Bare Metal [ ] Cloud VM | _____________ |
| _____________ | [ ] VM [ ] Bare Metal [ ] Cloud VM | _____________ |
| _____________ | [ ] VM [ ] Bare Metal [ ] Cloud VM | _____________ |

### Node Sizing

What size CE nodes do you need?

!!! info "CE Node Size Reference"

| Size | vCPU | RAM | Disk | Use Case |
| --- | --- | --- | --- | --- |
| **Standard** | 8 | 32GB | 80GB | Basic networking/security |
| **App Stack** | 8 | 32GB | 100GB | + Container workloads |
| **Large** | 16 | 64GB | 100GB | High throughput/complex policies |

| Site | Size | Nodes | Total vCPU | Total RAM |
| --- | --- | --- | --- | --- |
| _____________ | [ ] Standard [ ] App Stack [ ] Large | [ ] 1 [ ] 3 | _____ | _____ GB |
| _____________ | [ ] Standard [ ] App Stack [ ] Large | [ ] 1 [ ] 3 | _____ | _____ GB |
| _____________ | [ ] Standard [ ] App Stack [ ] Large | [ ] 1 [ ] 3 | _____ | _____ GB |

### High Availability Configuration

For production sites, 3-node clusters are recommended:

| Site | HA Mode | Nodes | Notes |
| --- | --- | --- | --- |
| _____________ | [ ] Single [ ] 3-node HA | _____ | _____________ |
| _____________ | [ ] Single [ ] 3-node HA | _____ | _____________ |

---

## Network Configuration

### Network Interfaces

How many network interfaces per CE node?

- [ ] **Single interface (on-a-stick)** - Simplified deployment
- [ ] **Dual interface** - Inside and outside networks
- [ ] **Multiple interfaces** - Complex routing

### IP Addressing

| Site | Interface | Subnet | Gateway | DHCP or Static |
| --- | --- | --- | --- | --- |
| _____________ | Outside | ___**/**_ | _____________ | [ ] DHCP [ ] Static |
| _____________ | Inside | ___**/**_ | _____________ | [ ] DHCP [ ] Static |
| _____________ | Outside | ___**/**_ | _____________ | [ ] DHCP [ ] Static |
| _____________ | Inside | ___**/**_ | _____________ | [ ] DHCP [ ] Static |

### DNS Configuration

| Site | DNS Servers |
| --- | --- |
| _____________ | _____________ |
| _____________ | _____________ |

### Internet Connectivity

How do CE sites connect to F5 Regional Edges?

| Site | Internet Access | Proxy Required |
| --- | --- | --- |
| _____________ | [ ] Direct [ ] NAT [ ] Proxy | [ ] Yes [ ] No |
| _____________ | [ ] Direct [ ] NAT [ ] Proxy | [ ] Yes [ ] No |

---

## Workload Configuration

### Services at CE Sites

What services will run at CE sites?

| Site | Services |
| --- | --- |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |

### Origin Servers Behind CE

What applications/services are behind each CE?

| Site | Applications | Servers/IPs |
| --- | --- | --- |
| _____________ | _____________ | _____ servers |
| _____________ | _____________ | _____ servers |
| _____________ | _____________ | _____ servers |

### Traffic Volume Through CE

| Site | Requests/sec | Bandwidth | Connections |
| --- | --- | --- | --- |
| _____________ | _____ | _____ Mbps | _____ |
| _____________ | _____ | _____ Mbps | _____ |
| _____________ | _____ | _____ Mbps | _____ |

---

## Security Configuration

### Network Firewall at CE

- [ ] Yes - Ingress filtering
- [ ] Yes - Egress filtering
- [ ] Yes - East-West filtering
- [ ] No

Estimated firewall rules per site: _____

### Forward Proxy at CE

- [ ] Yes - For outbound internet access
- [ ] No

### Network Policies

What network policies are needed?

- [ ] Allow/deny lists
- [ ] Geographic restrictions
- [ ] Rate limiting
- [ ] Custom L3/L4 rules

---

## Multi-Cloud Connectivity

### Site Mesh

Will CE sites participate in site mesh?

- [ ] Yes - Full mesh with other CEs
- [ ] Yes - Hub-spoke topology
- [ ] No

### Tunnel Configuration

| Site | Connects To | Tunnel Type |
| --- | --- | --- |
| _____________ | _____________ | [ ] IPsec [ ] SSL VPN |
| _____________ | _____________ | [ ] IPsec [ ] SSL VPN |

---

## App Stack (Optional)

### App Stack Required

- [ ] Yes - Run container workloads
- [ ] No - Networking/security only

If yes:

| Site | Containers | Storage | Registry |
| --- | --- | --- | --- |
| _____________ | _____ | _____ GB | _____________ |
| _____________ | _____ | _____ GB | _____________ |

---

## Operational Requirements

### Management Access

How will CE sites be managed?

- [ ] F5 XC Console (required)
- [ ] SSH access for troubleshooting
- [ ] Local console access

### Monitoring

What monitoring is required?

- [ ] Infrastructure health (CPU/Memory/Disk)
- [ ] Network metrics (throughput/latency)
- [ ] Application metrics
- [ ] Security events

### Maintenance Windows

| Site | Maintenance Window | Change Control |
| --- | --- | --- |
| _____________ | _____________ | [ ] Standard [ ] Expedited [ ] Emergency only |
| _____________ | _____________ | [ ] Standard [ ] Expedited [ ] Emergency only |

---

## Summary: Customer Edge Requirements

| Requirement | Value |
| --- | --- |
| Total CE Sites | _____ |
| HA Sites (3-node) | _____ |
| Single Node Sites | _____ |
| Total CE Nodes | _____ |
| Total vCPU Required | _____ |
| Total RAM Required | _____ GB |
| App Stack Sites | _____ |

Site deployment timeline:

| Site | Target Deployment Date |
| --- | --- |
| _____________ | _____________ |
| _____________ | _____________ |
| _____________ | _____________ |

Additional notes:

```text
_____________________________________________________________
_____________________________________________________________
```
