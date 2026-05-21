---
title: Anexar páginas ao PDF
type: docs
weight: 10
url: /pt/python-net/append-pages-to-pdf/
description: Anexar páginas de um documento PDF a outro usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anexar páginas de um PDF a outro em Python
Abstract: Aprenda como anexar páginas de um documento PDF a outro usando Aspose.PDF for Python. Este exemplo demonstra como usar a classe PdfFileEditor para combinar páginas de vários PDFs e criar um único documento de saída.
---

Combinar páginas de diferentes documentos PDF é uma necessidade comum em fluxos de trabalho de processamento de documentos. Usando Aspose.PDF for Python, os desenvolvedores podem facilmente anexar páginas de um ou mais arquivos PDF a um documento existente.

Este trecho de código mostra como usar o método append de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para adicionar páginas selecionadas de outro arquivo PDF ao final de um PDF de origem. Ao especificar o intervalo de páginas, os desenvolvedores podem controlar exatamente quais páginas são incluídas no documento final.

1. Crie um objeto PdfFileEditor.
1. Anexar Páginas de Outro PDF.

As páginas especificadas do documento PDF secundário são anexadas ao final do PDF original, criando um arquivo de saída combinado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
