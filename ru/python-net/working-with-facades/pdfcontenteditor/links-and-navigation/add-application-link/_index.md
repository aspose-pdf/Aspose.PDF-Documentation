---
title: Добавить ссылку на приложение
linktitle: Добавить ссылку на приложение
type: docs
weight: 10
url: /python-net/add-application-link/
description: В этом примере привязывается входной PDF, добавляется ссылка для запуска приложения на первой странице и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте ссылку для запуска приложения в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере показано, как добавить ссылку для запуска приложения в PDF‑документ, используя Aspose.PDF for Python через API Facades. Демонстрируется создание области, по которой можно щёлкнуть, чтобы открыть указанное приложение, и сохранение обновлённого PDF.
---

PDF может включать интерактивные элементы, такие как ссылки, которые запускают внешние приложения. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить прямоугольную область на странице, которая при щелчке открывает конкретный исполняемый файл.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольную область для кликабельной ссылки.
1. Укажите путь к приложению, которое нужно запустить.
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
