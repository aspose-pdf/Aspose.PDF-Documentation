---
title: Excluindo páginas de PDF programaticamente em Python
linktitle: Excluindo Páginas de PDF
type: docs
weight: 80
url: /pt/python-net/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando a biblioteca Aspose.PDF for Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como excluir páginas de PDF usando Python
Abstract: Este artigo fornece um guia conciso sobre como excluir páginas de um arquivo PDF usando a biblioteca Aspose.PDF para Python via .NET. Ele se concentra em utilizar a classe `PageCollection` para remover páginas específicas. O processo envolve invocar o método `delete()` com o índice da página a ser removida e, em seguida, salvar o documento atualizado com o método `save()`. Além disso, um trecho de código é fornecido para demonstrar a exclusão de uma página de um arquivo PDF, ilustrando o uso da biblioteca Aspose.PDF em um contexto prático.
---

Você pode excluir páginas de um arquivo PDF usando o Aspose.PDF for Python via .NET. Para excluir uma página específica, use a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

## Excluir Página de Arquivo PDF

Aspose.PDF for Python via .NET exclui a página 2 do PDF de entrada e salva o documento atualizado em um novo arquivo. Este recurso é útil para remover páginas indesejadas ou sensíveis sem alterar o resto do documento.

1. Carregue o PDF de entrada como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Exclua a página usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Chame o método [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para salvar o arquivo PDF atualizado.

O trecho de código a seguir mostra como excluir uma página específica do arquivo PDF usando Python.

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

## Excluir Múltiplas Páginas de um Documento PDF

Excluir múltiplas páginas permite remover um conjunto de páginas especificadas em uma única operação, o que é mais eficiente do que excluir páginas uma a uma. O PDF resultante é salvo em um novo arquivo, preservando o documento original.

1. Carregue o PDF de entrada como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Exclua as páginas listadas no array de páginas usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) atualizado em um novo arquivo.

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

