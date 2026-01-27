# App Connect Sizing

F5 Distributed Cloud App Connect provides service mesh capabilities with
app-to-app connectivity, service discovery, and centralized orchestration across
distributed environments.

---

## App Connect Requirements

### Use Cases

What App Connect capabilities do you need?

- [ ] **Service discovery** - Discover services across environments
- [ ] **Service mesh** - Secure service-to-service communication
- [ ] **App migration** - Migrate apps between environments
- [ ] **Kubernetes networking** - Connect K8s clusters
- [ ] **Legacy integration** - Connect legacy and modern apps

---

## Application Environment

### Application Architecture

What type of applications do you have?

- [ ] Monolithic applications
- [ ] Microservices
- [ ] Hybrid (monolith + microservices)
- [ ] Serverless / Functions
- [ ] Legacy applications

### Kubernetes Deployments

Do you have Kubernetes clusters?

- [ ] Yes
- [ ] No

If yes:

| Cluster Name | Location | Distribution | Services |
| --- | --- | --- | --- |
| ___ | ___ | [ ] EKS [ ] AKS [ ] GKE [ ] OpenShift [ ] Other | ___ |
| ___ | ___ | [ ] EKS [ ] AKS [ ] GKE [ ] OpenShift [ ] Other | ___ |
| ___ | ___ | [ ] EKS [ ] AKS [ ] GKE [ ] OpenShift [ ] Other | ___ |

Total Kubernetes clusters: ___

### Service Inventory

How many services need connectivity?

| Environment | Service Count |
| --- | --- |
| Production | ___ |
| Staging | ___ |
| Development | ___ |
| **Total** | ___ |

---

## Service Discovery

### Service Discovery Requirements

What service discovery mechanisms do you use?

- [ ] Kubernetes DNS
- [ ] Consul
- [ ] DNS-based
- [ ] Static configuration
- [ ] Other: ___

### Cross-Environment Discovery

Do services need to discover services in other environments?

- [ ] Yes - Cross-cluster Kubernetes
- [ ] Yes - Kubernetes to VM-based
- [ ] Yes - Cloud to on-premises
- [ ] No - Single environment only

---

## Traffic Management

### Load Balancing

What load balancing is needed between services?

- [ ] Round robin
- [ ] Least connections
- [ ] Weighted distribution
- [ ] Geographic / Proximity-based

### Advanced Traffic Management

- [ ] **A/B testing** - Route percentage to different versions
- [ ] **Canary deployments** - Gradual rollout
- [ ] **Blue-green deployments** - Switch between versions
- [ ] **Header-based routing** - Route based on headers
- [ ] **Fault injection** - Test resilience

### Traffic Patterns

Describe service-to-service traffic patterns:

| Source Service | Destination Service | RPS | Latency Requirement |
| --- | --- | --- | --- |
| ___ | ___ | ___ | < ___ ms |
| ___ | ___ | ___ | < ___ ms |
| ___ | ___ | ___ | < ___ ms |

---

## Security

### Service-to-Service Security

What security is required between services?

- [ ] **mTLS** - Mutual TLS authentication
- [ ] **Service policies** - Allow/deny between services
- [ ] **Encryption** - Encrypt all service traffic

### Policy Requirements

| Source | Destination | Action | Notes |
| --- | --- | --- | --- |
| ___ | ___ | [ ] Allow [ ] Deny | ___ |
| ___ | ___ | [ ] Allow [ ] Deny | ___ |
| ___ | ___ | [ ] Allow [ ] Deny | ___ |

### Identity Integration

What identity systems need integration?

- [ ] Service accounts (Kubernetes)
- [ ] OAuth/OIDC
- [ ] SPIFFE/SPIRE
- [ ] Custom certificates
- [ ] None

---

## Observability

### Service Observability

What service observability do you need?

- [ ] Request tracing
- [ ] Service dependency mapping
- [ ] Traffic flow visualization
- [ ] Error rate monitoring
- [ ] Latency metrics

### Distributed Tracing

Do you use distributed tracing?

- [ ] Yes - Jaeger
- [ ] Yes - Zipkin
- [ ] Yes - Other: ___
- [ ] No

---

## Migration Use Cases

### Application Migration

Are you migrating applications?

- [ ] Yes - Cloud to cloud
- [ ] Yes - On-premises to cloud
- [ ] Yes - Monolith to microservices
- [ ] No

Migration details:

| Application | From | To | Timeline |
| --- | --- | --- | --- |
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |

### Hybrid Operation

- [ ] Yes - Active/Active across locations
- [ ] Yes - Active/Standby failover
- [ ] No

---

## Integration

### Existing Service Mesh

Do you have an existing service mesh?

- [ ] Yes - Istio
- [ ] Yes - Linkerd
- [ ] Yes - Consul Connect
- [ ] Yes - Other: ___
- [ ] No

If yes, will you:

- [ ] Replace with F5 App Connect
- [ ] Integrate/coexist
- [ ] Migrate gradually

### F5 BIG-IP Integration

Do you have F5 BIG-IP to integrate?

- [ ] Yes - Discover BIG-IP services
- [ ] Yes - Extend BIG-IP functionality
- [ ] No

---

## Summary: App Connect Requirements

| Requirement | Value |
| --- | --- |
| Total Services | ___ |
| Kubernetes Clusters | ___ |
| Cross-Environment Discovery | [ ] Yes [ ] No |
| mTLS Required | [ ] Yes [ ] No |
| Advanced Traffic Management | [ ] Yes [ ] No |
| Service Migration | [ ] Yes [ ] No |
| Tier Required | [ ] Standard [ ] Advanced |

Service mesh diagram attached: [ ] Yes [ ] No

Additional notes:

```text
___
```
