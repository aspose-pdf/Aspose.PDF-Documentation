---
title: Adicionar link de documento PDF
type: docs
weight: 50
url: /pt/python-net/add-pdf-document-link/
description: Este exemplo associa um PDF de entrada, adiciona um link de cor verde a uma página em outro PDF e salva o documento modificado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar um link de documento PDF usando PdfContentEditor em Python
Abstract: Este exemplo demonstra como adicionar um link a outro documento PDF usando Aspose.PDF for Python via the Facades API. Ele mostra como criar uma área clicável que abre um PDF diferente e salvar o documento atualizado.
---

Links de documentos PDF permitem que os usuários naveguem de um PDF para outro de forma contínua. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode definir um retângulo clicável que vincula a uma página em um arquivo PDF diferente, tornando seus documentos interativos e conectados.

1. Crie uma instância de PdfContentEditor.
1. Vincule o documento PDF de entrada.
1. Defina um retângulo para o link clicável.
1. Specifie o arquivo PDF vinculado, a página de origem e a página de destino.
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


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
