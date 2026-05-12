---
title: Добавить вложение
type: docs
weight: 10
url: /python-net/add-attachment/
description: В этом примере происходит привязка входного PDF, прикрепление внешнего файла к первой странице и сохранение изменённого PDF с встроенным вложением.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление файловых вложений в PDF с использованием Python
Abstract: В этом примере показано, как прикреплять внешние файлы к документу PDF с помощью Aspose.PDF for Python via the Facades API. Он демонстрирует, как привязать PDF, добавить вложения с описаниями и сохранить обновлённый документ.
---

Файловые вложения в PDF позволяют включать дополнительные документы, изображения или другие ресурсы непосредственно в PDF. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно прикреплять файлы к конкретным страницам, задавать имя вложения и предоставлять описание.

1. Создайте объект PdfContentEditor.
1. Привязать входной PDF.
1. Откройте файл вложения.
1. Добавьте вложение в PDF.
1. Сохранить обновлённый Document.

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
