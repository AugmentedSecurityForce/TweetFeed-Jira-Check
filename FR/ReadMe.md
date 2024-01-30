# PRESENTATION
Ce script Python permet de vérifier les indicateurs de compromission (IoC) extraits du fichier week.csv fournit par ![TweetFeed](https://tweetfeed.live) par rapport à un fichier de référence jira_soc.csv comportant l'extraction des tickets Jira.

# OBJECTIF
L'objectif de ce script est d'identifier les IoCs présents dans le fichier week.csv qui sont présents  dans le fichier de référence jira_soc.csv. Cela permet de détecter de nouvelles menaces potentielles et de prendre des mesures de sécurité appropriées.

# DIAGRAMME DES ACTIONS DU SCRIPT
[diagram](./Images/Diagram.png)
 
# Utilisation du script
## Prérequis
Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants :
* Python 3 installé sur votre système.
* Les bibliothèques Python listées dans le fichier requirements.txt.
* Accès internet

## Installation des prérequis
Pour installer les dépendances requises, exécutez la commande suivante :
```pip install -r requirements.txt```

##	Commande
Utiliser la commande suivante : 
```python3 controle_ioc_weekly.py```

## Modification
Le choix a été fait de réaliser un contrôle avec les IoC hebdomadaire, mais TweetFeed fournit aussi les csv journaliers, mensuels et annuels.