---
title: Добавить аннотацию линий
type: docs
weight: 30
url: /python-net/add-line-annotation/
description: В этом примере привязывается входной PDF, рисуется красная аннотация с квадратными окончаниями линии и сохраняется изменённый PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию линий в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как добавить аннотацию линий в PDF‑документ с использованием Aspose.PDF for Python через Facades API. Он объясняет, как определить начальную и конечную точки линии, границы прямоугольника, свойства отображения и сохранить обновлённый документ.
---

Аннотации линий полезны для акцентирования текста, выделения взаимосвязей или привлечения внимания к определённым областям в PDF. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно создавать аннотации линий, указывая начальные и конечные точки, ограничивающий прямоугольник, цвет, стиль границы и окончания линий.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Определите свойства аннотации линии.
1. Добавьте аннотацию линии.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
