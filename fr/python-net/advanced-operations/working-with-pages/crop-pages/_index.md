---
title: Recadrer des pages PDF en Python
linktitle: Recadrage de pages PDF
type: docs
weight: 70
url: /fr/python-net/crop-pages/
description: Apprenez à recadrer des pages PDF et à ajuster les boîtes de recadrage, de rognage, de débordement et de média en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment accéder aux propriétés des pages d’un PDF et les modifier avec Python
Abstract: L’article présente un aperçu de la façon d’accéder aux propriétés des pages et de les modifier dans un document PDF à l’aide d’Aspose.PDF for Python. Il décrit plusieurs propriétés de page, notamment la boîte de média, la boîte de débordement, la boîte de rognage, la boîte d’art et la boîte de recadrage, en expliquant leurs rôles dans la définition des dimensions et des limites d’une page PDF aux fins d’impression et d’affichage. La boîte de média représente la plus grande taille de page, tandis que la boîte de débordement assure une couverture d’encre au‑delà du bord de la page pour le découpage. La boîte de rognage indique la taille finale du document après découpage, et la boîte d’art encapsule le contenu réel de la page. La boîte de recadrage définit la zone visible dans Adobe Acrobat. L’article inclut un extrait de code Python montrant comment définir une nouvelle boîte de recadrage, ainsi que d’autres boîtes, pour une page spécifique d’un document PDF. Des exemples visuels illustrent l’apparence de la page avant et après l’application du recadrage, mettant en évidence l’utilisation pratique de la modification de ces propriétés.
---

## Obtenir les propriétés de la page

Chaque page d'un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, bleed-, crop- et trimbox. Aspose.PDF for Python vous permet d'accéder à ces propriétés.

Utilisez cette page lorsque vous avez besoin de réduire la zone visible de la page, de préparer des fichiers pour les flux de travail d'impression, ou d'inspecter la géométrie des boîtes de page dans les documents PDF.

- **media_box**: La media box est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou en PDF. En d'autres termes, la media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **bleed_box**: Si le document possède du bleed, le PDF comportera également une boîte de bleed. Le bleed est la quantité de couleur (ou d'illustration) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille (\u0022trimmed\u0022), l'encre ira jusqu'au bord de la page. Même si la page est mal découpée - découpée légèrement en dehors des repères de coupe - aucune bordure blanche n'apparaîtra sur la page.
- **trim_box**: La trim box indique la taille finale d'un document après impression et découpe.
- **art_box** : La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d’autres applications.
- **crop_box** : La boîte de rognage est la taille "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En mode normal, seul le contenu de la boîte de rognage est affiché dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, consultez la spécification Adobe.Pdf, en particulier la section 10.10.1 Limites de page.

Rogner le premier [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) d'un PDF vers une zone rectangulaire spécifique en utilisant Aspose.PDF for Python. La fonction ajuste plusieurs boîtes de page—`crop_box`, `trim_box`, `art_box`, et `bleed_box`—pour garantir des résultats visuels cohérents. Le recadrage peut être utile pour supprimer les marges indésirables ou se concentrer sur une zone particulière d’une page.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (utiliser `ap.Document()`).
1. Définissez le rectangle de rognage en utilisant [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) with the desired coordinates (in points).
1. Set the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, et `bleed_box` au rectangle défini.
1. Enregistrer le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers un nouveau fichier de sortie.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

Dans cet exemple, nous avons utilisé un fichier d'exemple [ici](crop_page.pdf). Initialement, notre page ressemble à ce qui est montré sur la Figure 1.
![Figure 1. Page recadrée](crop_page.png)

Après la modification, la page ressemblera à la Figure 2.
![Figure 2. Page recadrée](crop_page2.png)

## Recadrer la page PDF en fonction du contenu de la première image

Rogner le premier [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dynamiquement basé sur les limites de la première image trouvée sur la page. En utilisant [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), le script identifie la première image et ajuste la page `crop_box` pour correspondre aux dimensions de l’image. Cette approche est utile lorsque vous souhaitez vous concentrer sur un contenu visuel spécifique plutôt que sur des coordonnées prédéfinies.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Localiser les images sur la première page en utilisant [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Vérifier si des images existent :
    - Si trouvé, définissez le [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` pour correspondre à la première image [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Si non, conservez la page inchangée et avertissez l'utilisateur.
1. Enregistrer le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers le fichier de sortie spécifié.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Modifier la taille de la page PDF en Python](/pdf/fr/python-net/change-page-size/)
- [Obtenir et définir les propriétés des pages PDF en Python](/pdf/fr/python-net/get-and-set-page-properties/)
- [Faire pivoter les pages PDF en Python](/pdf/fr/python-net/rotate-pages/)