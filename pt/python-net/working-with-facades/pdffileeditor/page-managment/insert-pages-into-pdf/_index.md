---
title: Inserir páginas em PDF
type: docs
weight: 40
url: /pt/python-net/insert-pages-into-pdf/
description: Inserir páginas de um PDF em outro usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inserir páginas de outro PDF em um PDF existente em Python
Abstract: Aprenda como inserir páginas de um PDF em outro usando Aspose.PDF for Python. Este exemplo demonstra como adicionar páginas selecionadas de um PDF secundário em uma posição específica do documento original, criando um PDF combinado com posicionamento preciso das páginas.
---

Inserir páginas em um PDF existente é uma necessidade comum ao combinar documentos, adicionar conteúdo ou reorganizar relatórios. Usando Aspose.PDF for Python, os desenvolvedores podem inserir programaticamente páginas de um PDF em outro em um local especificado.

Este artigo mostra como usar o método insert da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. Ao especificar os números das páginas a inserir e a localização de destino, você pode mesclar conteúdo de diferentes PDFs enquanto mantém a formatação e a estrutura originais.

1. Crie um objeto PdfFileEditor.
1. Defina a Posição de Inserção e as Páginas.
1. Inserir Páginas.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
