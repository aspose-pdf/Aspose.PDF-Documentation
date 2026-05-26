---
title: Ajouter des tampons de texte à un PDF en Python
linktitle: Tampons de texte dans un fichier PDF
type: docs
weight: 20
url: /fr/python-net/text-stamps-in-the-pdf-file/
description: Apprenez comment ajouter des tampons de texte aux documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons de texte dans un PDF en utilisant Python
Abstract: Cet article fournit un guide complet sur l'ajout de tampons de texte aux fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il décrit l'utilisation de la classe `TextStamp` pour créer des tampons de texte personnalisables avec des propriétés telles que la taille de la police, le style, la couleur et l'alignement. L'article inclut des extraits de code montrant comment ajouter un tampon de texte simple, configurer l'alignement du texte et appliquer des modes de rendu avancés comme le texte à remplissage et contour. La première section explique la création d'un objet `Document` et `TextStamp`, la définition des propriétés du texte, et l'ajout du tampon à une page spécifique. La deuxième section présente la propriété `text_alignment` pour aligner le texte horizontalement et verticalement, en fournissant un exemple de code centré sur une page PDF. La section finale traite des modes de rendu, démontrant comment ajouter du texte à remplissage et contour à l'aide d'un objet `TextState` pour définir la couleur du contour et le mode de rendu avant de le lier à un tampon. Chaque section est accompagnée d'exemples pratiques pour faciliter la compréhension et la mise en œuvre.
---

## Ajout d'un tampon de texte avec Python

Vous pouvez utiliser [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) classe pour ajouter un tampon de texte dans un fichier PDF. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) la classe fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de police et la couleur de police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) méthode de la Page pour ajouter le tampon dans le PDF. Le fragment de code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF. Ceci est utile pour ajouter des annotations, des filigranes ou des étiquettes aux pages PDF.

1. Ouvrez le document PDF.
1. Créer un objet TextStamp.
1. Définir le comportement d'arrière-plan du tampon.
1. Positionner le tampon sur la page.
1. Faire pivoter le tampon si nécessaire.
1. Définir les propriétés du texte.
1. Ajouter le tampon à une page.
1. Enregistrez le document PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Sujets liés à l'estampage

- [Tamponner les pages PDF en Python](/pdf/fr/python-net/stamping/)
- [Ajouter des tampons de page à un PDF en Python](/pdf/fr/python-net/page-stamps-in-the-pdf-file/)
- [Ajouter des tampons d'image à un PDF en Python](/pdf/fr/python-net/image-stamps-in-pdf-page/)
- [Ajouter des numéros de page à un PDF en Python](/pdf/fr/python-net/add-page-number/)