"""Wanhe Compliance SDK — Chinese advertising-law & AI-labeling checks.

Free tier available; see README. Note: the public site is temporarily
unavailable pending ICP filing; the SDK will surface HTTP errors as-is.
"""
from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

__version__ = "0.1.0"
BASE_URL = os.environ.get("WANHE_BASE_URL", "https://wanhetools.top")


def _post(path: str, payload: Dict[str, Any], timeout: int = 30) -> Dict[str, Any]:
    url = BASE_URL.rstrip("/") + path
    r = requests.post(url, json=payload, timeout=timeout,
                      headers={"User-Agent": "wanhe-compliance-sdk/" + __version__})
    r.raise_for_status()
    return r.json()


def check(text: str, checks: Optional[list] = None, timeout: int = 30) -> Dict[str, Any]:
    """Check Chinese content for advertising-law / AI-labeling risks.

    >>> check("本产品全网最好，100%有效")
    {'ok': True, 'issues': [...]}
    """
    payload: Dict[str, Any] = {"text": text}
    if checks:
        payload["check"] = checks
    return _post("/api/v1/check", payload, timeout=timeout)


def rules(timeout: int = 30) -> Dict[str, Any]:
    """Return the machine-readable rule catalog (groups + locales)."""
    url = BASE_URL.rstrip("/") + "/api/v1/rules"
    r = requests.get(url, timeout=timeout,
                     headers={"User-Agent": "wanhe-compliance-sdk/" + __version__})
    r.raise_for_status()
    return r.json()


def health(timeout: int = 15) -> Dict[str, Any]:
    url = BASE_URL.rstrip("/") + "/api/v1/health"
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.json()
