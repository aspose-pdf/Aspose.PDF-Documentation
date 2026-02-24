---
title: Extraire des données vectorielles d'un fichier PDF à l'aide de Python
linktitle: Extraire des données vectorielles du PDF
type: docs
weight: 80
url: /fr/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilite l'extraction de données vectorielles d'un fichier PDF. Vous pouvez obtenir les données vectorielles (chemin, polygone, polyligne), telles que la position, la couleur, l'épaisseur du trait, etc.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Accès aux données vectorielles du document PDF

L'extrait de code suivant utilise la classe GraphicsAbsorber pour montrer comment extraire des éléments graphiques vectoriels d'une page spécifique d'un document PDF et examiner des propriétés telles que les limites du rectangle, les opérateurs et les positions.

1. Charger le document PDF en utilisant 'ap.Document'.
1. Initialiser une instance de 'GraphicsAbsorber'.
1. Appeler 'gr_absorber.visit()' pour inspecter la deuxième page.
1. Récupérer les éléments extraits via 'gr_absorber.elements'.
1. Parcourir chaque élément et enregistrer les propriétés - rectangle, position et nombre d'opérateurs.
1. Écrire les informations dans un fichier texte de sortie.
1. Fermer le document pour libérer les ressources.

```python

import os
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
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## Enregistrer les graphiques vectoriels d'une page dans un fichier SVG

Exporter les graphiques vectoriels d'une page PDF dans un fichier SVG, en conservant les formes et chemins vectoriels :

1. Charger le document PDF.
1. Accéder à la page cible().
1. Appeler 'page.try_save_vector_graphics()' qui exporte les chemins vectoriels de la page dans un fichier SVG.
1. Fermer le document.

```python

import os
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

Extraire chaque sous-chemin (composant) des graphiques vectoriels dans des fichiers SVG distincts en utilisant un objet d'options d'extraction.

1. Charger le PDF.
1. Créer 'SvgExtractionOptions' et définir 'extract_every_subpath_to_svg'.
1. Accéder à la première page du document.
1. Instancier 'SvgExtractor' avec les options.
1. Appeler 'extractor.extract()' pour générer des fichiers SVG séparés pour chaque sous-chemin vectoriel.
1. Fermer le document.

```python

import os
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

### Extraire la liste des éléments en une seule image

Extraire plusieurs éléments vectoriels d'une page PDF et les enregistrer comme une image SVG combinée unique en utilisant Aspose.PDF pour Python.
Ceci est utile lorsque vous souhaitez conserver la structure visuelle de formes ou de dessins groupés, tels que des diagrammes ou des exportations CAD.

1. Ouvrir le PDF en utilisant 'Document'.
1. Sélectionner une page et préparer une liste d'éléments vectoriels.
1. Utiliser 'SvgExtractor' pour combiner ces éléments en un SVG.
1. Enregistrer le fichier de sortie.

```python

import os
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

Extraire un élément vectoriel spécifique d'un PDF et l'enregistrer comme un fichier SVG individuel.
Cela est bénéfique pour isoler et exporter des logos, icônes ou formes autonomes à partir de PDFs complexes basés sur des vecteurs.

1. Créer un 'GraphicsAbsorber' pour capturer les données vectorielles.
1. Visiter une page spécifique pour collecter ses éléments vectoriels.
1. Sélectionner un élément cible (par ex., un 'XFormPlacement').
1. Enregistrer cet élément unique dans un fichier SVG.

```python

import os
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
