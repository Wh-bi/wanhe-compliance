# wanhe-compliance

Chinese advertising-law & AI-labeling compliance checks with statutory citations — Python client for the Wanhe Compliance API.

> Status: the public site is temporarily unavailable pending ICP filing (HTTP 403). The SDK is ready; calls will work once access is restored.

## Install

```bash
pip install wanhe-compliance
```

## Use

```python
from wanhe_compliance import check
print(check("本产品全网最好，100%有效"))
```

```bash
wanhe-compliance check "本产品全网最好，100%有效"
```

## Free tier
- 2,000 characters per request
- 30 requests per hour per IP
- No signup required for the free tier

## Rules
`rules()` returns the machine-readable rule catalog (80 groups; Chinese groups cite PRC Advertising Law article numbers).

## Links
- Docs / OpenAPI: https://wanhetools.top/openapi.json
- Site: https://wanhetools.top

## Notes
- Technical checks only; not legal advice.
- No personal data is collected by this SDK; the API may log a salted IP hash for rate limiting.
- License: MIT
