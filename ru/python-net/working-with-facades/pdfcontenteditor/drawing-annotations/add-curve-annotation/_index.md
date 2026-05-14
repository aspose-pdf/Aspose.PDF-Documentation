---
title: Добавить аннотацию кривой
linktitle: Добавить аннотацию кривой
type: docs
weight: 20
url: /python-net/add-curve-annotation/
description: В этом примере привязывается входной PDF, рисуется пунктирная кривая на первой странице и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию кривой в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как добавить аннотацию кривой в PDF‑документ с использованием Aspose.PDF for Python через Facades API. Показано, как определить вершины кривой, стиль границы, границы аннотации, текстовое содержание и сохранить обновлённый документ.
---

Аннотации кривой используются для выделения нерегулярных путей или форм в PDF, обеспечивая визуальное акцентирование или маркировку важных областей. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете рисовать кривые, задавая последовательность вершин, стиль границы, видимость, прямоугольник аннотации и описательный текст.

1. Создайте объект PdfContentEditor.
1. Привяжите onput PDF.
1. Настройте свойства Curve.
1. Нарисуйте аннотацию Curve.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
