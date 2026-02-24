---
title: Extração de Texto Básica usando Python
linktitle: Extração de Texto Básica
type: docs
weight: 10
url: /pt/python-net/basic-text-extraction/
description: Esta seção contém artigos sobre extração básica de texto de documentos PDF usando Aspose.PDF em Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extrair texto de todas as páginas de um documento PDF

Aspose.PDF para Python ensina como extrair texto de cada página de um documento PDF. Ele usa a classe TextAbsorber para capturar todo o conteúdo textual do documento inteiro e salvá-lo em um arquivo de texto separado.
Ideal para converter PDFs em texto pesquisável, realizar análise de conteúdo ou exportar texto para tarefas de indexação e processamento.

1. Carregue o arquivo PDF.
1. Crie um objeto 'TextAbsorber'.
1. Chame 'document.pages.accept(text_absorber)' para que ele escaneie todas as páginas.
1. Obtenha o texto completo via 'text_absorber.text'.
1. Grave o resultado em um arquivo de texto.

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

## Extrair texto de uma página específica

Extraia texto de uma única página de um documento PDF. Ao aplicar o TextAbsorber apenas a uma página especificada, você pode isolar e salvar o texto de uma seção específica de um PDF de várias páginas.

Útil quando você precisa apenas do conteúdo de uma página — por exemplo, extrair texto da página de uma fatura, seção de relatório ou resumo de campo de formulário.

1. Abra o PDF.
1. Crie um TextAbsorber.
1. Aceite somente a página designada (pages[page_number]).
1. Extraia o texto e grave em um arquivo.

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

