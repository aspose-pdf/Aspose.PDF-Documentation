---
title: Добавить JavaScript‑ссылку
linktitle: Добавить JavaScript‑ссылку
type: docs
weight: 30
url: /python-net/add-javascript-link/
description: В этом примере привязывается входной PDF, добавляется JavaScript‑ссылка, которая вызывает предупреждение при щелчке, и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить JavaScript‑ссылку в PDF с помощью PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как добавить JavaScript‑ссылку в PDF‑документ с использованием Aspose.PDF for Python через API фасадов. Он показывает, как создать кликабельную область, которая выполняет JavaScript‑код при щелчке, и сохранить обновлённый PDF.
---

JavaScript‑ссылки в PDF позволяют реализовать интерактивный функционал, такой как отображение предупреждений, выполнение вычислений или динамическое изменение содержимого документа. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить кликабельный прямоугольник на странице и связать его с пользовательским JavaScript‑кодом.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для кликабельной JavaScript‑ссылки.
1. Укажите номер страницы и цвет ссылки.
1. Назначьте JavaScript‑код, который будет выполнен при клике.
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
