"""CLI for wanhe-compliance."""
import argparse
import json
import sys

from . import check, rules, health


def main() -> int:
    p = argparse.ArgumentParser(prog="wanhe-compliance", description="Chinese ad-law / AI-labeling checks")
    sub = p.add_subparsers(dest="cmd")
    c = sub.add_parser("check", help="check text")
    c.add_argument("text", nargs="?", help="text to check; omit to read stdin")
    sub.add_parser("rules", help="print rule catalog")
    sub.add_parser("health", help="health check")
    args = p.parse_args()
    try:
        if args.cmd == "check":
            text = args.text if args.text is not None else sys.stdin.read()
            print(json.dumps(check(text), ensure_ascii=False, indent=2))
        elif args.cmd == "rules":
            print(json.dumps(rules(), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(health(), ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
