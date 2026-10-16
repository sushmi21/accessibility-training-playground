#!/usr/bin/env python3
"""Generate accessible/index.html and broken/index.html from src/template.html.

The template carries both versions. Block markers keep one branch:
    <!--IF BROKEN--> ... <!--ELSE--> ... <!--ENDIF-->      (HTML)
    /*IF BROKEN*/ ... /*ELSE*/ ... /*ENDIF*/              (CSS and JS)
Inline markers choose an attribute or a fragment:
    {{broken:aria-label="Close"|accessible:}}
Run:  python3 build.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
TEMPLATE = ROOT / "src" / "template.html"

BLOCK = re.compile(
    r"(?:<!--|/\*)\s*IF BROKEN\s*(?:-->|\*/)(.*?)"
    r"(?:(?:<!--|/\*)\s*ELSE\s*(?:-->|\*/)(.*?))?"
    r"(?:<!--|/\*)\s*ENDIF\s*(?:-->|\*/)",
    re.S,
)
INLINE = re.compile(r"\{\{broken:(.*?)\|accessible:(.*?)\}\}")
NOTE = "<!-- Generated from src/template.html by build.py; edit the template, not this file. -->\n"


def build(source: str, broken: bool) -> str:
    out = BLOCK.sub(lambda m: (m.group(1) if broken else (m.group(2) or "")), source)
    out = INLINE.sub(lambda m: m.group(1) if broken else m.group(2), out)
    out = re.sub(r"(<[a-zA-Z][^<>]*?)[ \t]+>", r"\1>", out)  # tidy "<tag attr >"
    out = re.sub(r"(<[a-zA-Z][^<>]*?)[ \t]{2,}", r"\1 ", out)  # tidy doubled spaces in tags
    out = re.sub(r"\n(?:[ \t]*\n){2,}", "\n\n", out)  # collapse runs of blank lines
    out = re.sub(r"\n[ \t]*\n(?=[ \t]*(?:</?(?:dialog|div|form|script)|\}))", "\n", out)
    return out.replace("<!doctype html>\n", "<!doctype html>\n" + NOTE, 1)


def main() -> None:
    source = TEMPLATE.read_text(encoding="utf-8")
    for name, broken in (("accessible", False), ("broken", True)):
        target = ROOT / name
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(build(source, broken), encoding="utf-8")
        print(f"wrote {name}/index.html")


if __name__ == "__main__":
    main()
