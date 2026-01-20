import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LEGACY_RE = re.compile(r"^\ufeff?<!--\s*\n(.*?)\n-->\s*\n*", re.DOTALL)


def convert_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")

    stripped = content.lstrip("\ufeff")
    if stripped.startswith("---\n") or stripped.startswith("---\r\n"):
        return False

    match = LEGACY_RE.match(content)
    if not match:
        return False

    yaml_block = match.group(1).strip()
    if not yaml_block:
        return False

    rest = content[match.end() :].lstrip("\r\n")
    new_content = f"---\n{yaml_block}\n---\n\n{rest}"
    path.write_text(new_content, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for md in ROOT.rglob("*.md"):
        if convert_file(md):
            changed += 1
            print(f"converted: {md.relative_to(ROOT)}")
    print(f"done. converted {changed} file(s).")


if __name__ == "__main__":
    main()

