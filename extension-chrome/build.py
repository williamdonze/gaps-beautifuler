#!/usr/bin/env python3
"""Construit l'extension Chrome (et Edge, Brave, Opera…) à partir du style UserCSS.

  python3 build.py

Même CSS et même logo que l'extension Firefox (../extension-firefox) :
- src/gaps.css      : le CSS de ../gaps-heig-moderne.css, sans l'enveloppe @-moz-document.
- src/manifest.json : Manifest V3 ; la version reprend le @version du UserCSS.
- src/icons/        : icônes tirées de ../extension-firefox/logo.png.
- gaps-beautifuler-chrome.zip : l'archive à envoyer au Chrome Web Store.
"""
import importlib.util
import json
import re
import zipfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
SRC = ICI / "src"
FIREFOX = ICI.parent / "extension-firefox"
ZIP = ICI / "gaps-beautifuler-chrome.zip"

spec = importlib.util.spec_from_file_location("build_firefox", FIREFOX / "build.py")
ff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ff)


def main():
    texte = ff.USERCSS.read_text(encoding="utf-8")
    version = re.search(r"@version\s+([\d.]+)", texte).group(1)
    (SRC / "gaps.css").write_text(ff.css_sans_enveloppe(texte), encoding="utf-8")

    manifeste = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    manifeste["version"] = version
    manifeste["content_scripts"][0]["matches"] = ff.adresses(texte)
    (SRC / "manifest.json").write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ff.SRC = SRC  # mêmes icônes que Firefox, écrites dans src/icons/
    ff.icones()
    (SRC / "icons" / "icon-96.png").unlink(missing_ok=True)  # inutile pour Chrome

    ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SRC.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(SRC).as_posix())
    print(f"{ZIP.name} : version {version}, {ZIP.stat().st_size // 1024} Ko")


if __name__ == "__main__":
    main()
