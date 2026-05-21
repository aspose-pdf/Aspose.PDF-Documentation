---
title: Adicionar link JavaScript
type: docs
weight: 30
url: /pt/python-net/add-javascript-link/
description: Este exemplo vincula um PDF de entrada, adiciona um link JavaScript que dispara um alerta ao ser clicado e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um link JavaScript a um PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link JavaScript a um documento PDF usando Aspose.PDF for Python via a API Facades. Ele mostra como criar uma área clicável que executa código JavaScript quando clicada e salvar o PDF atualizado.
---

Links JavaScript em PDFs permitem funcionalidades interativas, como exibir alertas, realizar cálculos ou modificar dinamicamente o conteúdo do documento. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um retângulo clicável em uma página e associá-lo a um código JavaScript personalizado.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o link JavaScript clicável.
1. Especifique o número da página e a cor do link.
1. Atribua o código JavaScript a ser executado ao clicar.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
