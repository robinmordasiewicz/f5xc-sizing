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
- [ ] Other: ___

---

## Cloud Provider Inventory

### AWS Sites

- [ ] Yes
- [ ] No

If yes:

| AWS Region | VPCs to Connect | Workloads | Node Size |
| --- | --- | --- | --- |
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |

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
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |

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
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |
| ___ | ___ | ___ | [ ] Standard [ ] Large |

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
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |

### VPC/VNet Connectivity

What cloud networks need connectivity?

| Cloud Network | Cloud Provider | CIDR | Connect To |
| --- | --- | --- | --- |
| ___ | [ ] AWS [ ] Azure [ ] GCP | ___ | ___ |
| ___ | [ ] AWS [ ] Azure [ ] GCP | ___ | ___ |
| ___ | [ ] AWS [ ] Azure [ ] GCP | ___ | ___ |

---

## High Availability

### HA Configuration

What availability is required?

| Cloud Site | HA Mode | Availability Zones |
| --- | --- | --- |
| ___ | [ ] Single AZ [ ] Multi-AZ | ___ AZs |
| ___ | [ ] Single AZ [ ] Multi-AZ | ___ AZs |
| ___ | [ ] Single AZ [ ] Multi-AZ | ___ AZs |

### Node Count

| Cloud Site | Master Nodes | Worker Nodes (if App Stack) |
| --- | --- | --- |
| ___ | [ ] 1 [ ] 3 | ___ |
| ___ | [ ] 1 [ ] 3 | ___ |
| ___ | [ ] 1 [ ] 3 | ___ |

---

## Services at Cloud Sites

### Services Required

What services will run at Cloud Sites?

| Cloud Site | Services |
| --- | --- |
| ___ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
| ___ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
| ___ | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |

### Traffic Volume

| Cloud Site | Expected Throughput | Connections |
| --- | --- | --- |
| ___ | ___ Mbps | ___ |
| ___ | ___ Mbps | ___ |
| ___ | ___ Mbps | ___ |

---

## Cloud Credentials

### Cloud Account Access

How will F5 XC access your cloud accounts?

| Cloud Provider | Access Method | Account/Subscription ID |
| --- | --- | --- |
| AWS | [ ] IAM Role [ ] Access Key | ___ |
| Azure | [ ] Service Principal | ___ |
| GCP | [ ] Service Account | ___ |

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
| AWS | [ ] t3.xlarge [ ] m5.xlarge [ ] m5.2xlarge [ ] Custom | ___ | ___ GB |
| Azure | [ ] Standard_D4s_v4 [ ] Standard_D8s_v4 [ ] Custom | ___ | ___ GB |
| GCP | [ ] n1-standard-4 [ ] n1-standard-8 [ ] Custom | ___ | ___ GB |

### Cost Considerations

- [ ] Use spot/preemptible instances where possible
- [ ] Use reserved capacity for steady workloads
- [ ] Optimize for specific regions with lower costs

---

## Summary: Cloud Sites Requirements

| Requirement | Value |
| --- | --- |
| AWS Cloud Sites | ___ |
| Azure Cloud Sites | ___ |
| GCP Cloud Sites | ___ |
| Total Cloud Sites | ___ |
| Multi-AZ Deployments | ___ |
| App Stack Sites | ___ |

Cloud regions to deploy:

```text
AWS: ___
Azure: ___
GCP: ___
```

Additional notes:

```text
___
```
