---
title: Добавить штамп
linktitle: Добавить штамп
type: docs
weight: 10
url: /python-net/add-rubber-stamp/
description: В этом примере привязывает входной PDF, добавляет зелёный “Approved” штамп на первые четыре страницы и сохраняет изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию штампа к PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как добавить аннотацию штампа к PDF‑документу с использованием Aspose.PDF for Python via the Facades API. Штампы позволяют визуально помечать страницы одобрениями, отзывами или пользовательскими метками.
---

Аннотации штампов часто используются в PDF для указания одобрения, статуса обзора или других заметок. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить прямоугольник для штампа, установить его текст и комментарии, выбрать цвет и применить его к нескольким страницам документа.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Пройдите по страницам 1–4.
1. Добавьте аннотацию штампа с пользовательским текстом, комментариями и цветом.
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
