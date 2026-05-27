---
title: Créer des fichiers PDF en Python
linktitle: Créer un document PDF
type: docs
weight: 10
url: /fr/python-net/create-pdf-document/
description: Apprenez comment créer des fichiers PDF et générer des PDF consultables en Python en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un fichier PDF avec Python
Abstract: Aspose.PDF for Python via .NET est une API polyvalente conçue pour les développeurs afin de manipuler les fichiers PDF au sein d’applications Python ciblant le framework .NET. Elle permet aux utilisateurs de créer, charger, modifier et convertir des documents PDF sans effort. Cet article propose un guide étape par étape pour créer un fichier PDF simple à l’aide d’Aspose.PDF. Le processus consiste à initialiser un objet `Document`, à ajouter une `Page` au document, à insérer un `TextFragment` dans les paragraphes de la page, puis à enregistrer le fichier au format PDF. L’extrait de code Python inclus illustre ces étapes en créant un document PDF contenant le texte "Hello World!". Cette API simplifie la gestion des PDF avec un code minimal, améliorant la productivité des développeurs travaillant avec des PDF dans les environnements .NET.
---

**Aspose.PDF for Python via .NET** est une API de manipulation de PDF qui permet aux développeurs de créer, charger, modifier et convertir des fichiers PDF directement depuis Python pour les applications .NET en seulement quelques lignes de code.

Utilisez ces exemples lorsque vous devez générer de nouveaux fichiers PDF à partir de zéro ou convertir la sortie OCR en documents PDF recherchables en Python.

## Comment créer un fichier PDF simple

Pour créer un PDF en utilisant Python via .NET avec Aspose.PDF, vous pouvez suivre ces étapes :

1. Créez un objet de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe
1. Ajouter un [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objet à le [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) collection de le Document objet
1. Ajouter [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection de la page
1. Enregistrez le document PDF résultant

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## Comment créer un document PDF consultable

Aspose.PDF for Python via .NET permet de créer et de manipuler des documents PDF existants. Lors de l'ajout d'éléments Text à un fichier PDF, le PDF résultant est consultable. Cependant, lors de la conversion d'une image contenant du texte en fichier PDF, le contenu du PDF résultant n'est pas consultable. Comme solution de contournement, nous pouvons appliquer l'OCR au fichier résultant afin qu'il devienne consultable.

Le code complet suivant permet de répondre à cette exigence :

1. Chargez le PDF en utilisant 'ap.Document'.
1. Configurez la résolution de rendu.
1. Utilisez 'PngDevice.process' pour convertir la page PDF sélectionnée en image.
1. Exécutez l’OCR sur l’image générée.
1. Créez un nouveau PDF à partir de la sortie OCR.
1. Enregistrez le PDF consultable.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Formater des documents PDF en Python](/pdf/fr/python-net/formatting-pdf-document/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)
- [Optimiser les fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)

