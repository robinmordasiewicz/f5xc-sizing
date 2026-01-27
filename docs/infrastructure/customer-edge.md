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
- [ ] Other:

---

## Site Inventory

### Site Locations

Where will CE sites be deployed?

| Site Name | Location | Environment | Purpose |
| --- | --- | --- | --- |
|  |  | ( ) DC ( ) Branch ( ) Edge ( ) Cloud |  |
|  |  | ( ) DC ( ) Branch ( ) Edge ( ) Cloud |  |
|  |  | ( ) DC ( ) Branch ( ) Edge ( ) Cloud |  |
|  |  | ( ) DC ( ) Branch ( ) Edge ( ) Cloud |  |
|  |  | ( ) DC ( ) Branch ( ) Edge ( ) Cloud |  |

Total CE sites:

### Site Criticality

| Site | Criticality | High Availability Required |
| --- | --- | --- |
|  | ( ) Critical ( ) High ( ) Medium ( ) Low | ( ) Yes (3-node) ( ) No (1-node) |
|  | ( ) Critical ( ) High ( ) Medium ( ) Low | ( ) Yes (3-node) ( ) No (1-node) |
|  | ( ) Critical ( ) High ( ) Medium ( ) Low | ( ) Yes (3-node) ( ) No (1-node) |

---

## Infrastructure Requirements

### Deployment Platform

How will CE sites be deployed?

| Site | Platform | Hypervisor/OS |
| --- | --- | --- |
|  | ( ) VM ( ) Bare Metal ( ) Cloud VM |  |
|  | ( ) VM ( ) Bare Metal ( ) Cloud VM |  |
|  | ( ) VM ( ) Bare Metal ( ) Cloud VM |  |

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
|  | ( ) Standard ( ) App Stack ( ) Large | ( ) 1 ( ) 3 |  | GB |
|  | ( ) Standard ( ) App Stack ( ) Large | ( ) 1 ( ) 3 |  | GB |
|  | ( ) Standard ( ) App Stack ( ) Large | ( ) 1 ( ) 3 |  | GB |

### High Availability Configuration

For production sites, 3-node clusters are recommended:

| Site | HA Mode | Nodes | Notes |
| --- | --- | --- | --- |
|  | ( ) Single ( ) 3-node HA |  |  |
|  | ( ) Single ( ) 3-node HA |  |  |

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
|  | Outside |  |  | ( ) DHCP ( ) Static |
|  | Inside |  |  | ( ) DHCP ( ) Static |
|  | Outside |  |  | ( ) DHCP ( ) Static |
|  | Inside |  |  | ( ) DHCP ( ) Static |

### DNS Configuration

| Site | DNS Servers |
| --- | --- |
|  |  |
|  |  |

### Internet Connectivity

How do CE sites connect to F5 Regional Edges?

| Site | Internet Access | Proxy Required |
| --- | --- | --- |
|  | ( ) Direct ( ) NAT ( ) Proxy | ( ) Yes ( ) No |
|  | ( ) Direct ( ) NAT ( ) Proxy | ( ) Yes ( ) No |

---

## Workload Configuration

### Services at CE Sites

What services will run at CE sites?

| Site | Services |
| --- | --- |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Firewall [ ] App Stack |

### Origin Servers Behind CE

What applications/services are behind each CE?

| Site | Applications | Servers/IPs |
| --- | --- | --- |
|  |  | servers |
|  |  | servers |
|  |  | servers |

### Traffic Volume Through CE

| Site | Requests/sec | Bandwidth | Connections |
| --- | --- | --- | --- |
|  |  | Mbps |  |
|  |  | Mbps |  |
|  |  | Mbps |  |

---

## Security Configuration

### Network Firewall at CE

- [ ] Yes - Ingress filtering
- [ ] Yes - Egress filtering
- [ ] Yes - East-West filtering
- [ ] No

Estimated firewall rules per site:

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
|  |  | ( ) IPsec ( ) SSL VPN |
|  |  | ( ) IPsec ( ) SSL VPN |

---

## App Stack (Optional)

### App Stack Required

- [ ] Yes - Run container workloads
- [ ] No - Networking/security only

If yes:

| Site | Containers | Storage | Registry |
| --- | --- | --- | --- |
|  |  | GB |  |
|  |  | GB |  |

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
|  |  | ( ) Standard ( ) Expedited ( ) Emergency only |
|  |  | ( ) Standard ( ) Expedited ( ) Emergency only |

---

## Summary: Customer Edge Requirements

| Requirement | Value |
| --- | --- |
| Total CE Sites |  |
| HA Sites (3-node) |  |
| Single Node Sites |  |
| Total CE Nodes |  |
| Total vCPU Required |  |
| Total RAM Required | GB |
| App Stack Sites |  |

Site deployment timeline:

| Site | Target Deployment Date |
| --- | --- |
|  |  |
|  |  |
|  |  |

Additional notes:

```text


```
