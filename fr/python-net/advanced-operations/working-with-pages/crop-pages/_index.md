---
title: Recadrage des pages PDF avec Python
linktitle: Recadrage des pages PDF
type: docs
weight: 70
url: /fr/python-net/crop-pages/
description: Vous pouvez changer les propriétés des pages, telles que la largeur, la hauteur, les zones Bleed, Crop et Trimbox, en utilisant Aspose.PDF for Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment accéder et modifier les propriétés des pages PDF en Python
Abstract: L'article fournit un aperçu de la façon d'accéder et de modifier les propriétés des pages dans un document PDF en utilisant Aspose.PDF for Python. Il décrit plusieurs propriétés de page, notamment la media box, la bleed box, la trim box, l'art box et la crop box, en expliquant leur rôle dans la définition des dimensions et des limites d'une page PDF pour l'impression et l'affichage. La media box représente la plus grande taille de page, tandis que la bleed box garantit la couverture d'encre au-delà du bord de la page pour la coupe. La trim box indique la taille finale du document après le rognage, et l'art box englobe le contenu réel de la page. La crop box définit la zone visible dans Adobe Acrobat. L'article inclut un extrait de code Python montrant comment définir une nouvelle crop box, ainsi que les autres boîtes, pour une page spécifique d'un document PDF. Des exemples visuels illustrent l'apparence de la page avant et après l'application du recadrage, démontrant l'application pratique de la modification de ces propriétés.
---

## Obtenir les propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, les zones bleed, crop et trimbox. Aspose.PDF for Python vous permet d'accéder à ces propriétés.

- **media_box**: La media box est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **bleed_box**: Si le document possède une zone de débordement (bleed), le PDF aura également une bleed box. Le bleed correspond à la quantité de couleur (ou d'illustration) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsqu'un document est imprimé et découpé à la taille (« trimmed »), l'encre atteindra le bord de la page. Même si la page est mal découpée - coupée légèrement en dehors des repères de coupe - aucune bordure blanche n'apparaîtra sur la page.
- **trim_box** : La trim box indique la taille finale d'un document après impression et découpe.
- **art_box** : L'art box est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **crop_box** : La crop box est la taille « de page » à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seul le contenu de la crop box est affiché dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, en particulier la section 10.10.1 Page Boundaries.

Recadrez la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) d'un PDF à une zone rectangulaire spécifique en utilisant Aspose.PDF for Python. La fonction ajuste plusieurs boîtes de page — `crop_box`, `trim_box`, `art_box` et `bleed_box` — pour garantir des résultats visuels cohérents. Le recadrage peut être utile pour supprimer les marges indésirables ou se concentrer sur une zone particulière d'une page.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (utilisez `ap.Document()`).
1. Définissez le rectangle de recadrage en utilisant [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) avec les coordonnées souhaitées (en points).
1. Définissez les `crop_box`, `trim_box`, `art_box` et `bleed_box` de la [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) sur le rectangle défini.
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié dans un nouveau fichier de sortie.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

Dans cet exemple, nous avons utilisé un fichier d'exemple [ici](crop_page.pdf). Initialement, notre page ressemble à celle montrée sur la Figure 1.
![Figure 1. Page recadrée](crop_page.png)

Après la modification, la page ressemblera à la Figure 2.
![Figure 2. Page recadrée](crop_page2.png)

## Recadrer la page PDF en fonction du contenu de la première image

Recadrez dynamiquement la première [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) en fonction des limites de la première image trouvée sur la page. En utilisant [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), le script identifie la première image et ajuste le `crop_box` de la page pour correspondre aux dimensions de l'image. Cette approche est utile lorsque vous souhaitez vous concentrer sur un contenu visuel spécifique plutôt que sur des coordonnées prédéfinies.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Localisez les images sur la première page en utilisant [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Vérifiez si des images existent :
- Si trouvé, définissez le `crop_box` de la [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pour correspondre au [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) de la première image.
- Sinon, laissez la page inchangée et informez l'utilisateur.
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modifié dans le fichier de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
