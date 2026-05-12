---
title: Добавить резиновую печать
type: docs
weight: 10
url: /python-net/add-rubber-stamp/
description: В этом примере связывается входной PDF, добавляется зеленая резиновая печать “Approved” на первые четыре страницы и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию резиновой печати в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как добавить аннотацию резиновой печати в документ PDF, используя Aspose.PDF for Python через Facades API. Резиновые печати позволяют визуально помечать страницы одобрениями, рецензиями или пользовательскими метками.
---

Аннотации резиновой печати обычно используются в PDF для указания одобрения, статуса рецензии или других заметок. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить прямоугольник для печати, установить её текст и комментарии, выбрать цвет и применить её к нескольким страницам документа.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Перебрать страницы 1–4.
1. Добавить аннотацию резиновой печати с пользовательским текстом, комментариями и цветом.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
