---
title: Добавить аннотацию полилиний
linktitle: Добавить аннотацию полилиний
type: docs
weight: 50
url: /ru/python-net/add-polyline-annotation/
description: В примере привязывается входной PDF, создаётся сплошная полилиния на первой странице и сохраняется изменённый документ с аннотацией.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию полилиний в PDF с помощью PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как добавить аннотацию полилиний в документ PDF, используя Aspose.PDF for Python через API Facades. Он показывает, как определить последовательность вершин, стиль границы, прямоугольник аннотации, текст и сохранить обновлённый документ.
---

Аннотации полилиний позволяют выделять серию соединённых отрезков линий в PDF. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)", вы можете нарисовать полилинию, указав координаты вершин, стиль границы, номер страницы и границы аннотации. Это полезно для визуального представления путей, тенденций или соединений в диаграммах и документах.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Настройте свойства Polyline.
1. Добавьте аннотацию Polyline.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

