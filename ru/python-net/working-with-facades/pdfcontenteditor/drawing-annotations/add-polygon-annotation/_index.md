---
title: Добавить аннотацию полигога
linktitle: Добавить аннотацию полигога
type: docs
weight: 40
url: /ru/python-net/add-polygon-annotation/
description: В этом примере привязывается входной PDF, рисуется сплошной полигон на первой странице и сохраняется изменённый документ с аннотацией.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию полигона в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как добавить аннотацию полигона в PDF‑документ с использованием Aspose.PDF for Python через Facades API. Показано, как определить вершины полигона, стиль границы, границы аннотации, описательный текст и сохранить обновлённый документ.
---

Аннотации полигона используются для выделения неправильных областей или форм в PDF, обеспечивая визуальное акцентирование или маркировку конкретных регионов. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете создавать полигоны, указывая координаты вершин, стиль границы, номер страницы и прямоугольник аннотации.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Настройте свойства Polygon.
1. Добавьте аннотацию Polygon.
1. Сохраните обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

