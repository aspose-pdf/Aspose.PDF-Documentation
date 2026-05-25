---
title: Adicionar link da Web
type: docs
weight: 60
url: /pt/python-net/add-web-link/
description: Este exemplo associa um PDF de entrada, adiciona uma anotação de link da web azul na página 1 apontando para a página do produto Python PDF da Aspose, e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um link da Web a um PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link da web a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como criar uma área clicável em uma página que abre um URL especificado em um navegador web e salvar o documento atualizado.
---

Links da Web em PDFs permitem que os usuários naveguem diretamente para recursos online, sites ou documentação. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir uma área retangular em uma página PDF que, ao ser clicada, abre um URL no navegador padrão.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o link da web clicável.
1. Especifique o URL, número da página e cor do link.
1. Salve o documento PDF atualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
