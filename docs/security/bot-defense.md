# Bot Defense Sizing

F5 Distributed Cloud Bot Defense provides AI/ML-powered protection against automated threats including credential stuffing, account takeover, content scraping, and other bot attacks.

---

## Section 1: Bot Defense Requirements Assessment

### 1.1 Do You Need Bot Defense?

- [ ] Yes - We experience bot attacks or need proactive protection
- [ ] No - Skip this section
- [ ] Unsure - We need visibility into our bot traffic

### 1.2 Current Bot Challenges

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

```
_____________________________________________________________
_____________________________________________________________
```

---

## Section 2: Application Scope

### 2.1 Applications Requiring Bot Defense

Which applications need bot protection?

| Application/Domain | Critical Pages | Platform |
|-------------------|----------------|----------|
| _____________ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |
| _____________ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |
| _____________ | [ ] Login [ ] Registration [ ] Checkout [ ] Search | [ ] Web [ ] Mobile [ ] API |

### 2.2 FQDNs to Protect

List the fully qualified domain names requiring bot defense:

| FQDN | Environment |
|------|-------------|
| _____________ | [ ] Production [ ] Staging |
| _____________ | [ ] Production [ ] Staging |
| _____________ | [ ] Production [ ] Staging |
| _____________ | [ ] Production [ ] Staging |

!!! note "Standard Tier"
    Standard Bot Defense includes protection for 2 FQDNs. Additional FQDNs require add-ons.

### 2.3 Mobile Applications

Do you have mobile applications requiring bot protection?

- [ ] Yes - iOS applications
- [ ] Yes - Android applications
- [ ] Yes - Both iOS and Android
- [ ] No - Web only

If yes, provide mobile app details:

| App Name | Platform | Downloads (est.) |
|----------|----------|------------------|
| _____________ | [ ] iOS [ ] Android | _____________ |
| _____________ | [ ] iOS [ ] Android | _____________ |

---

## Section 3: Traffic Volume

### 3.1 Transaction Volume

Provide estimated transaction volumes:

| Metric | Daily Volume |
|--------|--------------|
| Total page views / transactions | _____ |
| Login attempts | _____ |
| Registration attempts | _____ |
| Checkout / purchase attempts | _____ |
| Search queries | _____ |
| API calls | _____ |

!!! note "Tier Entitlements"
    - Standard: Up to 500,000 transactions/day
    - Advanced: Up to 1,000,000 transactions/day
    - Additional capacity available as add-ons

### 3.2 Peak Traffic

| Metric | Peak Value | When |
|--------|------------|------|
| Peak transactions per day | _____ | _____________ |
| Peak transactions per hour | _____ | _____________ |
| Seasonal peaks (e.g., Black Friday) | _____ | _____________ |

### 3.3 Current Bot Traffic Estimate

What percentage of your traffic do you estimate is bot traffic?

- [ ] < 10%
- [ ] 10-25%
- [ ] 25-50%
- [ ] 50-75%
- [ ] > 75%
- [ ] Unknown - need visibility

---

## Section 4: Bot Defense Features

### 4.1 Detection Method

What level of bot detection do you need?

- [ ] **Signature-Based** (Standard) - Detect known bot frameworks and tools
- [ ] **Behavioral** (Advanced) - AI/ML analysis of device signals and behavior
- [ ] **Both** - Maximum protection

### 4.2 Mitigation Actions

What actions should be taken when bots are detected?

| Detection Confidence | Action |
|---------------------|--------|
| High confidence bot | [ ] Block [ ] Challenge [ ] Log only |
| Medium confidence bot | [ ] Block [ ] Challenge [ ] Log only |
| Low confidence bot | [ ] Block [ ] Challenge [ ] Log only |

Challenge types acceptable:
- [ ] JavaScript challenges
- [ ] CAPTCHA (as last resort)
- [ ] Custom challenge pages

### 4.3 Specific Bot Types to Address

Which automated threat categories are priorities?

| OWASP Automated Threat | Priority | Notes |
|----------------------|----------|-------|
| Credential Stuffing | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Account Takeover | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Carding | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Scraping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Scalping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Spamming | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Denial of Inventory | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |
| Sniping | [ ] Critical [ ] High [ ] Medium [ ] Low [ ] N/A | |

---

## Section 5: Integration Requirements

### 5.1 Deployment Method

How will Bot Defense be deployed?

- [ ] F5 XC as reverse proxy (traffic flows through F5)
- [ ] JavaScript tag injection only
- [ ] Both (recommended for full protection)

### 5.2 JavaScript Integration

For web applications, how will the Bot Defense JavaScript be injected?

- [ ] F5 XC automatic injection (proxy mode)
- [ ] Manual insertion in page templates
- [ ] Tag manager (Google Tag Manager, etc.)
- [ ] CDN-based injection

### 5.3 Mobile SDK Integration

For mobile applications, can you integrate the F5 Mobile SDK?

- [ ] Yes - We can add SDK to our mobile apps
- [ ] No - Mobile integration not possible
- [ ] N/A - No mobile applications

### 5.4 Existing Bot Solutions

Do you have existing bot management solutions?

| Solution | Replace or Integrate |
|----------|---------------------|
| _____________ | [ ] Replace [ ] Integrate |
| _____________ | [ ] Replace [ ] Integrate |

---

## Section 6: Advanced Features (Advanced Tier)

### 6.1 Device Fingerprinting

Do you need advanced device fingerprinting?

- [ ] Yes - Identify devices across sessions
- [ ] No

### 6.2 Content Scraping Protection

Do you need protection against content/data scraping?

- [ ] Yes - Protect proprietary content, pricing, inventory
- [ ] No

### 6.3 Managed Threat Intelligence

Do you need managed bot threat intelligence?

- [ ] Yes - 24x7 SOC monitoring for bot threats
- [ ] Yes - Custom detection rules developed by F5
- [ ] Yes - Regular threat briefings
- [ ] No - Self-service is sufficient

!!! warning "Advanced/Premium Tier"
    Managed threat intelligence requires Advanced or Premium tier.

---

## Section 7: Reporting and Analytics

### 7.1 Visibility Requirements

What bot visibility do you need?

- [ ] Real-time dashboard of bot activity
- [ ] Automated threat summaries (monthly)
- [ ] Detailed attack attribution
- [ ] Custom reports

### 7.2 Integration with SIEM/Analytics

Do you need to export bot defense data?

- [ ] Yes - Send to SIEM (Splunk, etc.)
- [ ] Yes - Send to data lake (S3, etc.)
- [ ] No - F5 console is sufficient

Target system: _________________

---

## Section 8: Geographic Distribution

### 8.1 Bot Engine Regions

Where do you need bot detection infrastructure?

| Region | Required |
|--------|----------|
| North America | [ ] Yes [ ] No |
| Europe | [ ] Yes [ ] No |
| Asia-Pacific | [ ] Yes [ ] No |
| South America | [ ] Yes [ ] No |

!!! note "Tier Entitlements"
    - Standard: 1 production region, 1 QA region
    - Advanced: 6 bot engines across regions
    - Premium: Unlimited bot engines

---

## Section 9: Support Requirements

### 9.1 Support Level

What level of bot defense support do you need?

- [ ] **Self-Service** - Manage bot policies yourself
- [ ] **Enhanced** - 24x7 support with named resources
- [ ] **Enhanced Plus** - Dedicated resources + managed service

### 9.2 Onboarding Support

Do you need assistance with initial deployment?

- [ ] Yes - Full onboarding support
- [ ] Yes - Integration assistance only
- [ ] No - Self-service deployment

---

## Summary: Bot Defense Requirements

| Requirement | Value |
|-------------|-------|
| Number of FQDNs | _____ |
| Estimated Daily Transactions | _____ |
| Mobile SDK Required | [ ] Yes [ ] No |
| Detection Method | [ ] Signature [ ] Behavioral [ ] Both |
| Tier Required | [ ] Standard [ ] Advanced [ ] Premium |
| Support Level | [ ] Self-Service [ ] Enhanced [ ] Enhanced Plus |

Primary bot threats to address:

```
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________
```

Additional notes or special requirements:

```
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```
