# Edge Compute Sizing

F5 Distributed Cloud provides edge compute capabilities through Customer Edge
sites and App Stack, enabling you to run application logic closer to users.

---

## Edge Compute Requirements

### Edge Compute Use Cases

What are your edge compute requirements?

- [ ] **API processing** - Process API requests at the edge
- [ ] **Data transformation** - Transform data before reaching origin
- [ ] **Authentication** - Edge authentication/authorization
- [ ] **Content personalization** - Personalize content at the edge
- [ ] **IoT processing** - Process IoT data locally
- [ ] **Machine learning inference** - Run ML models at the edge
- [ ] **Real-time analytics** - Process analytics locally
- [ ] Other:

---

## Workload Profile

### Workload Types

What types of workloads will run at the edge?

- [ ] Containers (Docker/Kubernetes)
- [ ] Virtual machines
- [ ] Serverless functions
- [ ] Custom applications

### Workload Details

| Workload Name | Type | CPU | Memory | Storage |
| --- | --- | --- | --- | --- |
|  | [ ] Container [ ] VM | cores | GB | GB |
|  | [ ] Container [ ] VM | cores | GB | GB |
|  | [ ] Container [ ] VM | cores | GB | GB |

### Workload Scaling

How should workloads scale?

- [ ] Fixed size - Manual scaling
- [ ] Horizontal auto-scaling
- [ ] Vertical scaling

---

## Edge Locations

### Edge Site Locations

Where do you need edge compute?

| Location | Site Type | Workloads |
| --- | --- | --- |
|  | [ ] Data Center [ ] Branch [ ] Retail [ ] Other |  |
|  | [ ] Data Center [ ] Branch [ ] Retail [ ] Other |  |
|  | [ ] Data Center [ ] Branch [ ] Retail [ ] Other |  |

Total edge compute locations:

### Edge Infrastructure

What infrastructure is available at edge locations?

| Location | Compute Available | Network | Power/Cooling |
| --- | --- | --- | --- |
|  | [ ] Servers [ ] VMs [ ] None | Mbps | [ ] Yes [ ] Limited |
|  | [ ] Servers [ ] VMs [ ] None | Mbps | [ ] Yes [ ] Limited |

---

## App Stack Requirements

### App Stack Deployment

- [ ] Yes - Managed K8s at the edge
- [ ] No - Using existing infrastructure

### Container Requirements

If using containers:

| Parameter | Value |
| --- | --- |
| Total containers |  |
| Container registry | [ ] Docker Hub [ ] Private [ ] AWS ECR [ ] Azure ACR [ ] GCR |
| Container sizes needed | [ ] Tiny [ ] Medium [ ] Large |

!!! info "Container Sizes"
    - **Tiny**: 0.25 vCPU, 0.5GB RAM
    - **Medium**: 1 vCPU, 2GB RAM
    - **Large**: 2 vCPU, 4GB RAM

---

## Networking

### Edge Network Requirements

How do edge workloads need to communicate?

- [ ] With origin/cloud services
- [ ] With other edge sites
- [ ] With local devices (IoT, sensors)
- [ ] With external APIs

### Network Performance

| Requirement | Value |
| --- | --- |
| Latency to local users | < ms |
| Bandwidth to cloud | Mbps |
| Local network bandwidth | Mbps |

---

## Data Management

### Data at the Edge

What data will be processed at the edge?

- [ ] User data / PII
- [ ] IoT sensor data
- [ ] Transaction data
- [ ] Log data
- [ ] Media / video

### Data Residency

Are there data residency requirements?

- [ ] Yes - Data must stay in specific regions
- [ ] No

Regions with data residency requirements:

### Edge Storage

- [ ] Yes - GB per site
- [ ] No - Stateless workloads only

---

## Summary: Edge Compute Requirements

| Requirement | Value |
| --- | --- |
| Edge Compute Locations |  |
| Total Workloads |  |
| App Stack (Managed K8s) | [ ] Yes [ ] No |
| Container Count |  |
| Persistent Storage | [ ] Yes [ ] No |

Primary edge compute use case:

```text


```
