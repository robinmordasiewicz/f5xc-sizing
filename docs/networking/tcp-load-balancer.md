# TCP Load Balancer Sizing

F5 Distributed Cloud TCP Load Balancer provides Layer 4 load balancing for non-HTTP protocols including databases, gaming servers, mail servers, and custom TCP/UDP applications.

---

## Section 1: TCP Load Balancer Requirements

### 1.1 Do You Need TCP Load Balancing?

- [ ] Yes - We have non-HTTP applications to load balance
- [ ] No - Skip this section

### 1.2 Application Inventory

What TCP/UDP applications need load balancing?

| Application | Protocol | Port(s) | Use Case |
|-------------|----------|---------|----------|
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |
| _____________ | [ ] TCP [ ] UDP | _____ | [ ] Database [ ] Gaming [ ] Mail [ ] SSH [ ] Custom |

### 1.3 Port Configuration

Do you need to load balance multiple ports?

- [ ] Single port per load balancer
- [ ] Multiple specific ports: _____
- [ ] Port range: _____ to _____

---

## Section 2: Traffic Volume

### 2.1 Connection Metrics

| Metric | Average | Peak |
|--------|---------|------|
| Connections per second | _____ | _____ |
| Concurrent connections | _____ | _____ |
| Bandwidth (Mbps) | _____ | _____ |
| Average connection duration | _____ seconds | _____ |

### 2.2 Connection Patterns

What are your connection patterns?

- [ ] Short-lived connections (request/response)
- [ ] Long-lived connections (persistent)
- [ ] Mixed

---

## Section 3: Origin Configuration

### 3.1 Origin Servers

| Application | Origin Type | Count | Ports |
|-------------|-------------|-------|-------|
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |
| _____________ | [ ] IP [ ] FQDN | _____ | _____ |

### 3.2 Origin Connectivity

How will F5 XC reach TCP origins?

- [ ] Public Internet
- [ ] Customer Edge site
- [ ] Cloud Site (AWS/Azure/GCP)
- [ ] Private connectivity

---

## Section 4: Load Balancing Configuration

### 4.1 Load Balancing Algorithm

- [ ] **Round Robin**
- [ ] **Least Connections**
- [ ] **Source IP Hash** (session persistence)
- [ ] **Random**

### 4.2 Health Checks

Health check configuration:

| Parameter | Value |
|-----------|-------|
| Health check type | [ ] TCP Connect [ ] Custom |
| Check interval | _____ seconds |
| Healthy threshold | _____ checks |
| Unhealthy threshold | _____ checks |
| Timeout | _____ seconds |

### 4.3 Session Persistence

Do you need session persistence?

- [ ] Yes - Source IP based
- [ ] No - Connections can go to any origin

---

## Section 5: TLS Configuration

### 5.1 TLS Requirements

Do you need TLS for TCP connections?

- [ ] **TLS Termination** - F5 terminates TLS
- [ ] **TLS Pass-Through** - Pass encrypted traffic to origin
- [ ] **No TLS** - Unencrypted TCP

### 5.2 Certificate Configuration

If TLS termination:

| Parameter | Value |
|-----------|-------|
| Certificate source | [ ] Automatic [ ] Custom |
| Minimum TLS version | [ ] TLS 1.2 [ ] TLS 1.3 |
| mTLS required | [ ] Yes [ ] No |

---

## Section 6: Timeouts and Limits

### 6.1 Connection Timeouts

| Parameter | Value |
|-----------|-------|
| Connection timeout | _____ seconds |
| Idle timeout | _____ seconds |

### 6.2 Connection Limits

| Parameter | Value |
|-----------|-------|
| Max connections per client IP | _____ |
| Max total connections | _____ |

---

## Section 7: Use Case Specific

### 7.1 Database Load Balancing

If load balancing databases:

| Parameter | Value |
|-----------|-------|
| Database type | [ ] MySQL [ ] PostgreSQL [ ] MongoDB [ ] Redis [ ] Other: ___ |
| Read/Write splitting needed | [ ] Yes [ ] No |
| Connection pooling | [ ] Yes [ ] No |

### 7.2 Gaming/Real-Time

If gaming or real-time applications:

| Parameter | Value |
|-----------|-------|
| UDP support needed | [ ] Yes [ ] No |
| Latency sensitivity | [ ] Critical [ ] Important [ ] Normal |
| Geographic proximity required | [ ] Yes [ ] No |

---

## Summary: TCP Load Balancer Requirements

| Requirement | Value |
|-------------|-------|
| Number of TCP Load Balancers | _____ |
| Protocols | [ ] TCP [ ] UDP [ ] Both |
| Port(s) | _____ |
| Peak Connections per Second | _____ |
| TLS Required | [ ] Yes [ ] No |
| Session Persistence | [ ] Yes [ ] No |

Additional notes:

```
_____________________________________________________________
_____________________________________________________________
```
