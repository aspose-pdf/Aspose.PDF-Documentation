---
title: Extraction de texte de base avec Python
linktitle: Extraction de texte de base
type: docs
weight: 10
url: /fr/python-net/basic-text-extraction/
description: Apprenez comment extraire du texte à partir de documents PDF en utilisant Aspose.PDF for Python — depuis toutes les pages à la fois ou depuis une page spécifique.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Utiliser [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) pour capturer tout le texte de chaque page d'un document PDF et l'écrire dans un fichier texte. Cette approche convient parfaitement à la conversion de PDF en texte interrogeable, à l'analyse du contenu ou à la préparation du texte pour l'indexation et le traitement en aval.

1. Ouvrez le document PDF en utilisant [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Créer un `TextAbsorber` instance.
1. Appeler `document.pages.accept(text_absorber)` scanner toutes les pages.
1. Récupérer le texte extrait de `text_absorber.text`.
1. Écrivez le résultat dans un fichier texte de sortie.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Extraire le texte d'une page particulière

Appliquer [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) vers une seule page pour isoler et enregistrer le texte de cette section d'un document multipage. Ceci est utile lorsque vous avez besoin du contenu d'une seule page — par exemple, une facture, une section de rapport ou un résumé de formulaire.

1. Ouvrez le document PDF en utilisant [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Créer un `TextAbsorber` instance.
1. Appeler `accept` sur la page cible : `document.pages[page_number].accept(text_absorber)`.
1. Récupérez le texte extrait et écrivez‑le dans un fichier.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
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