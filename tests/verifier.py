"""Vérifie le kit : chaque skill a un en-tête valide, et le README pointe vers des fichiers qui existent.

Usage : python tests/verifier.py   (code de sortie 0 si tout va bien)
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
erreurs = []

skills = sorted(p for p in (RACINE / "skills").iterdir() if p.is_dir())
if not skills:
    erreurs.append("aucun skill trouvé dans skills/")

for dossier in skills:
    fichier = dossier / "SKILL.md"
    if not fichier.is_file():
        erreurs.append(f"{dossier.name} : SKILL.md manquant")
        continue
    texte = fichier.read_text(encoding="utf-8")
    entete = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", texte, re.S)
    if not entete:
        erreurs.append(f"{dossier.name} : en-tête absent")
        continue
    champs = dict(l.split(": ", 1) for l in entete.group(1).splitlines() if ": " in l)
    if champs.get("name") != dossier.name:
        erreurs.append(f"{dossier.name} : le nom de l'en-tête ne correspond pas au dossier")
    description = champs.get("description", "").strip()
    if not description:
        erreurs.append(f"{dossier.name} : description vide")
    elif len(description) > 1024:
        erreurs.append(f"{dossier.name} : description trop longue ({len(description)} caractères)")
    if not re.match(r"^[a-z0-9-]+$", dossier.name):
        erreurs.append(f"{dossier.name} : le nom ne doit contenir que des minuscules, chiffres et tirets")

readme = (RACINE / "README.md").read_text(encoding="utf-8")
for lien in re.findall(r"\]\((skills/[^)]+)\)", readme):
    if not (RACINE / lien).is_file():
        erreurs.append(f"README : lien cassé vers {lien}")
for dossier in skills:
    if f"skills/{dossier.name}/SKILL.md" not in readme:
        erreurs.append(f"README : {dossier.name} n'est pas présenté")

if erreurs:
    print("\n".join("ÉCHEC  " + e for e in erreurs))
    sys.exit(1)
print(f"OK  {len(skills)} skills valides, README cohérent.")
