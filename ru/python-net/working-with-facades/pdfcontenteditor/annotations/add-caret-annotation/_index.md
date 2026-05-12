---
title: Добавить аннотацию‑карет
type: docs
weight: 10
url: /python-net/add-caret-annotation/
description: В этом примере загружается существующий PDF, добавляется аннотация‑карет на первую страницу и сохраняется изменённый документ. Аннотация включает красный символ карета и пояснительный текст комментария.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию‑карет в PDF с помощью Python
Abstract: В этом примере демонстрируется, как добавить аннотацию‑карет в документ PDF с использованием Aspose.PDF for Python через Facades API. Пример показывает, как привязать файл PDF, определить расположение аннотации с помощью прямоугольников, настроить свойства карета и сохранить обновлённый документ.
---

Аннотации‑карет обычно используются для указания вставок текста или редакционных комментариев в документе. С помощью PdfContentEditor можно программно добавлять аннотации‑карет, указывая номер страницы, границы аннотации, область выноски, символ, текст заметки и цвет.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привязать входной PDF.
1. Определите параметры аннотации Caret:
  - Номер страницы, где будет добавлена аннотация
  - Прямоугольник Caret (позиция аннотации)
  - Прямоугольник выноски (текстовая область)
  - Символ (например "P")
  - Текст аннотации
  - Цвет аннотации
1. Добавить аннотацию каретки.
1. Сохранить обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
