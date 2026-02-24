---
title: Créer des liens dans un fichier PDF avec Python
linktitle: Créer des liens
type: docs
weight: 10
url: /fr/python-net/create-links/
description: Cette section explique comment créer des liens dans votre document PDF avec Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment créer des liens dans PDF
Abstract: Le guide Aspose.PDF pour Python via .NET sur la création de liens fournit aux développeurs des instructions pratiques pour ajouter des hyperliens interactifs aux documents PDF en utilisant Python. Il couvre la création de divers types de liens, y compris ceux qui lancent des applications externes, naviguent vers des pages spécifiques du même document ou ouvrent d'autres fichiers PDF. La documentation explique comment utiliser les objets LinkAnnotation, définir des zones cliquables avec Rectangle et attribuer des actions telles que LaunchAction ou GoToRemoteAction. Avec des exemples de code clairs et des directives étape par étape, cette ressource aide les développeurs à améliorer la navigation et l'interactivité des PDF dans leurs applications Python.
---

## Liens dans les documents PDF

Selon la spécification PDF 1.7 (ISO 32000-1:2008), une annotation **Link** peut déclencher plusieurs types d'actions qui définissent ce qui se passe lorsque l'annotation est activée. Voici les principales actions prises en charge :

1. **GoTo** – Navigue vers une destination dans le même document.
1. **GoToR** – Saute vers une destination dans un autre fichier PDF (navigation à distance).
1. **URI** – Ouvre un identifiant de ressource uniforme, généralement un lien web.
1. **Launch** – Lance une application ou ouvre un fichier (dépend de la plateforme et souvent limité pour des raisons de sécurité).
1. **Named** – Exécute une action prédéfinie, comme passer à la page suivante ou imprimer le document.
1. **JavaScript** – Exécute du code JavaScript intégré (utilisé avec prudence en raison des problèmes de sécurité).
1. **SubmitForm** – Soumet les données du formulaire à une URL spécifiée.
1. **ResetForm** – Réinitialise les champs du formulaire à leurs valeurs par défaut.
1. **ImportData** – Importe des données dans le document depuis un fichier externe.

En ajoutant un lien vers une application dans un document, il est possible de créer des liens vers des applications depuis un document. Cela est utile lorsque vous souhaitez que les lecteurs effectuent une certaine action à un point précis d'un tutoriel, par exemple, ou pour créer un document riche en fonctionnalités.

Pour créer un lien d'application avec 'LaunchAction' :

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Créer un lien de document PDF dans un fichier PDF

### Utilisation de GoToRemoteAction

Cet extrait de code montre comment ajouter une annotation de lien à une page spécifique d'un document PDF en utilisant une bibliothèque PDF Python.

1. Ouvrez le document PDF
1. Sélectionnez la deuxième page du document (index 1)
1. Créez une annotation de lien :
1. Positionnée aux coordonnées (10, 580, 120, 600)
1. Colorée en vert
1. Lien vers 'sample.pdf' sur sa première page
1. Ajoutez l'annotation de lien à la page
1. Enregistrez le document modifié vers le chemin de fichier de sortie

Pour créer un lien de document PDF en utilisant 'GoToRemoteAction' :

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Utilisation de GoToAction

Ce code montre comment ajouter une annotation de lien à une page spécifique d'un document PDF en utilisant Aspose.PDF pour Python. Le lien apparaît sous la forme d'un rectangle vert à bordure pointillée et permet à l'utilisateur de naviguer vers une autre page du même PDF. Pour créer un lien de document PDF en utilisant 'GoToAction' :

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Application de GoToURIAction

Le prochain exemple montre comment ajouter une annotation de lien à un document PDF en utilisant Aspose.PDF pour Python. Le lien apparaît comme une zone cliquable verte sur la première page et, lorsqu'elle est cliquée, elle ouvre la documentation Aspose.PDF pour Python dans un navigateur web via un GoToURIAction.

Cette fonctionnalité est utile pour intégrer des références externes utiles, de la documentation ou des liens d'assistance directement dans vos PDF.

1. Chargez le document PDF. Ouvrez le fichier PDF existant en utilisant ap.Document.
1. Accédez à la première page. Utilisez document.pages[1] pour accéder à la première page (Aspose utilise l'indexation à partir de 1).
1. Créez une annotation de lien. Créez un objet LinkAnnotation et spécifiez la zone rectangulaire cliquable à l'aide de ap.Rectangle.
1. Définissez l'apparence de l'annotation. Réglez la couleur de l'annotation en vert en utilisant link.color = ap.Color.green.
1. Assignez une action URI. Utilisez GoToURIAction pour lier l'annotation à une URL externe.
1. Ajoutez l'annotation à la page. Ajoutez l'annotation de lien configurée à la collection d'annotations de la première page.
1. Enregistrez le document modifié. Enregistrez le document PDF mis à jour vers le chemin de sortie spécifié.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

