---
name: garde-fou
description: Met en place, avec l'accord de l'utilisateur, un garde-fou automatique (un hook) dans Claude Code : bloquer les suppressions de fichiers, prévenir par une notification quand Claude attend une réponse. À utiliser quand l'utilisateur veut protéger ses fichiers, être prévenu, ou demande « installe un garde-fou ». Ne se lance jamais seul.
disable-model-invocation: true
---

# Garde-fou

Un garde-fou est une règle que l'application applique à chaque fois, contrairement à une consigne que Claude peut oublier. Il s'installe dans les réglages de Claude Code.

## Avant tout
1. Expliquer en trois phrases, sans jargon, ce qu'est un garde-fou et ce que l'on va installer.
2. Demander lequel l'utilisateur veut :
   - **Pas de suppression** : bloquer toute commande qui supprime des fichiers ou des dossiers ;
   - **Prévenir** : une notification de l'ordinateur quand Claude attend une réponse ;
   - les deux.
3. Demander s'il doit valoir **partout** (réglages personnels) ou **dans ce projet seulement**.

## Installation
- Lire la documentation officielle des hooks de Claude Code avant d'écrire quoi que ce soit, et suivre son format actuel.
- Adapter les commandes au système de l'utilisateur (Windows, macOS ou Linux).
- Ajouter le garde-fou sans effacer les réglages existants : relire le fichier de réglages, ajouter, montrer la différence à l'utilisateur, et n'enregistrer qu'après son accord.

## Vérification
- Faire un essai sans risque devant l'utilisateur (par exemple tenter de supprimer un fichier vide créé pour l'occasion) et montrer que le garde-fou bloque.
- Indiquer que la commande `/hooks` liste les garde-fous actifs, et comment retirer celui-ci.

## Limites à dire
Un garde-fou réduit les risques, il ne remplace ni les sauvegardes ni le fait de travailler sur une copie des fichiers précieux.
