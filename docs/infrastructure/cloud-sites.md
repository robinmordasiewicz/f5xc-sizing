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
- [ ] Other:

---

## Cloud Provider Inventory

### AWS Sites

- [ ] Yes
- [ ] No

If yes:

| AWS Region | VPCs to Connect | Workloads | Node Size |
| --- | --- | --- | --- |
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |

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
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |

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
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |
|  |  |  | [ ] Standard [ ] Large |

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
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### VPC/VNet Connectivity

What cloud networks need connectivity?

| Cloud Network | Cloud Provider | CIDR | Connect To |
| --- | --- | --- | --- |
|  | [ ] AWS [ ] Azure [ ] GCP |  |  |
|  | [ ] AWS [ ] Azure [ ] GCP |  |  |
|  | [ ] AWS [ ] Azure [ ] GCP |  |  |

---

## High Availability

### HA Configuration

What availability is required?

| Cloud Site | HA Mode | Availability Zones |
| --- | --- | --- |
|  | [ ] Single AZ [ ] Multi-AZ | AZs |
|  | [ ] Single AZ [ ] Multi-AZ | AZs |
|  | [ ] Single AZ [ ] Multi-AZ | AZs |

### Node Count

| Cloud Site | Master Nodes | Worker Nodes (if App Stack) |
| --- | --- | --- |
|  | [ ] 1 [ ] 3 |  |
|  | [ ] 1 [ ] 3 |  |
|  | [ ] 1 [ ] 3 |  |

---

## Services at Cloud Sites

### Services Required

What services will run at Cloud Sites?

| Cloud Site | Services |
| --- | --- |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |
|  | [ ] HTTP LB [ ] TCP LB [ ] WAF [ ] Network Connect [ ] App Stack |

### Traffic Volume

| Cloud Site | Expected Throughput | Connections |
| --- | --- | --- |
|  | Mbps |  |
|  | Mbps |  |
|  | Mbps |  |

---

## Cloud Credentials

### Cloud Account Access

How will F5 XC access your cloud accounts?

| Cloud Provider | Access Method | Account/Subscription ID |
| --- | --- | --- |
| AWS | [ ] IAM Role [ ] Access Key |  |
| Azure | [ ] Service Principal |  |
| GCP | [ ] Service Account |  |

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
| AWS | [ ] t3.xlarge [ ] m5.xlarge [ ] m5.2xlarge [ ] Custom |  | GB |
| Azure | [ ] Standard_D4s_v4 [ ] Standard_D8s_v4 [ ] Custom |  | GB |
| GCP | [ ] n1-standard-4 [ ] n1-standard-8 [ ] Custom |  | GB |

### Cost Considerations

- [ ] Use spot/preemptible instances where possible
- [ ] Use reserved capacity for steady workloads
- [ ] Optimize for specific regions with lower costs

---

## Summary: Cloud Sites Requirements

| Requirement | Value |
| --- | --- |
| AWS Cloud Sites |  |
| Azure Cloud Sites |  |
| GCP Cloud Sites |  |
| Total Cloud Sites |  |
| Multi-AZ Deployments |  |
| App Stack Sites |  |

Cloud regions to deploy:

```text
AWS:
Azure:
GCP:
```

Additional notes:

```text


```
