---
title: Extraire les données vectorielles d'un fichier PDF à l'aide de Python
linktitle: Extraire les données vectorielles du PDF
type: docs
weight: 80
url: /fr/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilite l'extraction des données vectorielles d'un fichier PDF. Vous pouvez obtenir les données vectorielles (path, polygon, polyline), telles que la position, la couleur, l'épaisseur de ligne, etc.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Accéder aux données vectorielles d'un Document PDF

Utiliser [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) pour inspecter les éléments graphiques vectoriels sur une page de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Après avoir visité la page cible, parcourez les éléments extraits pour examiner les propriétés telles que les limites rectangulaires, les positions et les opérateurs de dessin.

1. Ouvrez le PDF source en tant que `Document`.
1. Créer un `GraphicsAbsorber` instance.
1. Appeler `gr_absorber.visit(page)` sur la page cible.
1. Lire les éléments extraits de `gr_absorber.elements`.
1. Itérez à travers les éléments et écrivez leurs propriétés dans un fichier de sortie.

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## Enregistrer les graphiques vectoriels d’une page dans un fichier SVG

Exporter les graphiques vectoriels d’une page PDF vers SVG afin de préserver les tracés et formes évolutifs en dehors du PDF d’origine. Cette méthode est utile pour réutiliser les illustrations vectorielles dans les flux de travail web, design ou édition.

1. Charger le document PDF.
1. Accédez à la page cible.
1. Appeler `page.try_save_vector_graphics()` exporter les chemins vectoriels de la page au format SVG.
1. Fermez le document.

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### Extraire chaque sous-chemin dans un SVG séparé

Lorsqu'une page contient plusieurs chemins vectoriels indépendants, utilisez [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) avec [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) pour écrire chaque sous-chemin dans un fichier SVG séparé.

1. Chargez le PDF.
1. Créer `SvgExtractionOptions` et définir `extract_every_subpath_to_svg`.
1. Accédez à la première page du document.
1. Instancier `SvgExtractor` avec les options.
1. Appeler `extractor.extract()` pour écrire des fichiers SVG séparés pour chaque sous-chemin vectoriel.
1. Fermez le document.

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Extraire une liste d'éléments en une seule image

Extraire plusieurs éléments vectoriels d'une page PDF et les enregistrer en une seule image SVG combinée. Ceci est utile lorsque vous souhaitez préserver la relation visuelle entre des formes groupées, des diagrammes ou des fragments de dessin.

1. Ouvrez le PDF en utilisant [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Sélectionnez une page et préparez une liste d'éléments vectoriels.
1. Utiliser [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) pour combiner ces éléments en un seul SVG.
1. Enregistrez le fichier de sortie.

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### Extraire un seul élément

Extraire un élément vectoriel spécifique d'un PDF et le sauvegarder en tant que fichier SVG individuel. Cela est utile pour isoler des logos, des icônes ou des formes autonomes à partir de pages plus complexes basées sur des vecteurs.

1. Créer un [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) pour capturer des données vectorielles.
1. Visitez une page spécifique pour collecter ses éléments vectoriels.
1. Sélectionnez un élément cible, tel un [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Enregistrez cet unique élément dans un fichier SVG.

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
