---
title: Obtenir et définir les propriétés des pages en Python
linktitle: Obtenir et définir les propriétés des pages
type: docs
weight: 90
url: /fr/python-net/get-and-set-page-properties/
description: Cette section montre comment obtenir le nombre de pages d'un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment obtenir et définir les propriétés des pages avec Python
Abstract: Cet article examine les capacités d'Aspose.PDF pour Python via .NET, en se concentrant sur la lecture et la définition des propriétés des pages dans les fichiers PDF à l'aide de Python. L'article couvre différentes fonctionnalités, notamment la détermination du nombre de pages d'un PDF, l'accès et la modification des propriétés des pages, ainsi que la gestion des informations de couleur. Pour obtenir le nombre de pages, les classes `Document` et la collection `PageCollection` sont utilisées, avec des extraits de code montrant comment récupérer le nombre de pages, même sans enregistrer le document. L'article explique les différentes propriétés de page telles que MediaBox, BleedBox, TrimBox, ArtBox et CropBox, et fournit des exemples de code pour accéder à ces propriétés. De plus, il aborde la récupération d'une page spécifique d'un PDF et son enregistrement en tant que document séparé, ainsi que la détermination du type de couleur de chaque page. Les exemples sont implémentés en Python, illustrant des applications pratiques de ces fonctionnalités.
---

Aspose.PDF pour Python via .NET vous permet de lire et de définir les propriétés des pages d'un fichier PDF dans vos applications Python. Cette section montre comment obtenir le nombre de pages d'un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages. Les exemples utilisent les APIs [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) et sont écrits en Python.

## Obtenir le nombre de pages d'un fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne nécessite pas plus de deux lignes de code.

Pour obtenir le nombre de pages d'un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Ensuite, utilisez la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (de l'objet Document) pour obtenir le nombre total de pages du document.

L'extrait de code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obtenir le nombre de pages sans enregistrer le document

Il arrive parfois que nous générions des fichiers PDF à la volée et, lors de la création d'un fichier PDF, nous puissions être confrontés à la nécessité (création de tables des matières, etc.) d'obtenir le nombre de pages du PDF sans l'enregistrer sur le système ou dans un flux. Ainsi, pour répondre à ce besoin, une méthode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) a été introduite dans la classe Document. Veuillez consulter l'extrait de code suivant qui montre les étapes pour obtenir le nombre de pages sans enregistrer le document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Obtenir les propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, le bleed‑box, le crop‑box et le trim‑box. Aspose.PDF vous permet d'accéder à ces propriétés.

### Comprendre les propriétés des pages : la différence entre ArtBox, BleedBox, CropBox, MediaBox, TrimBox et la propriété Rect

- **Media box** : Le media box est la plus grande boîte de page. Il correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d’autres termes, le media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Bleed box** : Si le document comporte du débord (bleed), le PDF aura également un bleed box. Le débord correspond à la quantité de couleur (ou d'illustration) qui dépasse le bord d'une page. Il sert à garantir que, lors de l'impression et de la découpe du document à la taille (« trimmed »), l'encre atteindra le bord de la page. Même si la page est mal découpée – coupée légèrement en dehors des repères de coupe – aucune bordure blanche n'apparaîtra sur la page.
- **Trim box** : Le trim box indique la taille finale d'un document après impression et découpe.
- **Art box** : L'art box est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box** : Le crop box correspond à la taille « page » à laquelle votre document PDF est affiché dans Adobe Acrobat. En affichage normal, seuls les contenus du crop box sont affichés dans Adobe Acrobat.
Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, en particulier la section 10.10.1 Page Boundaries.
-- **Page.Rect** : l'intersection (rectangle généralement visible) du MediaBox et du DropBox (`Page.rect`). Consultez le type [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) pour les propriétés du rectangle. L'image ci‑dessous illustre ces propriétés.

Pour plus de détails, veuillez consulter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accéder aux propriétés de la page

La classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fournit toutes les propriétés liées à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

À partir de là, il est possible d'accéder soit à des objets `Page` individuels en utilisant leur indice, soit de parcourir la collection pour obtenir toutes les pages. Une fois qu'une page individuelle est accessible, nous pouvons obtenir ses propriétés. L'extrait de code suivant montre comment obtenir les propriétés d'une page (l'API `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Déterminer la couleur de la page

La classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fournit les propriétés liées à une page particulière d'un document PDF, y compris le type de couleur – RGB, noir et blanc, niveaux de gris ou indéfini – que la page utilise.

Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). La propriété [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) indique la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur d'une page PDF particulière, utilisez la propriété [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de l'objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

L'extrait de code suivant montre comment parcourir chaque page d'un fichier PDF afin d'obtenir les informations de couleur.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


