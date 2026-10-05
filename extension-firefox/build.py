#!/usr/bin/env python3
"""Construit l'extension Firefox à partir du style UserCSS.

  python3 build.py

- src/gaps.css      : le CSS de ../gaps-heig-moderne.css, sans l'enveloppe
                      @-moz-document (Firefox ne l'accepte plus hors Stylus).
- src/manifest.json : la version reprend le @version du UserCSS.
- src/icons/        : icônes tirées de logo.png s'il existe, sinon générées.
- gaps-beautifuler.xpi : l'archive à installer.
"""
import json
import re
import zipfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
SRC = ICI / "src"
USERCSS = ICI.parent / "gaps-heig-moderne.css"
XPI = ICI / "gaps-beautifuler.xpi"
# ton logo (carré de préférence) : logo.png, .jpg, .jpeg ou .webp ; sinon icône générée
LOGO = next((ICI / f"logo.{e}" for e in ("png", "jpg", "jpeg", "webp") if (ICI / f"logo.{e}").exists()), ICI / "logo.png")


def css_sans_enveloppe(texte):
    m = re.search(r'@-moz-document\s+domain\("gaps\.heig-vd\.ch"\)\s*\{', texte)
    if not m:
        raise SystemExit("Enveloppe @-moz-document introuvable dans le UserCSS")
    fin = texte.rstrip().rfind("}")
    corps = texte[m.end():fin].strip("\n")
    entete = texte[:m.start()].strip()
    return f"{entete}\n\n/* Généré par extension-firefox/build.py depuis gaps-heig-moderne.css */\n\n{corps}\n"


def icones():
    from PIL import Image, ImageDraw, ImageFont
    (SRC / "icons").mkdir(parents=True, exist_ok=True)
    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        cote = max(logo.size)  # centré sur un carré transparent, sans déformation
        carre = Image.new("RGBA", (cote, cote), (0, 0, 0, 0))
        carre.paste(logo, ((cote - logo.width) // 2, (cote - logo.height) // 2))
        for taille in (16, 32, 48, 96, 128):
            carre.resize((taille, taille), Image.LANCZOS).save(SRC / "icons" / f"icon-{taille}.png")
        return
    police = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    for taille in (16, 32, 48, 96, 128):
        k = 8  # suréchantillonnage pour des bords nets
        t = taille * k
        im = Image.new("RGBA", (t, t), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, t - 1, t - 1), radius=int(t * 0.22), fill=(225, 37, 27, 255))
        f = ImageFont.truetype(police, int(t * 0.62))
        d.text((t / 2, t / 2 + t * 0.02), "G", font=f, fill=(255, 255, 255, 255), anchor="mm")
        im.resize((taille, taille), Image.LANCZOS).save(SRC / "icons" / f"icon-{taille}.png")


def main():
    texte = USERCSS.read_text(encoding="utf-8")
    version = re.search(r"@version\s+([\d.]+)", texte).group(1)
    SRC.mkdir(exist_ok=True)
    (SRC / "gaps.css").write_text(css_sans_enveloppe(texte), encoding="utf-8")

    manifeste = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    manifeste["version"] = version
    (SRC / "manifest.json").write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    icones()

    XPI.unlink(missing_ok=True)
    with zipfile.ZipFile(XPI, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SRC.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(SRC).as_posix())
    print(f"{XPI.name} : version {version}, {XPI.stat().st_size // 1024} Ko")


if __name__ == "__main__":
    main()
