# TCP Load Balancer Sizing

F5 Distributed Cloud TCP Load Balancer provides Layer 4 load balancing for
non-HTTP protocols including databases, gaming servers, mail servers, and custom
TCP/UDP applications.

---

## TCP Load Balancer Requirements

### Application Inventory

What TCP/UDP applications need load balancing?

| Application | Protocol | Port(s) | Use Case |
| --- | --- | --- | --- |
|  | [ ] TCP [ ] UDP |  | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
|  | [ ] TCP [ ] UDP |  | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
|  | [ ] TCP [ ] UDP |  | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
|  | [ ] TCP [ ] UDP |  | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |

### Port Configuration

- [ ] Single port per load balancer
- [ ] Multiple specific ports:
- [ ] Port range: to

---

## Traffic Volume

### Connection Metrics

| Metric | Average | Peak |
| --- | --- | --- |
| Connections per second |  |  |
| Concurrent connections |  |  |
| Bandwidth (Mbps) |  |  |
| Average connection duration | seconds |  |

### Connection Patterns

What are your connection patterns?

- [ ] Short-lived connections (request/response)
- [ ] Long-lived connections (persistent)
- [ ] Mixed

---

## Origin Configuration

### Origin Servers

| Application | Origin Type | Count | Ports |
| --- | --- | --- | --- |
|  | [ ] IP [ ] FQDN |  |  |
|  | [ ] IP [ ] FQDN |  |  |
|  | [ ] IP [ ] FQDN |  |  |

### Origin Connectivity

How will F5 XC reach TCP origins?

- [ ] Public Internet
- [ ] Customer Edge site
- [ ] Cloud Site (AWS/Azure/GCP)
- [ ] Private connectivity

---

## Load Balancing Configuration

### Load Balancing Algorithm

- [ ] **Round Robin**
- [ ] **Least Connections**
- [ ] **Source IP Hash** (session persistence)
- [ ] **Random**

### Health Checks

Health check configuration:

| Parameter | Value |
| --- | --- |
| Health check type | [ ] TCP Connect [ ] Custom |
| Check interval | seconds |
| Healthy threshold | checks |
| Unhealthy threshold | checks |
| Timeout | seconds |

### Session Persistence

- [ ] Yes - Source IP based
- [ ] No - Connections can go to any origin

---

## TLS Configuration

### TLS Requirements

- [ ] **TLS Termination** - F5 terminates TLS
- [ ] **TLS Pass-Through** - Pass encrypted traffic to origin
- [ ] **No TLS** - Unencrypted TCP

### Certificate Configuration

If TLS termination:

| Parameter | Value |
| --- | --- |
| Certificate source | [ ] Automatic [ ] Custom |
| Minimum TLS version | [ ] TLS 1.2 [ ] TLS 1.3 |
| mTLS required | [ ] Yes [ ] No |

---

## Timeouts and Limits

### Connection Timeouts

| Parameter | Value |
| --- | --- |
| Connection timeout | seconds |
| Idle timeout | seconds |

### Connection Limits

| Parameter | Value |
| --- | --- |
| Max connections per client IP |  |
| Max total connections |  |

---

## Use Case Specific

### Database Load Balancing

If load balancing databases:

| Parameter | Value |
| --- | --- |
| Database type | [ ] MySQL [ ] PostgreSQL [ ] MongoDB [ ] Redis [ ] Other: |
| Read/Write splitting needed | [ ] Yes [ ] No |
| Connection pooling | [ ] Yes [ ] No |

### Gaming/Real-Time

If gaming or real-time applications:

| Parameter | Value |
| --- | --- |
| UDP support needed | [ ] Yes [ ] No |
| Latency sensitivity | [ ] Critical [ ] Important [ ] Normal |
| Geographic proximity required | [ ] Yes [ ] No |

---

## Summary: TCP Load Balancer Requirements

| Requirement | Value |
| --- | --- |
| Number of TCP Load Balancers |  |
| Protocols | [ ] TCP [ ] UDP [ ] Both |
| Port(s) |  |
| Peak Connections per Second |  |
| TLS Required | [ ] Yes [ ] No |
| Session Persistence | [ ] Yes [ ] No |

Additional notes:

```text


```
