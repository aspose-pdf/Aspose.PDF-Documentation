---
title: Adicionar Anotações Pop-up
type: docs
weight: 40
url: /pt/python-net/add-popup-annotation/
description: Este exemplo carrega um PDF, adiciona uma anotação pop-up à primeira página e salva o documento modificado. O pop-up está configurado para ser visível por padrão e exibe o texto de comentário especificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Anotações Pop-up a um PDF Usando Python
Abstract: Este exemplo demonstra como inserir uma anotação pop-up em um documento PDF usando Aspose.PDF for Python via a Facades API. Ele explica como definir a área do pop-up, definir o texto da anotação, controlar a visibilidade e salvar o documento atualizado.
---

Anotações pop-up são úteis para adicionar comentários, explicações ou notas interativas em arquivos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode criar anotações pop-up programaticamente especificando a localização, o conteúdo, a visibilidade e o número da página.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Defina o retângulo da Anotação Popup.
1. Adicione a Anotação Popup.
1. Salvar o Document atualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
