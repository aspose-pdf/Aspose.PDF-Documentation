---
title: Adicionar Carimbo de Borracha
type: docs
weight: 10
url: /pt/python-net/add-rubber-stamp/
description: Este exemplo vincula um PDF de entrada, adiciona um carimbo de borracha verde “Approved” nas quatro primeiras páginas e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar uma Anotação de Carimbo de Borracha a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar uma anotação de carimbo de borracha a um documento PDF usando Aspose.PDF for Python via a API Facades. Carimbos de borracha permitem marcar visualmente páginas com aprovações, revisões ou rótulos personalizados.
---

Anotações de carimbo de borracha são comumente usadas em PDFs para indicar aprovação, status de revisão ou outras notas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um retângulo para o carimbo, definir seu texto e comentários, escolher uma cor e aplicá-lo a várias páginas de um documento.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Percorra as páginas 1–34.
1. Adicione uma anotação de selo de borracha com texto personalizado, comentários e cor.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
