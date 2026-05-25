---
title: Remover Ação de Abertura
type: docs
weight: 30
url: /pt/python-net/remove-open-action/
description: Este exemplo carrega um PDF existente, remove a ação de abertura e salva o documento limpo.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Ação de Abertura de Documento de um PDF Usando Python
Abstract: Este exemplo demonstra como remover uma ação de abertura de documento de um PDF usando Aspose.PDF for Python via a Facades API. Ele mostra como vincular um PDF, limpar a ação de abertura e salvar o documento atualizado.
---

Documentos PDF podem conter ações que são executadas automaticamente quando o arquivo é aberto, como alertas de JavaScript, comandos de navegação ou outros comportamentos. Em alguns cenários, pode ser necessário remover essas ações por razões de segurança, conformidade ou experiência do usuário.

Usando PdfContentEditor, você pode remover facilmente a ação de abertura do documento e garantir que o PDF abra sem executar nenhum comportamento automático.

1. Crie o objeto PdfContentEditor.
1. Vincular o PDF de entrada.
1. Remover a ação de abertura do Document Open Action.
1. Salvar o Document atualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
