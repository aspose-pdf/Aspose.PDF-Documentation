---
title: Extraction basée sur la région avec Python
linktitle: Extraction basée sur la région
type: docs
weight: 20
url: /fr/python-net/region-based-extraction/
description: Apprenez comment extraire du texte d'une région spécifique d'une page ou d'une structure de paragraphe dans des documents PDF avec Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire du texte d'une région spécifique d'une page

Utiliser [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) avec un [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) pour limiter l'extraction à une zone spécifique d'une page. Cette approche est utile pour l'extraction basée sur des zones à partir des en-têtes, pieds de page, cellules de tableau, champs de formulaire, factures, ou d'autres régions à mise en page fixe où la position du texte est connue à l'avance.

1. Ouvrez le PDF source en tant que [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer un `TextAbsorber` instance.
1. Configurer `text_search_options` pour limiter l'extraction à un rectangle.
1. Accepter l'absorbeur sur la page cible.
1. Écrire le texte extrait dans un fichier de sortie.

```python
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

## Extraire les paragraphes en les parcourant

Utiliser [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) lorsque vous avez besoin d'une extraction sensible aux paragraphes au lieu de texte de page simple. Contrairement [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) ou [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), cette API organise la sortie par page, section et paragraphe, ce qui est utile pour l'analyse de texte, l'exportation structurée et le traitement sensible à la mise en page.

1. Ouvrez le PDF source en tant que [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer un `ParagraphAbsorber` instance.
1. Appeler `absorber.visit(document)` pour analyser toutes les pages.
1. Parcourir `page_markups`, puis à travers chaque section et paragraphe.
1. Lire les fragments de texte de chaque paragraphe et écrire le résultat dans un fichier.

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extraire les paragraphes avec le rendu du polygone de délimitation

Vous pouvez également utiliser [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) pour inspecter la géométrie des paragraphes. En plus d’extraire le texte, cette approche enregistre chaque rectangle de section et chaque polygone de paragraphe, ce qui est utile pour la cartographie de la mise en page, l’analyse de documents, les outils d’accessibilité ou le post‑traitement sensible aux régions.

1. Ouvrez le PDF source en tant que [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créer un `ParagraphAbsorber` instance.
1. Visitez la page cible.
1. Lire le balisage de la page depuis `absorber.page_markups`.
1. Parcourez les sections et les paragraphes pour capturer la géométrie et le texte.
1. Écrivez les données du rectangle, du polygone et du texte dans le fichier de sortie.

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
