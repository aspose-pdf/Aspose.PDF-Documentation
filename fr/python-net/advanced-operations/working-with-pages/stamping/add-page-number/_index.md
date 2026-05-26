---
title: Ajouter des numéros de page à PDF en Python
linktitle: Ajout de numéro de page
type: docs
weight: 30
url: /fr/python-net/add-page-number/
description: Apprenez comment ajouter des tampons de numéro de page aux documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un numéro de page à un PDF en utilisant Python
Abstract: Cet article traite de l'importance d'ajouter des numéros de page aux documents pour faciliter la navigation et présente la bibliothèque Aspose.PDF for Python via .NET comme outil permettant d'obtenir cela dans les fichiers PDF. La bibliothèque utilise la classe PageNumberStamp, qui offre des propriétés pour personnaliser le tampon de numéro de page, notamment le format, les marges, les alignements et le numéro de départ. Le processus consiste à créer un objet Document et un objet PageNumberStamp, à configurer les propriétés souhaitées, puis à appliquer le tampon aux pages PDF à l'aide de la méthode add_stamp(). L'article fournit un exemple de code Python montrant comment configurer et appliquer des tampons de numéro de page avec des attributs de police personnalisables.
---

Tous les documents doivent comporter des numéros de page. Le numéro de page facilite la localisation des différentes parties du document par le lecteur.

**Aspose.PDF for Python via .NET** vous permet d'ajouter des numéros de page avec [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Ajout du tampon de numéro de page à un PDF

Ajoutez des tampons de numéro de page dynamiques à un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant Aspose.PDF for Python. Le [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) l'objet vous permet d'afficher automatiquement le numéro de page actuel ainsi que le nombre total de pages. L'exemple montre comment créer un tampon de numéro de page, personnaliser son apparence (police, taille, style, couleur, alignement et marges) en utilisant [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), et l'appliquer à un(e) spécifique [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dans le PDF via le [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) méthode. Les valeurs d'alignement proviennent du [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) enum, et couleur/police/style sont disponibles via [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) et [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (polices découvertes via [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Cette fonctionnalité est utile pour générer des documents professionnels, numérotés, et automatiser la pagination dans les flux de travail PDF.

1. Ouvrez le document PDF.
1. Créez un tampon de numéro de page.
1. Définissez les propriétés du tampon.
1. Personnalisez le style du texte.
1. Appliquez le tampon à une page.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Ajout de numéros de page en chiffres romains à un PDF

Ajoutez des numéros de page au format chiffre romain à toutes les pages d'un document PDF. Les numéros de page sont ajoutés sous forme de tampons en utilisant [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), avec une police, une taille, un style, une couleur et un alignement personnalisables. Utilisez le [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) énumération pour choisir les chiffres romains ou d'autres systèmes de numérotation. La numérotation peut également commencer à partir de n'importe quelle valeur spécifiée.

1. Ouvrez le document PDF.
1. Créez un tampon de numéro de page.
1. Configurer les propriétés du tampon.
1. Définir l'apparence du texte.
1. Appliquer le tampon à toutes les pages.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Exemple en direct

[Ajouter des numéros de page PDF](https://products.aspose.app/pdf/page-number) est une application web gratuite en ligne qui vous permet d'examiner le fonctionnement de l'ajout de la fonctionnalité de numérotation des pages.

[![Comment ajouter un numéro de page dans un PDF en utilisant Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## Sujets liés à l'estampage

- [Tamponner les pages PDF en Python](/pdf/fr/python-net/stamping/)
- [Ajouter des tampons de page à un PDF en Python](/pdf/fr/python-net/page-stamps-in-the-pdf-file/)
- [Ajouter des tampons d'image à un PDF en Python](/pdf/fr/python-net/image-stamps-in-pdf-page/)
- [Ajouter des tampons de texte à un PDF en Python](/pdf/fr/python-net/text-stamps-in-the-pdf-file/)