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

## Offline package (0.2.1)
- 80 bundled rule groups; no network, no API key, no upload
- wheel: GitHub Releases（PyPI 上传待账号）
- `pip install` 将从 PyPI 提供；当前可用 `git clone` + `PYTHONPATH` 或 GitHub Release wheel

## Contact
- 免费邮件自查：`hello@wanhetools.top`（贴文案，自动回命中词+法条+规则ID；免费、不承诺交付）

## Rules
`rules()` returns the machine-readable rule catalog (80 groups; Chinese groups cite PRC Advertising Law article numbers).

## Benchmark pages (original data)
- 2026 ad-law benchmark: https://wh-bi.github.io/wanhe-compliance/
- Medical/beauty test: https://wh-bi.github.io/wanhe-compliance/medical-beauty-2026.html
- Negative cases: https://wh-bi.github.io/wanhe-compliance/negative-cases-2026.html

## Links
- Pages: https://wh-bi.github.io/wanhe-compliance/
- Contact: hello@wanhetools.top

## Notes
- Technical checks only; not legal advice.
- No personal data is collected by this SDK; the API may log a salted IP hash for rate limiting.
- License: MIT
