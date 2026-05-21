---
title: Redimensionar Conteúdo da Página PDF
type: docs
weight: 30
url: /pt/python-net/resize-pdf-page-contents/
description: Redimensione o conteúdo de páginas PDF específicas usando Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionar Conteúdo da Página PDF Programaticamente em Python
Abstract: Aprenda como redimensionar o conteúdo de páginas PDF específicas usando Aspose.PDF for Python. Este exemplo demonstra como ajustar a largura e a altura do conteúdo da página enquanto preserva a estrutura do documento, facilitando a otimização de layouts para impressão ou visualização.
---

Ajustar o tamanho do conteúdo da página PDF é frequentemente necessário ao preparar documentos para impressão, adaptar o conteúdo a um layout específico ou padronizar os formatos de página em um documento. Usando Aspose.PDF for Python, os desenvolvedores podem redimensionar o conteúdo de páginas selecionadas programaticamente sem editar manualmente o documento.

Este artigo mostra como usar o método \u0027resize_contents\u0027 de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para modificar as dimensões do conteúdo da página para páginas específicas em um arquivo PDF. Ao especificar a largura e a altura desejadas, o conteúdo nas páginas selecionadas é redimensionado de acordo.

1. Crie um objeto PdfFileEditor.
1. Redimensionar Conteúdos da Página.

Parâmetros:

- [1, 3] – lista de números de página cujos conteúdos serão redimensionados.
- 400 – a nova largura do conteúdo da página (em pontos).
- 750 – a nova altura do conteúdo da página (em pontos).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
