# Networking Services Overview

F5 Distributed Cloud provides comprehensive networking services for application delivery, DNS management, and multi-cloud connectivity.

## Networking Services Portfolio

<div class="grid cards" markdown>

-   :material-load-balance:{ .lg .middle } **HTTP Load Balancing**

    ---

    Global application delivery with intelligent routing, health checks, and advanced traffic management for HTTP/HTTPS applications.

    [:octicons-arrow-right-24: HTTP LB Questionnaire](http-load-balancer.md)

-   :material-server-network:{ .lg .middle } **TCP Load Balancing**

    ---

    Layer 4 load balancing for non-HTTP protocols including databases, gaming, and custom applications.

    [:octicons-arrow-right-24: TCP LB Questionnaire](tcp-load-balancer.md)

-   :material-dns:{ .lg .middle } **DNS Services**

    ---

    Geo-distributed DNS with global server load balancing (GSLB), automatic failover, and DDoS protection.

    [:octicons-arrow-right-24: DNS Questionnaire](dns.md)

-   :material-cloud-sync:{ .lg .middle } **Multi-Cloud Networking**

    ---

    Secure connectivity between clouds, data centers, and edge sites with encrypted site-to-site networking.

    [:octicons-arrow-right-24: MCN Questionnaire](multi-cloud-networking.md)

-   :material-application:{ .lg .middle } **App Connect**

    ---

    Service mesh capabilities with app-to-app connectivity, service discovery, and centralized orchestration.

    [:octicons-arrow-right-24: App Connect Questionnaire](app-connect.md)

</div>

## Networking Requirements Assessment

### Application Delivery Needs

| Requirement | Service | Priority |
|-------------|---------|----------|
| HTTP/HTTPS load balancing | HTTP Load Balancer | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Non-HTTP protocol load balancing | TCP Load Balancer | [ ] High [ ] Medium [ ] Low [ ] N/A |
| DNS hosting and GSLB | DNS Services | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Multi-cloud site connectivity | Network Connect | [ ] High [ ] Medium [ ] Low [ ] N/A |
| Service mesh / App connectivity | App Connect | [ ] High [ ] Medium [ ] Low [ ] N/A |

### Infrastructure Overview

Provide a high-level view of your infrastructure:

| Environment | Locations | Applications |
|-------------|-----------|--------------|
| On-Premises Data Centers | _____ | _____ |
| AWS | _____ regions | _____ |
| Azure | _____ regions | _____ |
| Google Cloud | _____ regions | _____ |
| Edge / Branch Locations | _____ | _____ |
| Other Cloud | _____ | _____ |

### Current Networking Solutions

Do you have existing solutions for:

| Solution Type | Vendor/Product | Replace or Integrate |
|--------------|----------------|---------------------|
| Load Balancer | _____________ | [ ] Replace [ ] Integrate |
| DNS Provider | _____________ | [ ] Replace [ ] Integrate |
| SD-WAN | _____________ | [ ] Replace [ ] Integrate |
| Cloud Networking | _____________ | [ ] Replace [ ] Integrate |
| Service Mesh | _____________ | [ ] Replace [ ] Integrate |

## Network Topology

### Current Architecture

Describe your current network architecture:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

### Target Architecture

What networking improvements are you seeking?

- [ ] Consolidate multiple networking tools
- [ ] Simplify multi-cloud connectivity
- [ ] Improve application performance
- [ ] Enhance disaster recovery
- [ ] Enable zero-trust networking
- [ ] Reduce operational complexity
- [ ] Other: _________________

## Proceed to Detailed Questionnaires

Complete each networking service questionnaire that applies:

1. [HTTP Load Balancing](http-load-balancer.md)
2. [TCP Load Balancing](tcp-load-balancer.md)
3. [DNS Services](dns.md)
4. [Multi-Cloud Networking](multi-cloud-networking.md)
5. [App Connect](app-connect.md)
