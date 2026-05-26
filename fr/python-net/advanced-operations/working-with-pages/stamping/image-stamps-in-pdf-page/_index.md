---
title: Ajouter des tampons d'image au PDF en Python
linktitle: Tampons d'image dans le fichier PDF
type: docs
weight: 10
url: /fr/python-net/image-stamps-in-pdf-page/
description: Apprenez comment ajouter des tampons d'image aux pages PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons d'image dans le PDF en utilisant Python
Abstract: Cet article fournit un guide complet sur l'ajout de tampons d'image aux fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Python. Il détaille l'utilisation de la classe `ImageStamp`, qui permet de personnaliser les tampons basés sur des images, y compris les propriétés telles que la hauteur, la largeur, l'opacité et la rotation. Le processus consiste à créer un objet `Document` et un objet `ImageStamp` avec les propriétés souhaitées, puis à ajouter le tampon à une page spécifique du PDF en utilisant la méthode `add_stamp()`. L'article inclut des extraits de code Python montrant comment appliquer un tampon d'image à un PDF et contrôler sa qualité à l'aide de la propriété `quality`, qui ajuste la qualité de l'image en pourcentage. De plus, l'article explique comment utiliser les tampons d'image comme arrière-plans dans des boîtes flottantes avec la classe `FloatingBox`, en fournissant un autre exemple de code pour montrer comment cela peut être implémenté. Ce guide constitue une ressource utile pour les développeurs souhaitant enrichir les PDFs avec des tampons d'image en utilisant Aspose.PDF.
---

## Ajout du tampon d'image dans le fichier PDF

Vous pouvez utiliser le [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) classe pour ajouter un tampon d'image à un fichier PDF. Le [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) La classe fournit les propriétés nécessaires pour créer un tampon basé sur une image, telles que la hauteur, la largeur, l'opacité, etc. Le tampon peut être positionné, redimensionné, pivoté et rendu partiellement transparent, permettant le filigrane, la marque ou les annotations.

Le morceau de code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

1. Chargez le PDF en utilisant 'ap.Document()'.
1. Créez un tampon d'image avec 'ImageStamp()'.
1. Configurer les propriétés du tampon.
1. Ajoutez le tampon à la page cible.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

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

## Contrôler la qualité de l'image lors de l'ajout d'un tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez contrôler la qualité de l'image. Le [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) propriété de [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) la classe est utilisée à cette fin. Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).
En définissant la propriété quality, vous pouvez réduire la résolution de l'image afin d'optimiser la taille du PDF ou de maintenir une fidélité plus élevée pour une meilleure clarté.

1. Ouvrez le document PDF.
1. Créer un tampon d'image.
1. Définir la qualité de l'image.
1. Ajoutez le tampon à la page cible.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## ImageStamp comme arrière-plan dans une boîte flottante

Créer un [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) dans un PDF et appliquez une image comme arrière-plan. Il montre également comment ajouter du texte, définir les bordures, la couleur d'arrière-plan et positionner la boîte précisément sur la page. Ceci est utile pour créer un contenu PDF visuellement riche comme des encadrés, des bannières ou des sections mises en évidence avec du texte sur des images.

1. Ouvrez ou créez un document PDF.
1. Créez un objet \u0027FloatingBox\u0027.
1. Ajoutez du texte à la boîte.
1. Définissez la bordure et la couleur d'arrière-plan de la boîte.
1. Ajoutez une image d'arrière-plan.
1. Ajoutez le FloatingBox à la page.
1. Enregistrez le document PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
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

## Sujets liés à l'estampage

- [Tamponner les pages PDF en Python](/pdf/fr/python-net/stamping/)
- [Ajouter des tampons de page à un PDF en Python](/pdf/fr/python-net/page-stamps-in-the-pdf-file/)
- [Ajouter des tampons de texte à un PDF en Python](/pdf/fr/python-net/text-stamps-in-the-pdf-file/)
- [Ajouter des numéros de page à un PDF en Python](/pdf/fr/python-net/add-page-number/)