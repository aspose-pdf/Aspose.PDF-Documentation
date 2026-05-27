---
title: Créer des liens PDF en Python
linktitle: Créer des liens
type: docs
weight: 10
url: /fr/python-net/create-links/
description: Apprenez comment créer des liens PDF internes, externes et distants en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment créer des liens dans PDF
Abstract: Le guide Aspose.PDF for Python via .NET sur la création de liens fournit aux développeurs des instructions pratiques pour ajouter des hyperliens interactifs aux documents PDF en utilisant Python. Il couvre la création de différents types de liens, y compris ceux qui lancent des applications externes, naviguent vers des pages spécifiques du même document ou ouvrent d’autres fichiers PDF. La documentation explique comment utiliser les objets LinkAnnotation, définir des zones cliquables avec Rectangle et attribuer des actions telles que LaunchAction ou GoToRemoteAction. Avec des exemples de code clairs et des directives pas à pas, cette ressource aide les développeurs à améliorer la navigation et l’interactivité des PDF dans leurs applications Python.
---

## Liens dans les documents PDF

Selon la spécification PDF 1.7 (ISO 32000-1:2008), une **annotation de lien** peut déclencher plusieurs types d'actions qui définissent ce qui se passe lorsque l'annotation est activée. Voici les actions principales prises en charge :

1. **GoTo** – Navigue vers une destination dans le même document.
1. **GoToR** – Saute vers une destination dans un autre fichier PDF (go‑to distant).
1. **URI** – Ouvre un identifiant uniforme de ressource, généralement un lien web.
1. **Launch** – Lance une application ou ouvre un fichier (dépendant de la plateforme et souvent restreint pour des raisons de sécurité).
1. **Named** – Exécute une action prédéfinie, telle que passer à la page suivante ou imprimer le document.
1. **JavaScript** – Exécute du code JavaScript intégré (utilisé avec précaution en raison de problèmes de sécurité).
1. **SubmitForm** – Envoie les données du formulaire à une URL spécifiée.
1. **ResetForm** – Réinitialise les champs du formulaire à leurs valeurs par défaut.
1. **ImportData** – Importe des données dans le document depuis un fichier externe.

En ajoutant un lien vers une application dans un document, il est possible de créer des liens vers des applications depuis un document. Cela est utile lorsque vous souhaitez que les lecteurs effectuent une action précise à un moment donné d’un didacticiel, par exemple, ou pour créer un document riche en fonctionnalités.

Pour créer un lien d'application avec ‘LaunchAction’:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## Créer un lien de document PDF dans un fichier PDF

### Utilisation de GoToRemoteAction

Cet extrait de code montre comment ajouter une annotation de lien à une page spécifique d'un document PDF à l'aide d'une bibliothèque PDF Python.

1. Ouvrez le document PDF
1. Sélectionnez la deuxième page du document (indice 1)
1. Créez une annotation de lien :
1. Positionné aux coordonnées (10, 580, 120, 600)
1. Coloré en vert
1. Liens vers 'sample.pdf' sur sa première page
1. Ajouter l'annotation de lien à la page
1. Enregistrez le document modifié vers le chemin du fichier de sortie

Pour créer un lien de document PDF en utilisant 'GoToRemoteAction' :

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Utilisation de GoToAction

Ce code montre comment ajouter une annotation de lien à une page spécifique d'un document PDF à l'aide d'Aspose.PDF for Python. Le lien apparaît sous la forme d'un rectangle vert bordé de tirets et permet à l'utilisateur de naviguer vers une autre page du même PDF. Pour créer un lien de document PDF en utilisant 'GoToAction' :

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Appliquer GoToURIAction

L'exemple suivant montre comment ajouter une annotation de lien à un document PDF en utilisant Aspose.PDF for Python. Le lien apparaît sous la forme d'une zone cliquable verte sur la première page et, lorsqu'on clique dessus, il ouvre la documentation Aspose.PDF for Python dans un navigateur web via une GoToURIAction.

Cette fonctionnalité est utile pour intégrer des références externes utiles, de la documentation ou des liens d'assistance directement dans vos PDF.

1. Chargez le Document PDF. Ouvrez le fichier PDF existant en utilisant ap.Document.
1. Accédez à la première page. Utilisez document.pages[1] pour accéder à la première page (Aspose utilise un indice basé sur 1).
1. Créez une annotation de lien. Créez un objet LinkAnnotation et spécifiez la zone rectangulaire cliquable en utilisant ap.Rectangle.
1. Définir l’apparence de l'annotation. Définir la couleur de l'annotation sur vert en utilisant link.color = ap.Color.green.
1. Attribuer une action URI. Utiliser GoToURIAction pour lier l'annotation à une URL externe.
1. Ajouter l'annotation à la page. Ajouter l'annotation de lien configurée à la collection d'annotations de la première page.
1. Enregistrer le document modifié. Enregistrer le document PDF mis à jour vers le chemin de sortie spécifié.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Sujets liés aux liens

- [Travailler avec les liens PDF en Python](/pdf/fr/python-net/links/)
- [Extraire les liens du PDF en Python](/pdf/fr/python-net/extract-links/)
- [Mettre à jour les liens du PDF en utilisant Python](/pdf/fr/python-net/update-links/)