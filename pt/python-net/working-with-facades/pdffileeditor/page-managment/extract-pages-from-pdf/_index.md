---
title: Extrair Páginas de PDF
type: docs
weight: 30
url: /pt/python-net/extract-pages-from-pdf/
description: Extrair páginas selecionadas de um documento PDF usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair Páginas Específicas de um Documento PDF em Python
Abstract: Aprenda como extrair páginas selecionadas de um documento PDF usando Aspose.PDF for Python. Este exemplo demonstra como criar um novo PDF contendo apenas as páginas que você precisa, permitindo a criação de documentos personalizados e a manipulação de nível de página.
---

Extrair páginas de um PDF é útil quando você precisa criar um subconjunto de um documento, compartilhar apenas conteúdo específico ou reorganizar PDFs para apresentações, relatórios ou impressão. Usando Aspose.PDF for Python, os desenvolvedores podem extrair programaticamente páginas de um arquivo PDF e salvá-las como um novo documento.

Aprenda como usar o método extract de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. Ao especificar uma lista de páginas para extrair, você pode gerar um novo PDF contendo apenas as páginas selecionadas, preservando o conteúdo e a formatação originais.

1. Crie um objeto PdfFileEditor.
1. Definir Páginas para Extrair.
1. Extrair as Páginas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
