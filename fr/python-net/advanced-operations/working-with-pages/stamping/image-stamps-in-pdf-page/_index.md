---
title: Ajout de tampons d'image dans un PDF avec Python
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /fr/python-net/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons d'image dans un PDF avec Python
Abstract: Cet article fournit un guide complet sur l'ajout de tampons d'image aux fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il détaille l'utilisation de la classe `ImageStamp`, qui permet la personnalisation des tampons basés sur des images, y compris des propriétés telles que la hauteur, la largeur, l'opacité et la rotation. Le processus consiste à créer un objet `Document` et un objet `ImageStamp` avec les propriétés souhaitées, puis à ajouter le tampon à une page spécifique du PDF en utilisant la méthode `add_stamp()`. L'article inclut des extraits de code Python montrant comment appliquer un tampon d'image à un PDF et contrôler sa qualité à l'aide de la propriété `quality`, qui ajuste la qualité de l'image en pourcentage. De plus, l'article explique comment utiliser les tampons d'image comme arrière-plans dans des boîtes flottantes avec la classe `FloatingBox`, en fournissant un autre exemple de code pour montrer comment cela peut être mis en œuvre. Ce guide constitue une ressource utile pour les développeurs souhaitant enrichir les PDFs avec des tampons d'image en utilisant Aspose.PDF.
---

## Ajout d'un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) pour ajouter un tampon d'image à un fichier PDF. La classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) fournit les propriétés nécessaires à la création d'un tampon basé sur une image, comme la hauteur, la largeur, l'opacité, etc. Le tampon peut être positionné, redimensionné, rotatif, et rendu partiellement transparent, permettant le filigrane, le branding ou les annotations.

Le fragment de code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

1. Charger le PDF en utilisant 'ap.Document()'.
1. Créer un tampon d'image avec 'ImageStamp()'.
1. Configurer les propriétés du tampon.
1. Ajouter le tampon à la page cible.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Contrôler la qualité de l'image lors de l'ajout du tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez contrôler la qualité de l'image. La propriété [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) est utilisée à cette fin. Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).
En définissant la propriété quality, vous pouvez réduire la résolution de l'image pour optimiser la taille du PDF ou maintenir une fidélité supérieure pour plus de clarté.

1. Ouvrir le document PDF.
1. Créer un tampon d'image.
1. Définir la qualité de l'image.
1. Ajouter le tampon à la page cible.
1. Enregistrer le PDF modifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Tampon d'image comme arrière-plan dans une boîte flottante

Créez une [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) dans un PDF et appliquez une image comme arrière-plan. Cela montre également comment ajouter du texte, définir les bordures, la couleur d'arrière-plan et positionner la boîte précisément sur la page. C'est utile pour créer un contenu PDF visuellement riche comme des infobulles, des bannières ou des sections mises en évidence avec du texte superposé sur des images.

1. Ouvrir ou créer un document PDF.
1. Créer un objet 'FloatingBox'.
1. Ajouter du texte dans la boîte.
1. Définir la bordure de la boîte et la couleur d'arrière-plan.
1. Ajouter une image d'arrière-plan.
1. Ajouter la FloatingBox à la page.
1. Enregistrer le document PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```


