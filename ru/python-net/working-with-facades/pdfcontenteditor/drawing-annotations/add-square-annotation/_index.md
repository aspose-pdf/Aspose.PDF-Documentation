---
title: Добавить аннотацию квадрата
type: docs
weight: 60
url: /python-net/add-square-annotation/
description: В этом примере связывается входной PDF, добавляется заполненная синяя аннотация квадрата на первой странице и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию квадрата в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как добавить аннотацию квадрата в PDF‑документ, используя Aspose.PDF for Python via the Facades API. Показано, как определить прямоугольник аннотации, текстовое содержимое, цвет, параметры заливки и сохранить обновлённый документ.
---

Аннотации квадрата обычно используются для выделения интересующих областей, пометок важных разделов или предоставления визуальных подсказок в PDF‑документе. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете создавать аннотации квадрата, указывая ограничивающий прямоугольник, текст содержимого, цвет границы, параметр заливки, номер страницы и ширину границы.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Определите квадратную аннотацию.
1. Добавьте квадратную аннотацию.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
