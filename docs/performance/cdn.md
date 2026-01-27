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
- [ ] Other: ___

---

## Content Profile

### Content Types

What content will be cached?

| Content Type | Percentage | Cache TTL |
| --- | --- | --- |
| Static images (jpg, png, gif, svg) | ___ % | ___ hours |
| JavaScript / CSS | ___ % | ___ hours |
| Video / Media files | ___ % | ___ hours |
| HTML pages | ___ % | ___ hours |
| API responses | ___ % | ___ seconds |
| Documents (PDF, etc.) | ___ % | ___ hours |
| Other: ___ | ___ % | ___ |

### Content Size

| Metric | Value |
| --- | --- |
| Total unique content size | ___ GB/TB |
| Average object size | ___ KB |
| Largest object size | ___ MB |
| Total number of unique objects | ___ |

### Content Origin

Where is your origin content hosted?

| Origin Location | Provider | Percentage |
| --- | --- | --- |
| ___ | [ ] AWS [ ] Azure [ ] GCP [ ] On-Prem [ ] Other | ___ % |
| ___ | [ ] AWS [ ] Azure [ ] GCP [ ] On-Prem [ ] Other | ___ % |

---

## Traffic Volume

### Request Metrics

| Metric | Average | Peak |
| --- | --- | --- |
| Requests per second | ___ | ___ |
| Requests per month | ___ | ___ |
| Bandwidth (Gbps) | ___ | ___ |

### Regional Distribution

Where are your users located?

| Region | Traffic Percentage |
| --- | --- |
| North America | ___ % |
| Europe | ___ % |
| Asia-Pacific | ___ % |
| South America | ___ % |
| Other | ___ % |

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
- [ ] Specific headers: ___
- [ ] Cookies: ___

### Cache Purge Requirements

How will you purge cached content?

- [ ] Manual purge via console
- [ ] API-based purge
- [ ] Tag-based purge
- [ ] Path-based purge
- [ ] Full cache purge

Estimated purge frequency: ___ per day/week

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
| /api/* | [ ] Cache [ ] Bypass | ___ |
| /static/* | [ ] Cache [ ] Bypass | ___ |
| *.css | [ ] Cache [ ] Bypass | ___ |
| ___ | [ ] Cache [ ] Bypass | ___ |

---

## Performance Metrics

### Expected Cache Performance

| Metric | Target |
| --- | --- |
| Target cache hit ratio | > ___ % |
| Target TTFB from edge | < ___ ms |
| Acceptable origin load reduction | ___ % |

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
| Domains to CDN | ___ |
| Monthly Requests | ___ |
| Monthly Data Transfer | ___ GB |
| Primary Regions | ___ |
| Security Integration | [ ] Yes [ ] No |
| Custom Cache Rules | [ ] Yes [ ] No |

Additional notes:

```text
___
```
