---
title: Substituir Imagens em PDF
type: docs
weight: 30
url: /pt/python-net/replace-image/
description: Este exemplo vincula um PDF de entrada, substitui a primeira imagem na página 1 por uma nova imagem e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Substituir uma Imagem em um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como substituir uma imagem existente em um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como direcionar uma imagem específica em uma página e substituí‑la por uma nova imagem, e então salvar o PDF atualizado.
---

Os PDFs frequentemente contêm imagens que podem precisar ser atualizadas ou substituídas, como logotipos, diagramas ou fotos. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode substituir uma imagem específica em uma página determinada fornecendo o número da página, o índice da imagem e o caminho do novo arquivo de imagem.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Substitua uma imagem específica em uma página determinada.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
