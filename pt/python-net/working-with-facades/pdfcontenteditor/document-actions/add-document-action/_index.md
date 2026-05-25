---
title: Adicionar Ação de Documento
type: docs
weight: 20
url: /pt/python-net/add-document-action/
description: Este exemplo adiciona um alerta JavaScript que aparece quando o PDF é aberto. O script está anexado ao evento de abertura do documento e é executado automaticamente em visualizadores de PDF compatíveis.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Ação JavaScript de Abertura de Documento a um PDF Usando Python
Abstract: Este exemplo demonstra como adicionar uma ação JavaScript ao nível do documento que é acionada quando um PDF é aberto. Usando Aspose.PDF for Python via the Facades API, o exemplo mostra como vincular um documento, atribuir uma ação de evento de abertura e salvar o PDF atualizado.
---

Ações ao nível do documento permitem que você defina comportamentos que são executados automaticamente quando determinados eventos ocorrem, como a abertura de um PDF. Com [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), você pode anexar código JavaScript a esses eventos. Isso pode ser usado para notificações, lógica de validação ou fluxos de trabalho interativos.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Adicionar ação em nível de documento.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
