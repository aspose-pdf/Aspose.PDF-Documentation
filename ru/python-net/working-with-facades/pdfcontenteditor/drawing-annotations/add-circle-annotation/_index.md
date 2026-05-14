---
title: Добавить круговую аннотацию
linktitle: Добавить круговую аннотацию
type: docs
weight: 10
url: /python-net/add-circle-annotation/
description: В этом примере привязывается входной PDF, создаётся круговая аннотация на первой странице и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить круговую аннотацию в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как добавить круговую аннотацию в PDF‑документ с использованием Aspose.PDF for Python через API фасадов. Показано, как определить границы аннотации, задать текст содержимого, настроить цвет и внешний вид, а также сохранить обновлённый документ.
---

Круговые аннотации полезны для выделения областей интереса в PDF‑документе. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете создавать круглые формы, указывая прямоугольник, определяющий границы круга, а также текст аннотации, цвет, параметры заливки, номер страницы и ширину рамки.

1. Создайте объект PdfContentEditor.
1. Привязать входной PDF.
1. Определить границы круга.
1. Добавить аннотацию круга.
1. Сохранить обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
