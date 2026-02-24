---
title: Extraindo Páginas programaticamente em Python
linktitle: Extraindo Páginas PDF
type: docs
weight: 80
url: /pt/python-net/extract-pages/
description: Você pode extrair páginas do seu arquivo PDF usando a biblioteca Aspose.PDF para Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair páginas PDF usando Python
Abstract: Este artigo demonstra como extrair páginas de um documento PDF usando a biblioteca Aspose.PDF para Python. As técnicas cobrem tanto a extração de uma única página quanto a extração de múltiplas páginas, permitindo que desenvolvedores criem novos arquivos PDF contendo apenas as páginas selecionadas. Os exemplos ilustram como acessar páginas específicas usando indexação baseada em 1, copiá‑las para um novo documento PDF e salvar os resultados mantendo o documento original intacto. Esses métodos são úteis para dividir documentos grandes, compartilhar seções selecionadas ou criar subconjuntos de PDF personalizados para distribuição ou análise.
---

## Extrair uma página única de um PDF

Extrair uma página específica de um documento PDF e salvá‑la como um novo arquivo. Usando a biblioteca Aspose.PDF, o script copia a página desejada para um novo PDF, mantendo o documento original inalterado. Isso é útil para dividir PDFs ou isolar páginas importantes para distribuição.

1. Carregue o PDF fonte usando a API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para armazenar a página extraída.
1. Adicione a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) desejada do documento fonte ao novo PDF usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do documento de destino (`dst_document.pages.add(...)`).
- Neste exemplo, a página 2 é extraída (indexação baseada em 1).
1. Salve o novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com a página extraída no arquivo de saída especificado.

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

## Extrair múltiplas páginas de um PDF

Extrair várias páginas específicas de um documento PDF e salvá‑las em um novo arquivo. Usando a biblioteca Aspose.PDF, as páginas selecionadas são copiadas para um novo PDF, mantendo o documento original intacto. Isso é útil para criar PDFs menores contendo apenas as seções relevantes de um documento maior.

1. Carregue o PDF fonte usando a API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (`ap.Document()`).
1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para armazenar as páginas extraídas.
1. Selecione as páginas a extrair (neste exemplo, as páginas 2 e 3 usando indexação baseada em 1).
1. Adicione cada [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) selecionada do documento fonte ao novo PDF usando sua [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com as páginas extraídas no arquivo de saída especificado.

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
