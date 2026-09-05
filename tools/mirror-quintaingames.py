"""Recopie le site Ramio RENDU (GitHub Pages / Jekyll) sous
quintaingames.com/ramio (dépôt Tristache/quintaingames, dossier local
Projects/quintaingames-site, sans Jekyll).

À lancer après chaque changement de ce dépôt, une fois la page rendue
par GitHub Pages (une à trois minutes après le push) :
    python tools/mirror-quintaingames.py
puis committer et pousser quintaingames-site.

Ce qui est recopié : les pages (index + langues + règles + politiques +
suppression), le CSS du thème, stats.html, version.json, les assets.
Les liens /ramio-site/ deviennent /ramio/, le pied de page du thème
devient « Quintain Games ». rejoindre.html n'est PAS touché (il vit dans
quintaingames-site/ramio/, copie de tristache.github.io/rejoindre.html).
"""
import os
import re
import shutil
import sys
import urllib.request

BASE = "https://tristache.github.io/ramio-site/"
SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.normpath(os.path.join(SRC, "..", "..", "quintaingames-site", "ramio"))

LANGUES = ["en", "es", "de", "it", "pt", "pl", "tr", "ro", "hu", "ar"]
PAGES = {"": "index.html"}
PAGES.update({l: f"{l}.html" for l in LANGUES})
PAGES.update({
    p: f"{p}.html"
    for p in [
        "regles-rami-chinois", "politique-confidentialite", "privacy-policy",
        "suppression-compte", "delete-account", "mentions-legales",
    ]
})


def get(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def adapte(html: str) -> str:
    html = html.replace("https://tristache.github.io/ramio-site/", "https://quintaingames.com/ramio/")
    html = html.replace("/ramio-site/", "/ramio/")
    html = html.replace('href="https://github.com/Tristache/ramio-site"', 'href="https://quintaingames.com/"')
    html = re.sub(
        r'<span class="site-footer-owner">.*?</span>',
        '<span class="site-footer-owner"><a href="https://quintaingames.com/">Quintain Games</a></span>',
        html, flags=re.S,
    )
    html = re.sub(r'<span class="site-footer-credits">.*?</span>', "", html, flags=re.S)
    return html


def main() -> int:
    os.makedirs(os.path.join(DST, "assets", "css"), exist_ok=True)
    for chemin, sortie in PAGES.items():
        try:
            html = get(BASE + chemin).decode("utf-8")
        except Exception as e:  # page pas encore rendue : on le dit, on continue
            print(f"  {sortie}: ABSENT ({e})")
            continue
        open(os.path.join(DST, sortie), "w", encoding="utf-8").write(adapte(html))
        print(f"  {sortie}: {len(html)} car.")
    open(os.path.join(DST, "assets", "css", "style.css"), "wb").write(get(BASE + "assets/css/style.css"))
    for f in os.listdir(os.path.join(SRC, "assets")):
        shutil.copy(os.path.join(SRC, "assets", f), os.path.join(DST, "assets", f))
    for f in ["stats.html", "version.json"]:
        shutil.copy(os.path.join(SRC, f), os.path.join(DST, f))
    print("miroir écrit dans", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
