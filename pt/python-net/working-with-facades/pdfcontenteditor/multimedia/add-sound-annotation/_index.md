---
title: Adicionar Anotação de Som
type: docs
weight: 20
url: /pt/python-net/add-sound-annotation/
description: Este exemplo vincula um PDF de entrada, adiciona uma anotação de som na página 1 e salva o PDF modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar uma Anotação de Som a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como incorporar áudio em um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como adicionar uma anotação de som clicável que reproduz um arquivo de áudio diretamente no PDF.
---

Anotações de som em PDFs permitem que você adicione conteúdo de áudio, como notas de voz, música ou efeitos sonoros aos seus documentos. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um pequeno retângulo clicável em uma página que reproduz um arquivo de áudio especificado quando ativado.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para a anotação de som.
1. Especifique o arquivo de áudio, o nome da anotação, o número da página e a taxa de amostragem.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
