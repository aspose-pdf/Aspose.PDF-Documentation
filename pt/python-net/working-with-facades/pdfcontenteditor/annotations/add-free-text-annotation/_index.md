---
title: Adicionar Anotações de Texto Livre
type: docs
weight: 20
url: /pt/python-net/add-free-text-annotation/
description: Este exemplo carrega um arquivo PDF existente, adiciona uma anotação de texto livre à primeira página em uma posição definida e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotação de Texto Livre a um PDF Usando Python
Abstract: Este exemplo demonstra como inserir uma anotação de texto livre em um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como vincular um PDF, definir a posição da anotação, adicionar texto personalizado e salvar o documento atualizado.
---

Anotações de texto livre permitem que você coloque texto visível diretamente em uma página PDF sem a necessidade de comentários pop-up. Usando PdfContentEditor, você pode especificar o retângulo da anotação, o texto exibido e a página de destino.

1. Criar o [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular o PDF de entrada.
1. Defina a posição da anotação.
1. Adicionar a Anotação de Texto Livre.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
