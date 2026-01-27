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
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |

### Port Configuration

- [ ] Single port per load balancer
- [ ] Multiple specific ports: _____
- [ ] Port range: _____ to _____

---

## Traffic Volume

### Connection Metrics

| Metric | Average | Peak |
| --- | --- | --- |
| Connections per second | _____ | _____ |
| Concurrent connections | _____ | _____ |
| Bandwidth (Mbps) | _____ | _____ |
| Average connection duration | _____ seconds | _____ |

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
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |

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
| Check interval | _____ seconds |
| Healthy threshold | _____ checks |
| Unhealthy threshold | _____ checks |
| Timeout | _____ seconds |

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
| Connection timeout | _____ seconds |
| Idle timeout | _____ seconds |

### Connection Limits

| Parameter | Value |
| --- | --- |
| Max connections per client IP | _____ |
| Max total connections | _____ |

---

## Use Case Specific

### Database Load Balancing

If load balancing databases:

| Parameter | Value |
| --- | --- |
| Database type | [ ] MySQL [ ] PostgreSQL [ ] MongoDB [ ] Redis [ ] Other: ___ |
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
| Number of TCP Load Balancers | _____ |
| Protocols | [ ] TCP [ ] UDP [ ] Both |
| Port(s) | _____ |
| Peak Connections per Second | _____ |
| TLS Required | [ ] Yes [ ] No |
| Session Persistence | [ ] Yes [ ] No |

Additional notes:

```text
_____________________________________________________________
_____________________________________________________________
```
