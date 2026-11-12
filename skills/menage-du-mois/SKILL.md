---
name: menage-du-mois
description: Fait le ménage mensuel de la configuration de Claude avec l'utilisateur : fichiers de consignes trop longs ou contradictoires, skills inutilisés, connecteurs et tâches planifiées oubliés, notes de mémoire périmées. À utiliser quand l'utilisateur dit « fais le ménage », « ménage du mois », « range ma configuration ».
disable-model-invocation: true
---

# Le ménage du mois

Rien n'est modifié ni supprimé sans l'accord de l'utilisateur. Ce skill **propose** ; l'utilisateur **décide**.

## Passer en revue
1. **Les consignes** : le fichier de consignes du projet et le fichier personnel. Repérer ce qui est vague, contradictoire, périmé, ou qui décrit ce que Claude peut voir seul dans les fichiers. Repérer les procédures longues qui seraient mieux dans un skill. Indiquer la longueur de chaque fichier.
2. **Les skills** : ceux qui sont installés, ceux qui se ressemblent, ceux qui n'ont pas servi depuis longtemps, ceux dont la description est floue.
3. **Les connecteurs et les tâches planifiées** : lister ceux que l'application montre ; demander à l'utilisateur lesquels servent encore, puisque ce skill ne les voit pas tous.
4. **La mémoire** : demander à l'utilisateur ce que la mémoire contient (Paramètres, rubrique Mémoire) et signaler ce qui paraît faux ou dépassé.

## Rendre le bilan
Une liste courte, classée en trois groupes :
- **à supprimer ou désactiver** ;
- **à raccourcir ou corriger** ;
- **à garder tel quel**.

Pour chaque ligne, une raison en quelques mots. Puis demander, groupe par groupe : « Je fais ces changements ? » et ne faire que ceux que l'utilisateur accepte.

## Astuce
Si la commande `/doctor` est disponible (elle l'est dans Claude Code en terminal), elle fait une partie de ce contrôle automatiquement : la proposer en complément.
