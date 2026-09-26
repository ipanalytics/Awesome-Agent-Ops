#!/usr/bin/env python3
"""Собирает README.md и README.ru.md из data/entries.json, data/tags.json и data/prose.json.

Правки вносить в данные, а не в README: README — собранный файл, и проверка каталога в CI
(`--check`) отвергнет пул-реквест, где они разъехались.

    python3 scripts/build_readme.py            # пересобрать файлы
    python3 scripts/build_readme.py --check    # только проверить, что файлы не отстали
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
WIDTH = 100
CONTENTS_EN = "## Contents"
CONTENTS_RU = "## Содержание"
TAGS_START = "<!-- tags:start -->"
TAGS_END = "<!-- tags:end -->"
HEADER_EN = (
    "# Awesome Agent Ops\n\n"
    "_Русская версия: [README.ru.md](README.ru.md)_\n\n"
    '<p align="center">\n  <img src="./site/banner.svg" alt="Awesome Agent Ops" width="100%">\n</p>\n'
)
HEADER_RU = (
    "# Awesome Agent Ops\n\n"
    "_English version: [README.md](README.md)_\n\n"
    '<p align="center">\n  <img src="./site/banner.svg" alt="Awesome Agent Ops" width="100%">\n</p>\n'
)


def load(name):
    import json

    return json.loads((DATA / name).read_text(encoding="utf-8"))


def wrap(text: str) -> str:
    return textwrap.fill(
        " ".join(text.split()),
        width=WIDTH,
        subsequent_indent="  ",
        break_long_words=False,
        break_on_hyphens=False,
    )


def anchor(text: str) -> str:
    """Якорь как у GitHub: строчные, знаки препинания выброшены, пробелы в дефисы."""
    keep = [ch for ch in text.lower() if ch.isalnum() or ch in " -"]
    return "".join(keep).replace(" ", "-")


def entry_row(entry: dict, field: str) -> str:
    """Заголовок со ссылкой не переносим: перенос внутри markdown-ссылки ломает её вид."""
    head = f"- **[{entry[f'title_{field}']}]({entry['url']})**"
    tail = f"— {entry[f'text_{field}']}"
    if entry["tags"]:
        tail += " *(" + ", ".join(entry["tags"]) + ")*"
    return head + " " + wrap(tail)


def body_head(prose: dict, header: str) -> str:
    """Шапка: заглавие и ссылка на второй язык — канонические, остальное из прозы."""
    lines = []
    for line in prose["head"].splitlines():
        stripped = line.strip()
        if stripped.startswith(("# ", "_")) or stripped == "---":
            continue
        lines.append(line.rstrip())
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return header + "\n" + "\n".join(lines) + "\n"


def contents(categories: list, field: str, heading: str) -> str:
    key = f"title_{field}"
    lines = [heading, ""]
    for index, category in enumerate(categories, start=1):
        lines.append(f"{index}. [{category[key]}](#{index}-{anchor(category[key])})")
    return "\n".join(lines) + "\n"


def section(index: int, category: dict, entries: list, field: str) -> str:
    lines = [f"## {index}. {category[f'title_{field}']}", ""]
    for entry in entries:
        lines.append(entry_row(entry, field))
        lines.append("")
    return "\n".join(lines)


def tail(prose: dict) -> str:
    chunks = []
    for heading, text in prose["tail"].items():
        chunks.append(f"## {heading}\n\n{text.strip()}\n")
    return "\n".join(chunks)


def render(entries_doc: dict, prose: dict, lang: str) -> str:
    field = lang
    header = HEADER_EN if lang == "en" else HEADER_RU
    heading = CONTENTS_EN if lang == "en" else CONTENTS_RU
    parts = [body_head(prose, header)]
    categories = entries_doc["categories"]
    parts.append(contents(categories, field, heading))
    for index, category in enumerate(categories, start=1):
        rows = [e for e in entries_doc["entries"] if e["category"] == category["id"]]
        parts.append(section(index, category, rows, field))
    parts.append(tail(prose))
    return "\n".join(parts).rstrip() + "\n"


def tags_table(tags_doc: dict) -> str:
    axis = tags_doc["axes"]["topic"]
    lines = ["| Значение | Что означает |", "| --- | --- |"]
    for value in sorted(axis["values"].values(), key=lambda item: item["label"]):
        lines.append(f"| `{value['label']}` | {value['definition']} |")
    return "\n".join(lines)


def update_tags_table(text: str, table: str) -> str:
    if TAGS_START not in text or TAGS_END not in text:
        return text
    head, _, rest = text.partition(TAGS_START)
    _, _, after = rest.partition(TAGS_END)
    return f"{head}{TAGS_START}\n{table}\n{TAGS_END}{after}"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Собрать README.md и README.ru.md из данных каталога.")
    parser.add_argument("--check", action="store_true", help="только проверить, что файлы не отстали от данных")
    args = parser.parse_args(argv)
    entries_doc, tags_doc, prose_doc = load("entries.json"), load("tags.json"), load("prose.json")
    stale = []
    for lang in ("en", "ru"):
        path = ROOT / ("README.md" if lang == "en" else "README.ru.md")
        rendered = render(entries_doc, prose_doc[lang], lang)
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if rendered == current:
            continue
        if args.check:
            stale.append(path.name)
        else:
            path.write_text(rendered, encoding="utf-8")
            print(f"собран {path.name}: {len(rendered)} символов")
    contributing = ROOT / "CONTRIBUTING.md"
    if contributing.exists():
        text = contributing.read_text(encoding="utf-8")
        updated = update_tags_table(text, tags_table(tags_doc))
        if updated != text:
            if args.check:
                stale.append(contributing.name)
            else:
                contributing.write_text(updated, encoding="utf-8")
                print("обновлена таблица словаря в CONTRIBUTING.md")
    if stale:
        print(f"отстали от данных: {', '.join(sorted(stale))}", file=sys.stderr)
        print("запустите: python3 scripts/build_readme.py", file=sys.stderr)
        return 1
    if args.check:
        print("README и словарь совпадают с данными")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
