---
title: Ajout de tampons de texte dans PDF via Python
linktitle: Tampons de texte dans le fichier PDF
type: docs
weight: 20
url: /fr/python-net/text-stamps-in-the-pdf-file/
description: Ajoutez un tampon de texte à un document PDF en utilisant la classe TextStamp avec la bibliothèque Aspose.PDF pour Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons de texte dans PDF en utilisant Python
Abstract: Cet article fournit un guide complet sur l'ajout de tampons de texte aux fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il décrit l'utilisation de la classe `TextStamp` pour créer des tampons de texte personnalisables avec des propriétés telles que la taille de la police, le style, la couleur et l'alignement. L'article comprend des extraits de code démontrant comment ajouter un tampon de texte simple, configurer l'alignement du texte et appliquer des modes de rendu avancés comme le texte à remplissage et contour. La première section explique la création d'un objet `Document` et d'un objet `TextStamp`, la définition des propriétés du texte et l'ajout du tampon à une page spécifique. La deuxième section introduit la propriété `text_alignment` pour aligner le texte horizontalement et verticalement, en fournissant un exemple de code pour centrer le texte sur une page PDF. La section finale aborde les modes de rendu, montrant comment ajouter du texte à remplissage et contour en utilisant un objet `TextState` pour définir la couleur du contour et le mode de rendu avant de le lier à un tampon. Chaque section est accompagnée d'exemples pratiques pour faciliter la compréhension et l'implémentation.
---

## Ajout d'un tampon de texte avec Python

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) pour ajouter un tampon de texte dans un fichier PDF. La classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de police et la couleur de la police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Ensuite, vous pouvez appeler la méthode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) de la Page pour ajouter le tampon dans le PDF. Le fragment de code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF. Ceci est utile pour ajouter des annotations, des filigranes ou des étiquettes aux pages PDF.

1. Ouvrez le document PDF.
1. Créez un objet TextStamp.
1. Définissez le comportement de l'arrière-plan du tampon.
1. Positionnez le tampon sur la page.
1. Faites pivoter le tampon si nécessaire.
1. Définissez les propriétés du texte.
1. Ajoutez le tampon à une page.
1. Enregistrez le document PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

