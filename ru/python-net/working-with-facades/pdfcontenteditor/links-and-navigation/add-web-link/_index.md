---
title: Добавить веб‑ссылку
linktitle: Добавить веб‑ссылку
type: docs
weight: 60
url: /python-net/add-web-link/
description: В этом примере привязывается входной PDF, добавляется синяя аннотация веб‑ссылки на странице 1, указывающая на страницу продукта Aspose Python PDF, и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить веб‑ссылку в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как добавить веб‑ссылку в PDF‑документ с использованием Aspose.PDF for Python через API Facades. Показано, как создать кликабельную область на странице, которая открывает указанный URL в веб‑браузере, и сохранить обновлённый документ.
---

Веб‑ссылки в PDF позволяют пользователям переходить напрямую к онлайн‑ресурсам, веб‑сайтам или документации. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить прямоугольную область на странице PDF, которая при щелчке открывает URL в браузере по умолчанию.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для кликабельной веб‑ссылки.
1. Укажите URL, номер страницы и цвет ссылки.
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
