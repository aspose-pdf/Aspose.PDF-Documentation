---
title: Adicionar Anotação de Filme
type: docs
weight: 10
url: /pt/python-net/add-movie-annotation/
description: Este exemplo associa um PDF de entrada, adiciona uma anotação de filme na página 1 e salva o PDF atualizado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar uma Anotação de Filme a um PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como incorporar um filme (vídeo) em um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como adicionar uma anotação clicável que reproduz um vídeo diretamente no PDF.
---

Anotações de filme em PDFs permitem incorporar conteúdo multimídia, como vídeos, em seus documentos. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um retângulo em uma página onde o vídeo aparecerá. Quando clicado, o vídeo pode ser reproduzido diretamente do PDF, tornando seus documentos mais interativos e envolventes.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para a anotação de filme.
1. Especifique o arquivo de vídeo a incorporar.
1. Atribua o número da página para a anotação.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
