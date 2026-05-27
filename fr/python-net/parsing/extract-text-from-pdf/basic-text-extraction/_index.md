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
