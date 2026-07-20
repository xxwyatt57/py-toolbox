"""
minimal urlencode for cases where i don't want to import urllib.parse
and can accept the readability tradeoff.
"""

_SAFE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789-._~")


def encode(s: str) -> str:
    out = []
    for c in s:
        if c in _SAFE:
            out.append(c)
        else:
            for b in c.encode("utf-8"):
                out.append(f"%{b:02X}")
    return "".join(out)


if __name__ == "__main__":
    print(encode("hello world / ~foo"))
