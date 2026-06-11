#!/usr/bin/env python3
"""
Lee el bloque <!-- profile-excerpt -->...<!-- /profile-excerpt --> de cada repo
y lo inyecta en el README del perfil entre los marcadores correspondientes.
"""
import re
import os
import base64
import json
import urllib.request
import urllib.error

OWNER = "PandaAkiraNakai"

# Repos a sincronizar: nombre del repo tal como aparece en GitHub
REPOS = [
    "PandaControl",
    "Cerebro-Virtual-Ciberseguridad",
    "DerivaShield",
    "Bots-Telegram",
    "mem-cli",
    "dotfiles",
    "niri-bootstrap",
    "starship-cyberpunk-preset",
    "gamescope-auto",
    "gamdl-portable",
    "Cerebro-Virtual-Ciencias",
    "Cerebro-Virtual-3DS",
    "obsidian-quartz-publish",
    "Tetris",
]


def get_readme(repo: str, token: str) -> str:
    url = f"https://api.github.com/repos/{OWNER}/{repo}/contents/README.md"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    return base64.b64decode(data["content"]).decode("utf-8")


def extract_excerpt(content: str) -> str | None:
    m = re.search(
        r"<!-- profile-excerpt -->\n(.*?)\n<!-- /profile-excerpt -->",
        content,
        re.DOTALL,
    )
    if not m:
        return None
    text = m.group(1).strip()
    # Estilo limpio: quitar sufijo tipo `// foo · bar` y dejar una sola línea
    text = re.sub(r"\s*`//[^`]*`\s*$", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def inject_excerpt(profile: str, repo: str, excerpt: str) -> str:
    pattern = (
        rf"(<!-- excerpt:{re.escape(repo)} -->)"
        rf".*?"
        rf"(<!-- /excerpt:{re.escape(repo)} -->)"
    )
    replacement = rf"\1{excerpt}\2"
    return re.sub(pattern, replacement, profile, flags=re.DOTALL)


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise SystemExit("GITHUB_TOKEN no definido")

    with open("README.md", "r", encoding="utf-8") as f:
        profile = f.read()

    changed = False
    for repo in REPOS:
        try:
            readme = get_readme(repo, token)
            excerpt = extract_excerpt(readme)
            if not excerpt:
                print(f"[SKIP] {repo}: no se encontró bloque profile-excerpt")
                continue
            updated = inject_excerpt(profile, repo, excerpt)
            if updated != profile:
                profile = updated
                changed = True
                print(f"[OK] {repo}: excerpt actualizado")
            else:
                print(f"[=] {repo}: sin cambios")
        except urllib.error.HTTPError as e:
            print(f"[ERR] {repo}: HTTP {e.code}")
        except Exception as e:
            print(f"[ERR] {repo}: {e}")

    if changed:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(profile)
        print("README.md actualizado.")
    else:
        print("Sin cambios.")


if __name__ == "__main__":
    main()
