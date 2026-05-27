---
title: Obtenir et définir les propriétés des pages PDF en Python
linktitle: Obtention et définition des propriétés de page
type: docs
weight: 90
url: /fr/python-net/get-and-set-page-properties/
description: Apprenez à inspecter et à mettre à jour les propriétés des pages PDF telles que la taille, le nombre et les informations de couleur en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment obtenir et définir les propriétés de page en utilisant Python
Abstract: Cet article décrit les capacités d'Aspose.PDF for Python via .NET, en se concentrant sur la lecture et la définition des propriétés de page dans les fichiers PDF à l'aide de Python. L'article couvre diverses fonctionnalités, notamment la détermination du nombre de pages d'un PDF, l'accès et la modification des propriétés de page, et la gestion des informations de couleur. Pour obtenir le nombre de pages, les classes `Document` et la collection `PageCollection` sont utilisées, avec des extraits de code montrant comment récupérer le nombre de pages, même sans enregistrer le document. L'article explique les différentes propriétés de page telles que MediaBox, BleedBox, TrimBox, ArtBox et CropBox, et fournit des exemples de code pour accéder à ces propriétés. De plus, il décrit comment extraire une page spécifique d'un PDF et l'enregistrer comme document séparé, ainsi que la détermination du type de couleur de chaque page. Les exemples sont implémentés en Python, illustrant des applications pratiques de ces fonctionnalités.
---

Aspose.PDF for Python via .NET vous permet de lire et de définir les propriétés des pages d'un fichier PDF dans vos applications Python. Cette section montre comment obtenir le nombre de pages d'un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés des pages. Les exemples utilisent le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) APIs sont écrites en Python.

Utilisez ce guide lorsque vous devez inspecter les métadonnées des pages, déterminer le nombre de pages ou mettre à jour les caractéristiques au niveau de la page dans le cadre de l'analyse ou de la normalisation de documents.

## Obtenir le nombre de pages dans un fichier PDF

Lorsque vous travaillez avec des documents, vous voulez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF:

1. Ouvrez le fichier PDF en utilisant le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Ensuite utilisez le [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) propriété Count de la collection (à partir de l'objet Document) pour obtenir le nombre total de pages dans le document.

Le fragment de code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obtenir le nombre de pages sans enregistrer le document

Parfois, nous générons les fichiers PDF à la volée et, lors de la création d'un fichier PDF, nous pouvons être confrontés à la nécessité (création d'une table des matières, etc.) d'obtenir le nombre de pages d'un fichier PDF sans l'enregistrer sur le système ou le flux. Ainsi, afin de répondre à cette exigence, une méthode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) a été introduit dans la classe Document. Veuillez consulter le fragment de code suivant qui montre les étapes pour obtenir le nombre de pages sans enregistrer le document.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
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

Chaque page d’un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, les boîtes bleed, crop et trimbox. Aspose.PDF vous permet d’accéder à ces propriétés.

### Comprendre les propriétés de page : la différence entre Artbox, BleedBox, CropBox, MediaBox, TrimBox et la propriété Rect

- **Media box**: La media box est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d’autres termes, la media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Bleed box**: Si le document possède une marge de coupe, le PDF aura également une bleed box. La marge de coupe (bleed) est la quantité de couleur (ou d’illustration) qui dépasse le bord d’une page. Elle est utilisée pour s’assurer que lorsque le document est imprimé et découpé à la taille (« trimmed »), l’encre ira jusqu’au bord de la page. Même si la page est mal découpée - coupée légèrement hors des marques de coupe - aucune bordure blanche n’apparaîtra sur la page.
- **Trim box** : La trim box indique la taille finale d’un document après impression et rognage.
- **Art box** : La art box est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l’importation de documents PDF dans d’autres applications.
- **Crop box** : La crop box est la taille « page » à laquelle votre document PDF est affiché dans Adobe Acrobat. En affichage normal, seul le contenu de la crop box est affiché dans Adobe Acrobat.
  Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, en particulier la section 10.10.1 Limites de page.
-- **Page.Rect** : l'intersection (rectangle généralement visible) de la MediaBox et de la DropBox (`Page.rect`). Voir le [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) type pour les propriétés du rectangle. L'image ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accès aux propriétés de la page

Le [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) la classe fournit toutes les propriétés liées à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans le de le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de l'objet [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection.

De là, il est possible d'accéder soit à l'individu `Page` objets en utilisant leur indice, ou parcourir la collection pour obtenir toutes les pages. Une fois qu'une page individuelle est accédée, nous pouvons obtenir ses propriétés. Le fragment de code suivant montre comment obtenir les propriétés de la page (le `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
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
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Déterminer la couleur de la page

Le [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) La classe fournit les propriétés liées à une page particulière d'un document PDF, y compris le type de couleur - RVB, noir et blanc, niveaux de gris ou indéfini - utilisé par la page.

Toutes les pages des fichiers PDF sont contenues par le [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection. Le [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) la propriété spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur pour une page PDF particulière, utilisez le [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de l'objet [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) propriété.

L'extrait de code suivant montre comment parcourir chaque page d'un fichier PDF pour obtenir des informations sur les couleurs.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
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
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Modifier la taille de la page PDF en Python](/pdf/fr/python-net/change-page-size/)
- [Recadrer les pages PDF en Python](/pdf/fr/python-net/crop-pages/)
- [Faire pivoter les pages PDF en Python](/pdf/fr/python-net/rotate-pages/)