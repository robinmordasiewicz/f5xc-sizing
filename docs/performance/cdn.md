# CDN Sizing

F5 Distributed Cloud CDN provides global content delivery with intelligent
caching, reducing latency and bandwidth costs while integrating with F5's
security services.

---

## CDN Requirements

### CDN Goals

What are your primary CDN goals?

- [ ] Improve user experience / reduce latency
- [ ] Reduce origin server load
- [ ] Reduce bandwidth/egress costs
- [ ] Global content distribution
- [ ] DDoS protection at the edge
- [ ] Other: _________________

---

## Content Profile

### Content Types

What content will be cached?

| Content Type | Percentage | Cache TTL |
| --- | --- | --- |
| Static images (jpg, png, gif, svg) | _____% | _____ hours |
| JavaScript / CSS | _____% | _____ hours |
| Video / Media files | _____% | _____ hours |
| HTML pages | _____% | _____ hours |
| API responses | _____% | _____ seconds |
| Documents (PDF, etc.) | _____% | _____ hours |
| Other: _____________ | _____% | _____ |

### Content Size

| Metric | Value |
| --- | --- |
| Total unique content size | _____ GB/TB |
| Average object size | _____ KB |
| Largest object size | _____ MB |
| Total number of unique objects | _____ |

### Content Origin

Where is your origin content hosted?

| Origin Location | Provider | Percentage |
| --- | --- | --- |
| _____________ | [ ] AWS [ ] Azure [ ] GCP [ ] On-Prem [ ] Other | _____% |
| _____________ | [ ] AWS [ ] Azure [ ] GCP [ ] On-Prem [ ] Other | _____% |

---

## Traffic Volume

### Request Metrics

| Metric | Average | Peak |
| --- | --- | --- |
| Requests per second | _____ | _____ |
| Requests per month | _____ | _____ |
| Bandwidth (Gbps) | _____ | _____ |

### Regional Distribution

Where are your users located?

| Region | Traffic Percentage |
| --- | --- |
| North America | _____% |
| Europe | _____% |
| Asia-Pacific | _____% |
| South America | _____% |
| Other | _____% |

!!! note "Regional Pricing"
    CDN data transfer and request pricing varies by region.

---

## Caching Configuration

### Cache Policy

How should content be cached?

- [ ] **Honor origin headers** - Respect Cache-Control headers
- [ ] **Override with custom TTL** - Set custom cache times
- [ ] **Query string handling**: [ ] Include [ ] Ignore [ ] Selective

### Cache Key Configuration

What should be included in cache keys?

- [ ] URL path
- [ ] Query string parameters
- [ ] Specific headers: _________________
- [ ] Cookies: _________________

### Cache Purge Requirements

How will you purge cached content?

- [ ] Manual purge via console
- [ ] API-based purge
- [ ] Tag-based purge
- [ ] Path-based purge
- [ ] Full cache purge

Estimated purge frequency: _____ per day/week

---

## Security Integration

### CDN with Security

- [ ] WAF at the edge
- [ ] Bot defense at the edge
- [ ] DDoS protection
- [ ] Rate limiting
- [ ] Geographic restrictions

### TLS Configuration

| Parameter | Value |
| --- | --- |
| TLS termination at edge | [ ] Yes [ ] No |
| Minimum TLS version | [ ] TLS 1.2 [ ] TLS 1.3 |
| Custom certificates | [ ] Yes [ ] No |
| HTTP to HTTPS redirect | [ ] Yes [ ] No |

---

## Advanced Features

### Dynamic Content Optimization

- [ ] Image optimization / WebP conversion
- [ ] Minification (JS/CSS/HTML)
- [ ] Compression (Gzip/Brotli)
- [ ] HTTP/2 / HTTP/3 support

### Custom Rules

| URL Pattern | Cache Behavior | TTL |
| --- | --- | --- |
| /api/* | [ ] Cache [ ] Bypass | _____ |
| /static/* | [ ] Cache [ ] Bypass | _____ |
| *.css | [ ] Cache [ ] Bypass | _____ |
| _____________ | [ ] Cache [ ] Bypass | _____ |

---

## Performance Metrics

### Expected Cache Performance

| Metric | Target |
| --- | --- |
| Target cache hit ratio | > _____% |
| Target TTFB from edge | < _____ ms |
| Acceptable origin load reduction | _____% |

### Monitoring Requirements

What CDN metrics do you need?

- [ ] Cache hit/miss ratios
- [ ] Bandwidth by region
- [ ] Request counts
- [ ] Error rates
- [ ] Origin response times
- [ ] Popular content reports

---

## Summary: CDN Requirements

| Requirement | Value |
| --- | --- |
| Domains to CDN | _____ |
| Monthly Requests | _____ |
| Monthly Data Transfer | _____ GB |
| Primary Regions | _____________ |
| Security Integration | [ ] Yes [ ] No |
| Custom Cache Rules | [ ] Yes [ ] No |

Additional notes:

```text
_____________________________________________________________
_____________________________________________________________
```
