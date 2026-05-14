---
title: Добавить аннотации разметки
type: docs
weight: 30
url: /python-net/add-markup-annotation/
description: В этом примере привязывается входной PDF, добавляются четыре разных разметочных аннотации на первую страницу и сохраняется обновлённый документ. Каждая аннотация демонстрирует иной стиль разметки и цвет.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить выделения, подчёркивания, зачеркивания и волнистые аннотации разметки в PDF с помощью Python
Abstract: В этом примере демонстрируется, как добавить несколько разметочных аннотаций — выделение, подчёркивание, зачеркивание и волнистую — в документ PDF с использованием Aspose.PDF for Python via the Facades API. Пример показывает, как определить области аннотаций, указать типы разметки, применить цвета и сохранить изменённый документ.
---

Аннотации разметки используются для выделения или рецензирования текста в PDF. С помощью PdfContentEditor можно программно применять различные стили разметки, указывая область прямоугольника, текст комментария, тип разметки, номер страницы и цвет.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привяжите входной PDF.
1. Определите прямоугольники аннотаций.
1. Добавьте разметку аннотаций.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
