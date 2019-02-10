
# Présentation globale

Ceci est un convertisseur simple de fichier Markdown vers fichier HTML.

## Commandes

**Argument obligatoire, la politesse :**

 - [x] Il faut toujours commencer par le mot clé `mth` pour appeler la console.

**Arguments disponibles :**

| ARGUMENT | DESCRIPTION |
|--|--|
| -h ou --help | Permet d'affichier les commandes diponibles, et aussi un exemple d'utilisation de la console. |
| -i ou --input-directory | Permet de spécifier le chemin du fichier qui sera convertit mais le chemin sera défini par rapport à l'emplacement du Convertisseur. Si cet argument est utilisé seul, le résultat de la convertion sera dans le même fichier que le fichier qui à été convertit. |
| -o ou --output-directory | Permet de spécifier un chemin vers lequel le résultat de la conversion sera stocké. |
| -q ou --quitter | Permet de quitter la console de conversion. |

### Exemple d'utilisation

    M2H>> mth -i fichier.md

> Le fichier sera convertit, et le résultat sera stocké dans le même dossier.

    M2H>> mth -i fichier.md -o 

## Information complémentaires 

 - [x] Aucun packages autre que des packages propres à python sont utilisé, il n'y à pas de prérequis à installer.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDgwMzY5NDZdfQ==
-->