---
title: Excluir Imagens de PDF
type: docs
weight: 20
url: /pt/python-net/delete-images/
description:
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir Imagens Específicas de uma Página PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como excluir imagens específicas de um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como direcionar imagens em uma página específica e salvar o documento atualizado.
---

Às vezes, você pode querer remover apenas certas imagens de um PDF em vez de limpar todos os elementos visuais. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode excluir imagens selecionadas especificando o número da página e o índice da imagem.

Este trecho de código vincula um PDF de entrada, exclui a segunda imagem na página 1 e salva o PDF modificado, deixando as demais imagens intactas.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Exclua imagens específicas de uma página designada.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
