---
title: Modifier la taille de la page avec Python
linktitle: Modifier la taille de la page
type: docs
weight: 40
url: /fr/python-net/change-page-size/
description: Modifiez la taille des pages de votre document PDF à l'aide d'Aspose.PDF pour Python via la bibliothèque .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifier la taille de la page avec Python
Abstract: Cet article montre comment lire et modifier les dimensions des pages PDF à l'aide d'Aspose.PDF. L'exemple «Obtenir la taille de la page» récupère la largeur et la hauteur d'une page PDF spécifique, permettant aux utilisateurs d'inspecter la mise en page, de valider le formatage ou d'analyser la structure du document. L'exemple «Définir la taille de la page» montre comment modifier les dimensions d'une page — par exemple en convertissant la première page au format A4 — tout en affichant les propriétés des boîtes (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) avant et après la modification.
---

Aspose.PDF pour Python via .NET vous permet de modifier la taille des pages PDF avec quelques lignes de code. Ce sujet montre comment mettre à jour les dimensions des pages en utilisant les API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

Veuillez noter que les propriétés de hauteur et de largeur utilisent les points comme unité de base, où 1 pouce = 72 points et 1 cm = 1/2,54 pouce = 0,3937 pouce = 28,3 points.

{{% /alert %}}

### Définir la taille de la page PDF à A4

L'exemple met à jour la taille de la première page d'un document PDF aux dimensions standard A4. Il affiche également les dimensions des boîtes de la page (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) avant et après le redimensionnement afin que vous puissiez vérifier les modifications.

Le fragment de code suivant montre comment modifier les dimensions des pages PDF au format A4 :

1. Accédez à la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) du [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Affichez les tailles des boîtes de la page avant la modification (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Appliquez les dimensions A4 (597,6 × 842,4 points) à l'aide de l'API de la page.
1. Affichez les tailles des boîtes de la page mises à jour.
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié vers le chemin de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Obtenir la taille de la page PDF

Ce fragment lit un PDF et récupère les dimensions (largeur et hauteur) de la première page. Il utilise l'API [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pour extraire le [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) englobant de la page et affiche sa taille dans la console. Ceci est utile pour inspecter la mise en page, vérifier les formats ou préparer des documents pour un traitement ultérieur.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Accédez à la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Récupérez le rectangle englobant de la page à l'aide de `get_page_rect()`.
1. Extrayez les valeurs de largeur et de hauteur.
1. Imprimez les dimensions de la page.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obtenir la taille de la page PDF avant et après rotation

Récupérez les dimensions d'une page PDF avant et après l'application d'une rotation de 90°. Cela montre comment la rotation affecte la largeur et la hauteur et comment utiliser `get_page_rect()` avec ou sans prise en compte de la rotation.

1. Ouvrez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Accédez à la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Appliquez une rotation de 90° en utilisant `page.rotate = ap.Rotation.ON90` (voir l'énumération [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. Récupérez le rectangle de la page sans rotation en utilisant `get_page_rect(False)` et affichez sa largeur et sa hauteur.
1. Récupérez le rectangle de la page en prenant en compte la rotation avec `get_page_rect(True)` et affichez sa largeur et sa hauteur.
1. Comparez comment les dimensions changent en raison de la rotation.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
