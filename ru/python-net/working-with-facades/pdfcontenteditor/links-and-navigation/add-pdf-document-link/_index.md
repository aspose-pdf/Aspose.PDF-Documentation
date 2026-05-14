---
title: Добавить ссылку на PDF‑документ
linktitle: Добавить ссылку на PDF‑документ
type: docs
weight: 50
url: /python-net/add-pdf-document-link/
description: В этом примере привязывается входной PDF, добавляется ссылка зелёного цвета на страницу в другом PDF и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить ссылку на PDF‑документ с помощью PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как добавить ссылку на другой PDF‑документ с использованием Aspose.PDF for Python через API Facades. Показано, как создать кликабельную область, открывающую другой PDF, и сохранить обновлённый документ.
---

Ссылки в PDF‑документах позволяют пользователям беспрепятственно перемещаться от одного PDF к другому. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить кликабельный прямоугольник, который ссылается на страницу в другом PDF‑файле, делая ваши документы интерактивными и связанными.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для кликабельной ссылки.
1. Укажите связанный PDF‑файл, исходную страницу и страницу назначения.
1. Установите цвет ссылки.
1. Сохраните обновлённый PDF‑документ.

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
