---
title: Modifier la taille de la page PDF en Python
linktitle: Modification de la taille de la page
type: docs
weight: 40
url: /fr/python-net/change-page-size/
description: Apprenez comment lire et modifier les dimensions de page PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modification de la taille de la page avec Python
Abstract: Cet article montre comment lire et modifier les dimensions des pages PDF à l'aide d'Aspose.PDF. L'exemple Get Page Size récupère la largeur et la hauteur d'une page PDF spécifique, permettant aux utilisateurs d'inspecter la disposition des pages, de valider le formatage ou d'analyser la structure du document. L'exemple Set Page Size montre comment changer les dimensions d'une page—par exemple en convertissant la première page au format A4—tout en affichant les propriétés des boîtes (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) avant et après la modification.
---

Aspose.PDF for Python via .NET vous permet de modifier la taille des pages PDF avec quelques lignes de code. Ce sujet montre comment mettre à jour les dimensions des pages en utilisant le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API.

Utilisez ce guide lorsque vous devez redimensionner les pages PDF existantes, normaliser les dimensions du document ou inspecter les paramètres de boîte de page en Python.

{{% alert color="primary" %}}

Veuillez noter que les propriétés hauteur et largeur utilisent les points comme unité de base, où 1 pouce = 72 points et 1 cm = 1/2,54 pouce = 0,3937 pouce = 28,3 points.

{{% /alert %}}

## Définir la taille de page d'une page PDF à A4

L’exemple met à jour la taille de la première page d’un document PDF aux dimensions standard A4. Il affiche également les dimensions des boîtes de la page (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) avant et après le redimensionnement afin que vous puissiez vérifier les modifications.

Le fragment de code suivant montre comment modifier les dimensions de la page PDF au format A4 :

1. Accédez au premier [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) du [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Affichez les tailles des boîtes de la page avant modification (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Appliquez les dimensions A4 (597.6 × 842.4 points) à l'aide de l'API de page.
1. Affichez les tailles de boîte de page mises à jour.
1. Enregistrer le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers le chemin de sortie spécifié.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

Cet extrait lit un PDF et récupère les dimensions (largeur et hauteur) de la première page. Il utilise le [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API pour extraire les limites de la page [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) et affiche sa taille dans la console. Ceci est utile pour inspecter la mise en page, vérifier les formats ou préparer les documents pour un traitement ultérieur.

1. Chargez le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Accédez au premier [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Récupérer le rectangle englobant de la page en utilisant `get_page_rect()`.
1. Extrayez les valeurs de largeur et de hauteur.
1. Imprimez les dimensions de la page.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obtenir la taille de la page PDF avant et après la rotation

Récupérez les dimensions d’une page PDF avant et après l’application d’une rotation de 90°. Cela démontre comment la rotation affecte la largeur et la hauteur et comment l’utiliser. `get_page_rect()` avec ou sans prise en compte de la rotation.

1. Ouvrir le PDF en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Accédez au premier [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Appliquer une rotation de 90° en utilisant `page.rotate = ap.Rotation.ON90` (voir le [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Récupérer le rectangle de la page sans rotation en utilisant `get_page_rect(False)` et affiche sa largeur et sa hauteur.
1. Récupérer le rectangle de la page en tenant compte de la rotation en utilisant `get_page_rect(True)` et affiche sa largeur et sa hauteur.
1. Comparez comment les dimensions changent en raison de la rotation.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Recadrer les pages PDF en Python](/pdf/fr/python-net/crop-pages/)
- [Obtenir et définir les propriétés des pages PDF en Python](/pdf/fr/python-net/get-and-set-page-properties/)
- [Faire pivoter les pages PDF en Python](/pdf/fr/python-net/rotate-pages/)