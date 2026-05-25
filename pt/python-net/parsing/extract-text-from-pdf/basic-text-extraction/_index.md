---
title: Extração Básica de Texto usando Python
linktitle: Extração Básica de Texto
type: docs
weight: 10
url: /pt/python-net/basic-text-extraction/
description: Aprenda como extrair texto de documentos PDF usando Aspose.PDF for Python — de todas as páginas de uma vez ou de uma página específica.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair texto de todas as páginas de um documento PDF

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) capturar todo o texto de cada página de um documento PDF e gravá-lo em um arquivo de texto. Essa abordagem é bem adequada para converter PDFs em texto pesquisável, executar análise de conteúdo ou preparar o texto para indexação e processamento subsequente.

1. Abra o documento PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Criar um `TextAbsorber` instância.
1. Chamar `document.pages.accept(text_absorber)` para escanear todas as páginas.
1. Recuperar o texto extraído de `text_absorber.text`.
1. Grave o resultado em um arquivo de texto de saída.

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

## Extrair texto de uma página específica

Aplicar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) para uma única página para isolar e salvar o texto daquela seção de um documento de várias páginas. Isso é útil quando você precisa de conteúdo de apenas uma página — por exemplo, uma fatura, uma seção de relatório ou um resumo de formulário.

1. Abra o documento PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Criar um `TextAbsorber` instância.
1. Chamar `accept` na página de destino: `document.pages[page_number].accept(text_absorber)`.
1. Recupere o texto extraído e escreva-o em um arquivo.

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
