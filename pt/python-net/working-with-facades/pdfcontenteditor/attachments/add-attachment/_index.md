---
title: Adicionar anexo
type: docs
weight: 10
url: /pt/python-net/add-attachment/
description: Este exemplo vincula um PDF de entrada, anexa um arquivo externo à primeira página e salva o PDF modificado com o anexo incorporado.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar anexos de arquivo a um PDF usando Python
Abstract: Este exemplo demonstra como anexar arquivos externos a um documento PDF usando Aspose.PDF for Python via a Facades API. Ele mostra como vincular um PDF, adicionar anexos com descrições e salvar o documento atualizado.
---

Os anexos de arquivo em PDFs permitem incluir documentos suplementares, imagens ou outros recursos diretamente no PDF. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode anexar arquivos programaticamente a páginas específicas, definir o nome do anexo e fornecer uma descrição.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Abra o arquivo Attachment.
1. Adicione o Attachment ao PDF.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
