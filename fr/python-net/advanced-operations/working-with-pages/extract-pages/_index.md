---
title: Extraction de pages par programmation Python
linktitle: Extraction de pages PDF
type: docs
weight: 80
url: /fr/python-net/extract-pages/
description: Vous pouvez extraire des pages de votre fichier PDF en utilisant la bibliothèque Aspose.PDF pour Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des pages PDF en utilisant Python
Abstract: Cet article montre comment extraire des pages d'un document PDF en utilisant la bibliothèque Aspose.PDF pour Python. Les techniques couvrent à la fois l'extraction d'une seule page et l'extraction de plusieurs pages, permettant aux développeurs de créer de nouveaux fichiers PDF ne contenant que les pages sélectionnées. Les exemples illustrent comment accéder à des pages spécifiques par indexation à partir de 1, les copier dans un nouveau document PDF et enregistrer le résultat tout en conservant le document original intact. Ces méthodes sont utiles pour diviser de grands documents, partager des sections sélectionnées ou créer des sous‑ensembles PDF personnalisés pour la distribution ou l'analyse.
---

## Extraire une seule page d'un PDF

Extraire une page spécifique d'un document PDF et l'enregistrer comme un nouveau fichier. En utilisant la bibliothèque Aspose.PDF, le script copie la page désirée dans un nouveau PDF, laissant le document original inchangé. Cela est utile pour scinder les PDF ou isoler des pages importantes pour la distribution.

1. Chargez le PDF source en utilisant l'API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour contenir la page extraite.
1. Ajoutez la [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) souhaitée du document source au nouveau PDF en utilisant la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) du document de destination (`dst_document.pages.add(...)`).
- Dans cet exemple, la page 2 est extraite (indexation à partir de 1).
1. Enregistrez le nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contenant la page extraite dans le fichier de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## Extraire plusieurs pages d'un PDF

Extraire plusieurs pages spécifiques d'un document PDF et les enregistrer dans un nouveau fichier. En utilisant la bibliothèque Aspose.PDF, les pages sélectionnées sont copiées dans un nouveau PDF tout en laissant le document original intact. Cela est utile pour créer des PDF plus petits contenant uniquement les sections pertinentes d'un document plus volumineux.

1. Chargez le PDF source en utilisant l'API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Créez un nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pour contenir les pages extraites.
1. Sélectionnez les pages à extraire (dans cet exemple, les pages 2 et 3 en utilisant une indexation à partir de 1).
1. Ajoutez chaque [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) sélectionnée du document source au nouveau PDF en utilisant sa [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le nouveau [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) contenant les pages extraites dans le fichier de sortie spécifié.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```
