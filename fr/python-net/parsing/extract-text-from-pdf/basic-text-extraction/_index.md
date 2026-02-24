---
title: Extraction de texte de base avec Python
linktitle: Extraction de texte de base
type: docs
weight: 10
url: /fr/python-net/basic-text-extraction/
description: Cette section contient des articles sur l'extraction de texte de base à partir de documents PDF en utilisant Aspose.PDF avec Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Aspose.PDF pour Python vous montre comment extraire le texte de chaque page d'un document PDF. Il utilise la classe TextAbsorber pour capturer tout le contenu textuel du document entier et l'enregistre dans un fichier texte séparé.
Idéal pour convertir les PDF en texte interrogeable, effectuer une analyse de contenu ou exporter du texte pour des tâches d'indexation et de traitement.

1. Charger le fichier PDF.
1. Créer un objet 'TextAbsorber'.
1. Appeler 'document.pages.accept(text_absorber)' afin qu'il analyse toutes les pages.
1. Obtenir le texte complet via 'text_absorber.text'.
1. Écrire le résultat dans un fichier texte.

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
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extraire le texte d'une page particulière

Extraire le texte d'une seule page d'un document PDF. En appliquant le TextAbsorber uniquement à une page spécifiée, vous pouvez isoler et enregistrer le texte d'une section particulière d'un PDF multipage.

Utile lorsque vous n'avez besoin que du contenu d'une page — par exemple, extraire le texte d'une page de facture, d'une section de rapport ou d'un résumé de champ de formulaire.

1. Ouvrir le PDF.
1. Créer un TextAbsorber.
1. Accepter uniquement la page désignée (pages[page_number]).
1. Extraire le texte et l'écrire dans un fichier.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

