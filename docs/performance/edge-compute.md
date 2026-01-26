# Edge Compute Sizing

F5 Distributed Cloud provides edge compute capabilities through Customer Edge sites and App Stack, enabling you to run application logic closer to users.

---

## Section 1: Edge Compute Requirements

### 1.1 Do You Need Edge Compute?

- [ ] Yes - We need to run compute at the edge
- [ ] No - Skip this section

### 1.2 Edge Compute Use Cases

What are your edge compute requirements?

- [ ] **API processing** - Process API requests at the edge
- [ ] **Data transformation** - Transform data before reaching origin
- [ ] **Authentication** - Edge authentication/authorization
- [ ] **Content personalization** - Personalize content at the edge
- [ ] **IoT processing** - Process IoT data locally
- [ ] **Machine learning inference** - Run ML models at the edge
- [ ] **Real-time analytics** - Process analytics locally
- [ ] Other: _________________

---

## Section 2: Workload Profile

### 2.1 Workload Types

What types of workloads will run at the edge?

- [ ] Containers (Docker/Kubernetes)
- [ ] Virtual machines
- [ ] Serverless functions
- [ ] Custom applications

### 2.2 Workload Details

| Workload Name | Type | CPU | Memory | Storage |
|---------------|------|-----|--------|---------|
| _____________ | [ ] Container [ ] VM | _____ cores | _____ GB | _____ GB |
| _____________ | [ ] Container [ ] VM | _____ cores | _____ GB | _____ GB |
| _____________ | [ ] Container [ ] VM | _____ cores | _____ GB | _____ GB |

### 2.3 Workload Scaling

How should workloads scale?

- [ ] Fixed size - Manual scaling
- [ ] Horizontal auto-scaling
- [ ] Vertical scaling

---

## Section 3: Edge Locations

### 3.1 Edge Site Locations

Where do you need edge compute?

| Location | Site Type | Workloads |
|----------|-----------|-----------|
| _____________ | [ ] Data Center [ ] Branch [ ] Retail [ ] Other | _____________ |
| _____________ | [ ] Data Center [ ] Branch [ ] Retail [ ] Other | _____________ |
| _____________ | [ ] Data Center [ ] Branch [ ] Retail [ ] Other | _____________ |

Total edge compute locations: _____

### 3.2 Edge Infrastructure

What infrastructure is available at edge locations?

| Location | Compute Available | Network | Power/Cooling |
|----------|-------------------|---------|---------------|
| _____________ | [ ] Servers [ ] VMs [ ] None | _____ Mbps | [ ] Yes [ ] Limited |
| _____________ | [ ] Servers [ ] VMs [ ] None | _____ Mbps | [ ] Yes [ ] Limited |

---

## Section 4: App Stack Requirements

### 4.1 App Stack Deployment

Do you need F5 App Stack (managed Kubernetes)?

- [ ] Yes - Managed K8s at the edge
- [ ] No - Using existing infrastructure

### 4.2 Container Requirements

If using containers:

| Parameter | Value |
|-----------|-------|
| Total containers | _____ |
| Container registry | [ ] Docker Hub [ ] Private [ ] AWS ECR [ ] Azure ACR [ ] GCR |
| Container sizes needed | [ ] Tiny [ ] Medium [ ] Large |

!!! info "Container Sizes"
    - **Tiny**: 0.25 vCPU, 0.5GB RAM
    - **Medium**: 1 vCPU, 2GB RAM
    - **Large**: 2 vCPU, 4GB RAM

---

## Section 5: Networking

### 5.1 Edge Network Requirements

How do edge workloads need to communicate?

- [ ] With origin/cloud services
- [ ] With other edge sites
- [ ] With local devices (IoT, sensors)
- [ ] With external APIs

### 5.2 Network Performance

| Requirement | Value |
|-------------|-------|
| Latency to local users | < _____ ms |
| Bandwidth to cloud | _____ Mbps |
| Local network bandwidth | _____ Mbps |

---

## Section 6: Data Management

### 6.1 Data at the Edge

What data will be processed at the edge?

- [ ] User data / PII
- [ ] IoT sensor data
- [ ] Transaction data
- [ ] Log data
- [ ] Media / video

### 6.2 Data Residency

Are there data residency requirements?

- [ ] Yes - Data must stay in specific regions
- [ ] No

Regions with data residency requirements: _________________

### 6.3 Edge Storage

Do you need persistent storage at the edge?

- [ ] Yes - _____ GB per site
- [ ] No - Stateless workloads only

---

## Summary: Edge Compute Requirements

| Requirement | Value |
|-------------|-------|
| Edge Compute Locations | _____ |
| Total Workloads | _____ |
| App Stack (Managed K8s) | [ ] Yes [ ] No |
| Container Count | _____ |
| Persistent Storage | [ ] Yes [ ] No |

Primary edge compute use case:

```
_____________________________________________________________
_____________________________________________________________
```
