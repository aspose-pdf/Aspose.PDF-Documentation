---
title: Extraction basée sur les régions avec Python
linktitle: Extraction basée sur les régions
type: docs
weight: 20
url: /fr/python-net/region-based-extraction/
description: Cette section contient des articles sur l'extraction basée sur les régions de documents PDF à l'aide d'Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du texte d'une région spécifique d'une page

Extraire du texte d'une région rectangulaire définie sur une page particulière d'un PDF en utilisant Aspose.PDF pour Python. En spécifiant les coordonnées, vous pouvez concentrer l'extraction sur une zone spécifique — comme une cellule de tableau, un bloc de paragraphe ou une région de champ de formulaire.

Idéal pour l'extraction de texte basée sur des zones, comme l'extraction de données à partir des en-têtes, pieds de page, factures ou rapports à mise en page fixe où le texte apparaît à des emplacements prévisibles.

1. Ouvrez le document PDF.
1. Créez un 'TextAbsorber'.
1. Configurez 'text_search_options' pour restreindre à la région rectangulaire.
1. Appliquez l'absorbeur à la page spécifique.
1. Écrivez le texte extrait.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extraire des paragraphes en les parcourant

Nous pouvons obtenir le texte d'un document PDF en recherchant un texte particulier (en utilisant du "texte brut" ou des "expressions régulières") sur une page unique ou sur l'ensemble du document, ou nous pouvons obtenir le texte complet d'une page unique, d'une plage de pages ou du document complet. Cependant, dans certains cas, vous devez extraire des paragraphes d'un document PDF ou du texte sous forme de paragraphes. Nous avons implémenté une fonctionnalité de recherche de sections et de paragraphes dans le texte des pages de documents PDF. Nous avons introduit la classe ParagraphAbsorber (comme TextFragmentAbsorber et TextAbsorber), qui peut être utilisée pour extraire des paragraphes de documents PDF.

La bibliothèque Aspose.PDF vous permet de lire un fichier PDF et d'extraire tout le texte des paragraphes de chaque page en utilisant 'ParagraphAbsorber'. Elle organise la sortie par page, section et paragraphe, et écrit le contenu extrait dans un fichier texte brut. Cela est utile pour l'analyse de texte, l'archivage ou la conversion de contenu PDF structuré en formats lisibles.

1. Ouvrez le document PDF.
1. Instanciez un 'ParagraphAbsorber'.
1. Appelez 'absorber.visit(document)' pour analyser toutes les pages à la recherche de paragraphes.
1. Parcourez la collection 'page_markups' de l'absorbeur.
1. Pour chaque 'page‑markup', parcourez ses 'sections', puis chaque 'paragraph' dans la section.
1. À l'intérieur de chaque paragraphe, parcourez les 'lines', puis chaque 'fragment' dans la ligne, en accumulant 'fragment.text'.
1. Écrivez chaque paragraphe (avec les indices page/section/paragraphe) dans le fichier de sortie.
1. Fermez le document une fois terminé.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extraire des paragraphes avec rendu du polygone de délimitation

Ce fragment de code extrait le texte au niveau des paragraphes ainsi que les informations de mise en page d'une page spécifique d'un PDF. Il capture le rectangle de délimitation et les coordonnées du polygone de chaque paragraphe, ainsi que le contenu texte réel, et écrit les résultats dans un fichier texte. Cela est utile pour analyser la structure du document, la cartographie de la mise en page, ou préparer les données pour l'accessibilité et les tâches d'extraction de contenu.

1. Ouvrez le PDF et chargez le document.
1. Instanciez 'ParagraphAbsorber'.
1. Appelez 'absorber.visit(page)' pour la page spécifique souhaitée.
1. Récupérez le premier 'page_markup' depuis 'absorber.page_markups'.
1. Pour chaque section de ce markup :
- Récupérez son 'rectangle'.
1. Pour chaque paragraphe de la section :
- Obtenez ses 'points' (polygone).
- Extrayez le texte en parcourant 'paragraph.lines' - 'fragment.text'.
1. Écrivez les informations de géométrie et de texte dans le fichier de sortie.
1. Fermez le document.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

