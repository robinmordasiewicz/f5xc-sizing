# Infrastructure Overview

F5 Distributed Cloud can be deployed through Customer Edge (CE) sites in your environment or through Cloud Sites managed by F5 in public cloud providers.

## Deployment Options

<div class="grid cards" markdown>

-   :material-server:{ .lg .middle } **Customer Edge Sites**

    ---

    Deploy F5 software in your data centers, private clouds, or edge locations for private connectivity and local processing.

    [:octicons-arrow-right-24: CE Site Questionnaire](customer-edge.md)

-   :material-cloud:{ .lg .middle } **Cloud Sites**

    ---

    Deploy F5 managed sites in AWS, Azure, or Google Cloud for cloud-native integration.

    [:octicons-arrow-right-24: Cloud Sites Questionnaire](cloud-sites.md)

</div>

## Deployment Model Comparison

| Aspect | Customer Edge | Cloud Site |
|--------|---------------|------------|
| **Location** | Your infrastructure | F5 managed in public cloud |
| **Management** | You manage hardware/VMs | F5 manages infrastructure |
| **Connectivity** | Private network access | Cloud-native integration |
| **Use Cases** | On-prem apps, edge locations | Cloud-native apps |
| **Requirements** | Hardware/VM resources | Cloud account |

## Deployment Assessment

### Where Do You Need F5 XC Deployed?

| Location Type | Count | Deployment Type |
|---------------|-------|-----------------|
| On-premises data centers | _____ | [ ] CE |
| Private cloud | _____ | [ ] CE |
| AWS | _____ | [ ] CE [ ] Cloud Site |
| Azure | _____ | [ ] CE [ ] Cloud Site |
| Google Cloud | _____ | [ ] CE [ ] Cloud Site |
| Edge / Branch locations | _____ | [ ] CE |
| Colocation facilities | _____ | [ ] CE |

### Deployment Drivers

Why do you need specific deployment types?

- [ ] **Private connectivity** - Access to private networks/apps
- [ ] **Data residency** - Data must stay in specific locations
- [ ] **Latency** - Need local processing
- [ ] **Cloud integration** - Native cloud connectivity
- [ ] **Compliance** - Regulatory requirements
- [ ] **Existing infrastructure** - Leverage current hardware

## Proceed to Detailed Questionnaires

1. [Customer Edge Sites](customer-edge.md)
2. [Cloud Sites](cloud-sites.md)
