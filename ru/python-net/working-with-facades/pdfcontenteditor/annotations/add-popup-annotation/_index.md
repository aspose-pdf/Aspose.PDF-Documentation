---
title: Добавить всплывающие аннотации
type: docs
weight: 40
url: /python-net/add-popup-annotation/
description: В этом примере загружается PDF, добавляется всплывающая аннотация на первую страницу и сохраняется изменённый документ. Всплывающая аннотация установлена видимой по умолчанию и отображает указанный текст комментария.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить всплывающие аннотации в PDF с использованием Python
Abstract: В этом примере показано, как вставить всплывающую аннотацию в PDF‑документ, используя Aspose.PDF for Python via the Facades API. Объясняется, как определить область всплывающей аннотации, установить текст аннотации, управлять видимостью и сохранить обновлённый документ.
---

Всплывающие аннотации полезны для добавления комментариев, пояснений или интерактивных заметок в PDF‑файлах. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете создавать всплывающие аннотации программно, указывая местоположение, содержание, видимость и номер страницы.

1. Создайте объект PdfContentEditor.
1. Привязать входной PDF.
1. Определите прямоугольник всплывающей аннотации.
1. Добавьте всплывающую аннотацию.
1. Сохранить обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
