---
title: Adicionar Link de Aplicativo
type: docs
weight: 10
url: /pt/python-net/add-application-link/
description: Este exemplo vincula um PDF de entrada, adiciona um link de lançamento de aplicativo na primeira página e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um Link de Lançamento de Aplicativo a um PDF Usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link de lançamento de aplicativo a um documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como criar uma área clicável que abre um aplicativo especificado quando clicada, e salvar o PDF atualizado.
---

PDF pode incluir elementos interativos, como links que iniciam aplicativos externos. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir uma região retangular em uma página que, quando clicada, abre um arquivo executável específico.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina uma área retangular para o link clicável.
1. Especifique o caminho da aplicação a ser lançada.
1. Defina a cor do link.
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
