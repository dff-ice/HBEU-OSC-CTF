"""Generate the WP listing consumed by docs/sidebar/writeups.html."""

import json
import logging
import posixpath
import re
from pathlib import Path

import yaml


LOGGER = logging.getLogger("mkdocs.plugins.writeups")
FRONT_MATTER = re.compile(r"\A\ufeff?---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)


def _plain_text(value):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(value or ""))
    return re.sub(r"[`*_~]", "", text).strip()


def _summary(body, metadata):
    description = metadata.get("description")
    if description:
        return _plain_text(description)[:220]

    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", ">", "- ", "* ", "```", "|", "---")):
            continue
        summary = _plain_text(line)
        if summary:
            return summary[:220]
    return ""


def _page_url(source, docs_dir, use_directory_urls):
    relative = source.relative_to(docs_dir).with_suffix("")
    if relative.name.lower() == "index":
        relative = relative.parent

    route = relative.as_posix().strip("/")
    if use_directory_urls:
        route += "/"
    else:
        route += ".html"
    url = posixpath.relpath(route, start="sidebar")
    return url.rstrip("/") + "/" if use_directory_urls else url


def on_post_build(config):
    """Write site/hc-writeup/writeups.json after MkDocs copies the docs tree."""
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    writeup_root = docs_dir / "hc-writeup"
    posts = []

    for source in sorted(writeup_root.rglob("*.md")):
        try:
            text = source.read_text(encoding="utf-8-sig")
            match = FRONT_MATTER.match(text)
            if not match:
                continue
            metadata = yaml.safe_load(match.group(1)) or {}
        except (OSError, yaml.YAMLError) as error:
            LOGGER.warning("Skipping WP metadata in %s: %s", source, error)
            continue

        if not isinstance(metadata, dict) or metadata.get("type") != "writeup":
            continue

        authors = metadata.get("authors", metadata.get("author", []))
        if isinstance(authors, (str, int, float)):
            authors = [authors]
        author = ", ".join(str(item) for item in authors or [])
        date = metadata.get("date", "")

        posts.append(
            {
                "title": str(metadata.get("title") or source.stem),
                "competition": str(metadata.get("competition", "")),
                "category": str(metadata.get("category", "")),
                "author": author,
                "date": date.isoformat() if hasattr(date, "isoformat") else str(date),
                "summary": _summary(text[match.end() :], metadata),
                "url": _page_url(source, docs_dir, config["use_directory_urls"]),
            }
        )

    posts.sort(key=lambda post: post["date"], reverse=True)
    output = site_dir / "hc-writeup" / "writeups.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps({"writeups": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    LOGGER.info("Generated WP index: %s entries", len(posts))
