# Bot Defense Sizing

F5 Distributed Cloud Bot Defense provides AI/ML-powered protection against
automated threats including credential stuffing, account takeover, content
scraping, and other bot attacks.

---

## Bot Defense Requirements Assessment

### Current Bot Challenges

What bot-related challenges are you experiencing?

- [ ] Credential stuffing attacks
- [ ] Account takeover (ATO)
- [ ] Content scraping / price scraping
- [ ] Inventory hoarding / scalping
- [ ] Gift card fraud
- [ ] Fake account creation
- [ ] Spam / form abuse
- [ ] Ad fraud / click fraud
- [ ] API abuse by bots
- [ ] Competitive intelligence bots
- [ ] None currently, but want proactive protection

Describe specific bot challenges:

```text
___
```

---

## Application Scope

### Applications Requiring Bot Defense

Which applications need bot protection?

| Application/Domain | Critical Pages | Platform |
| --- | --- | --- |
| ___ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |
| ___ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |
| ___ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |

### FQDNs to Protect

List the fully qualified domain names requiring bot defense:

| FQDN | Environment |
| --- | --- |
| ___ | [ ] Production [ ] Staging |
| ___ | [ ] Production [ ] Staging |
| ___ | [ ] Production [ ] Staging |
| ___ | [ ] Production [ ] Staging |

!!! note "Standard Tier"
    Standard Bot Defense includes protection for 2 FQDNs. Additional FQDNs
    require add-ons.

### Mobile Applications

Do you have mobile applications requiring bot protection?

- [ ] Yes - iOS applications
- [ ] Yes - Android applications
- [ ] Yes - Both iOS and Android
- [ ] No - Web only

If yes, provide mobile app details:

| App Name | Platform | Downloads (est.) |
| --- | --- | --- |
| ___ | [ ] iOS [ ] Android | ___ |
| ___ | [ ] iOS [ ] Android | ___ |

---

## Traffic Volume

### Transaction Volume

Provide estimated transaction volumes:

| Metric | Daily Volume |
| --- | --- |
| Total page views / transactions | ___ |
| Login attempts | ___ |
| Registration attempts | ___ |
| Checkout / purchase attempts | ___ |
| Search queries | ___ |
| API calls | ___ |

!!! note "Tier Entitlements"
    - Standard: Up to 500,000 transactions/day
    - Advanced: Up to 1,000,000 transactions/day
    - Additional capacity available as add-ons

### Peak Traffic

| Metric | Peak Value | When |
| --- | --- | --- |
| Peak transactions per day | ___ | ___ |
| Peak transactions per hour | ___ | ___ |
| Seasonal peaks (e.g., Black Friday) | ___ | ___ |

### Current Bot Traffic Estimate

What percentage of your traffic do you estimate is bot traffic?

- [ ] < 10%
- [ ] 10-25%
- [ ] 25-50%
- [ ] 50-75%
- [ ] > 75%
- [ ] Unknown - need visibility

---

## Bot Defense Features

### Detection Method

What level of bot detection do you need?

- [ ] **Signature-Based** (Standard) - Detect known bot frameworks and tools
- [ ] **Behavioral** (Advanced) - AI/ML analysis of device signals and behavior
- [ ] **Both** - Maximum protection

### Mitigation Actions

What actions should be taken when bots are detected?

| Detection Confidence | Action |
| --- | --- |
| High confidence bot | [ ] Block [ ] Challenge [ ] Log only |
| Medium confidence bot | [ ] Block [ ] Challenge [ ] Log only |
| Low confidence bot | [ ] Block [ ] Challenge [ ] Log only |

Challenge types acceptable:

- [ ] JavaScript challenges
- [ ] CAPTCHA (as last resort)
- [ ] Custom challenge pages

### Specific Bot Types to Address

Which automated threat categories are priorities?

| OWASP Automated Threat | Priority | Notes |
| --- | --- | --- |
| Credential Stuffing | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Account Takeover | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Carding | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Scraping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Scalping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Spamming | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Denial of Inventory | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |
| Sniping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | ___ |

---

## Integration Requirements

### Deployment Method

How will Bot Defense be deployed?

- [ ] F5 XC as reverse proxy (traffic flows through F5)
- [ ] JavaScript tag injection only
- [ ] Both (recommended for full protection)

### JavaScript Integration

For web applications, how will the Bot Defense JavaScript be injected?

- [ ] F5 XC automatic injection (proxy mode)
- [ ] Manual insertion in page templates
- [ ] Tag manager (Google Tag Manager, etc.)
- [ ] CDN-based injection

### Mobile SDK Integration

For mobile applications, can you integrate the F5 Mobile SDK?

- [ ] Yes - We can add SDK to our mobile apps
- [ ] No - Mobile integration not possible
- [ ] N/A - No mobile applications

### Existing Bot Solutions

Do you have existing bot management solutions?

| Solution | Replace or Integrate |
| --- | --- |
| ___ | [ ] Replace [ ] Integrate |
| ___ | [ ] Replace [ ] Integrate |

---

## Advanced Features (Advanced Tier)

### Device Fingerprinting

- [ ] Yes - Identify devices across sessions
- [ ] No

### Content Scraping Protection

- [ ] Yes - Protect proprietary content, pricing, inventory
- [ ] No

### Managed Threat Intelligence

- [ ] Yes - 24x7 SOC monitoring for bot threats
- [ ] Yes - Custom detection rules developed by F5
- [ ] Yes - Regular threat briefings
- [ ] No - Self-service is sufficient

!!! warning "Advanced/Premium Tier"
    Managed threat intelligence requires Advanced or Premium tier.

---

## Reporting and Analytics

### Visibility Requirements

What bot visibility do you need?

- [ ] Real-time dashboard of bot activity
- [ ] Automated threat summaries (monthly)
- [ ] Detailed attack attribution
- [ ] Custom reports

### Integration with SIEM/Analytics

- [ ] Yes - Send to SIEM (Splunk, etc.)
- [ ] Yes - Send to data lake (S3, etc.)
- [ ] No - F5 console is sufficient

Target system: ___

---

## Geographic Distribution

### Bot Engine Regions

Where do you need bot detection infrastructure?

| Region | Required |
| --- | --- |
| North America | [ ] Yes [ ] No |
| Europe | [ ] Yes [ ] No |
| Asia-Pacific | [ ] Yes [ ] No |
| South America | [ ] Yes [ ] No |

!!! note "Tier Entitlements"
    - Standard: 1 production region, 1 QA region
    - Advanced: 6 bot engines across regions
    - Premium: Unlimited bot engines

---

## Support Requirements

### Support Level

What level of bot defense support do you need?

- [ ] **Self-Service** - Manage bot policies yourself
- [ ] **Enhanced** - 24x7 support with named resources
- [ ] **Enhanced Plus** - Dedicated resources + managed service

### Onboarding Support

- [ ] Yes - Full onboarding support
- [ ] Yes - Integration assistance only
- [ ] No - Self-service deployment

---

## Summary: Bot Defense Requirements

| Requirement | Value |
| --- | --- |
| Number of FQDNs | ___ |
| Estimated Daily Transactions | ___ |
| Mobile SDK Required | [ ] Yes [ ] No |
| Detection Method | [ ] Signature [ ] Behavioral [ ] Both |
| Tier Required | [ ] Standard [ ] Advanced [ ] Premium |
| Support Level | [ ] Self-Service [ ] Enhanced [ ] Enhanced Plus |

Primary bot threats to address:

```text
1. ___
2. ___
3. ___
```

Additional notes or special requirements:

```text
___
```
