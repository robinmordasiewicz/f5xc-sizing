# Cloud Sites Sizing

Cloud Sites are F5-managed deployments in public cloud providers (AWS, Azure,
GCP) that provide cloud-native integration and connectivity.

---

## Cloud Site Requirements

### Cloud Site Use Cases

Why do you need Cloud Sites?

- [ ] **Cloud-native apps** - Protect cloud workloads
- [ ] **VPC/VNet connectivity** - Connect to private cloud networks
- [ ] **Multi-cloud networking** - Bridge multiple clouds
- [ ] **Cloud egress** - Secure internet access from cloud
- [ ] **Service mesh** - Connect cloud-based services
- [ ] Other: _________________

---

## Cloud Provider Inventory

### AWS Sites

- [ ] Yes
- [ ] No

If yes:

| AWS Region | VPCs to Connect | Workloads | Node Size |
| --- | --- | --- | --- |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |

AWS integration requirements:

- [ ] AWS Transit Gateway integration
- [ ] AWS Direct Connect integration
- [ ] VPC peering
- [ ] PrivateLink endpoints

### Azure Sites

- [ ] Yes
- [ ] No

If yes:

| Azure Region | VNets to Connect | Workloads | Node Size |
| --- | --- | --- | --- |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |

Azure integration requirements:

- [ ] Azure Virtual WAN integration
- [ ] Azure ExpressRoute integration
- [ ] VNet peering
- [ ] Private Endpoint

### Google Cloud Sites

- [ ] Yes
- [ ] No

If yes:

| GCP Region | VPCs to Connect | Workloads | Node Size |
| --- | --- | --- | --- |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |
| _____________ | _____ | _____________ | [ ] Standard [ ] Large |

GCP integration requirements:

- [ ] Cloud Interconnect integration
- [ ] Shared VPC support
- [ ] Private Service Connect

---

## Cloud Network Configuration

### Deployment Mode

How should Cloud Sites be deployed?

- [ ] **Ingress/Egress Gateway** - Single interface, simplified
- [ ] **Ingress Gateway** - Internet-facing only
- [ ] **Workload** - Full routing capability

### IP Addressing

| Cloud Site | Site Network CIDR | Inside Subnets | Outside Subnets |
| --- | --- | --- | --- |
| _____________ | ___**/**_ | _____ | _____ |
| _____________ | ___**/**_ | _____ | _____ |
| _____________ | ___**/**_ | _____ | _____ |

### VPC/VNet Connectivity

What cloud networks need connectivity?

| Cloud Network | Cloud Provider | CIDR | Connect To |
| --- | --- | --- | --- |
| _____________ | [ ] AWS [ ] Azure [ ] GCP | ___**/**_ | _____________ |
| _____________ | [ ] AWS [ ] Azure [ ] GCP | ___**/**_ | _____________ |
| _____________ | [ ] AWS [ ] Azure [ ] GCP | ___**/**_ | _____________ |

---

## High Availability

### HA Configuration

What availability is required?

| Cloud Site | HA Mode | Availability Zones |
| --- | --- | --- |
| _____________ | [ ] Single AZ [ ] Multi-AZ | _____ AZs |
| _____________ | [ ] Single AZ [ ] Multi-AZ | _____ AZs |
| _____________ | [ ] Single AZ [ ] Multi-AZ | _____ AZs |

### Node Count

| Cloud Site | Master Nodes | Worker Nodes (if App Stack) |
| --- | --- | --- |
| _____________ | [ ] 1 [ ] 3 | _____ |
| _____________ | [ ] 1 [ ] 3 | _____ |
| _____________ | [ ] 1 [ ] 3 | _____ |

---

## Services at Cloud Sites

### Services Required

What services will run at Cloud Sites?

| Cloud Site | Services |
| --- | --- |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
| _____________ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |

### Traffic Volume

| Cloud Site | Expected Throughput | Connections |
| --- | --- | --- |
| _____________ | _____ Mbps | _____ |
| _____________ | _____ Mbps | _____ |
| _____________ | _____ Mbps | _____ |

---

## Cloud Credentials

### Cloud Account Access

How will F5 XC access your cloud accounts?

| Cloud Provider | Access Method | Account/Subscription ID |
| --- | --- | --- |
| AWS | [ ] IAM Role [ ] Access Key | _____________ |
| Azure | [ ] Service Principal | _____________ |
| GCP | [ ] Service Account | _____________ |

### Permissions Required

Have you reviewed F5 XC required cloud permissions?

- [ ] Yes - AWS IAM policy reviewed
- [ ] Yes - Azure RBAC permissions reviewed
- [ ] Yes - GCP IAM roles reviewed
- [ ] No - Need to review

---

## Cost Optimization

### Instance Types

Preferred cloud instance types:

| Cloud Provider | Instance Type | vCPU | Memory |
| --- | --- | --- | --- |
| AWS | [ ] t3.xlarge [ ] m5.xlarge [ ] m5.2xlarge [ ] Custom | _____ | _____ GB |
| Azure | [ ] Standard_D4s_v4 [ ] Standard_D8s_v4 [ ] Custom | _____ | _____ GB |
| GCP | [ ] n1-standard-4 [ ] n1-standard-8 [ ] Custom | _____ | _____ GB |

### Cost Considerations

- [ ] Use spot/preemptible instances where possible
- [ ] Use reserved capacity for steady workloads
- [ ] Optimize for specific regions with lower costs

---

## Summary: Cloud Sites Requirements

| Requirement | Value |
| --- | --- |
| AWS Cloud Sites | _____ |
| Azure Cloud Sites | _____ |
| GCP Cloud Sites | _____ |
| Total Cloud Sites | _____ |
| Multi-AZ Deployments | _____ |
| App Stack Sites | _____ |

Cloud regions to deploy:

```text
AWS: _____________________________________________________________
Azure: _____________________________________________________________
GCP: _____________________________________________________________
```

Additional notes:

```text
_____________________________________________________________
_____________________________________________________________
```
