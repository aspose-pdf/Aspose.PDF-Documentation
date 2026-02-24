---
title: Suppression de pages PDF programmatiquement avec Python
linktitle: Suppression de pages PDF
type: docs
weight: 80
url: /fr/python-net/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant la bibliothèque Aspose.PDF pour Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment supprimer des pages d’un PDF avec Python
Abstract: Cet article fournit un guide concis sur la façon de supprimer des pages d'un fichier PDF à l'aide de la bibliothèque Aspose.PDF pour Python via .NET. Il se concentre sur l'utilisation de la classe `PageCollection` pour supprimer des pages spécifiques. Le processus consiste à appeler la méthode `delete()` avec l'indice de la page à supprimer, puis à enregistrer le document mis à jour avec la méthode `save()`. De plus, un extrait de code est fourni pour démontrer la suppression d'une page d'un fichier PDF, illustrant l'utilisation de la bibliothèque Aspose.PDF dans un contexte pratique.
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant Aspose.PDF pour Python via .NET. Pour supprimer une page particulière, utilisez le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) d'un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

## Supprimer une page d'un fichier PDF

Aspose.PDF for Python via .NET supprime la page 2 du PDF d'entrée et enregistre le document mis à jour dans un nouveau fichier. Cette fonctionnalité est utile pour supprimer des pages indésirables ou sensibles sans modifier le reste du document.

1. Chargez le PDF d'entrée en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Supprimez la page en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Appelez la méthode [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pour enregistrer le fichier PDF mis à jour.

L'extrait de code suivant montre comment supprimer une page particulière du fichier PDF en utilisant Python.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## Supprimer plusieurs pages d'un document PDF

La suppression de plusieurs pages vous permet de retirer un ensemble de pages spécifiées en une seule opération, ce qui est plus efficace que de supprimer les pages une par une. Le PDF résultant est enregistré dans un nouveau fichier, préservant le document original.

1. Chargez le PDF d'entrée en tant que [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Supprimez les pages listées dans le tableau pages en utilisant le [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mis à jour dans un nouveau fichier.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

