---
title: Добавить действие Document
type: docs
weight: 20
url: /python-net/add-document-action/
description: В этом примере добавляется предупреждающее сообщение JavaScript, которое появляется при открытии PDF. Скрипт привязан к событию открытия документа и автоматически выполняется в поддерживаемых PDF‑просмотрщиках.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить действие Document Open JavaScript к PDF с использованием Python
Abstract: В этом примере демонстрируется, как добавить действие JavaScript уровня Document, которое срабатывает при открытии PDF. С использованием Aspose.PDF for Python via the Facades API пример показывает, как привязать Document, назначить действие события открытия и сохранить обновлённый PDF.
---

Действия уровня Document позволяют определять поведения, которые автоматически выполняются при наступлении определённых событий, например при открытии PDF. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете прикреплять код JavaScript к этим событиям. Это может использоваться для уведомлений, логики валидации или интерактивных рабочих процессов.

1. Создайте объект PdfContentEditor.
1. Привязать входной PDF.
1. Добавить действие уровня документа.
1. Сохранить обновлённый Document.

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
