---
title: Добавить свободные текстовые аннотации
type: docs
weight: 20
url: /python-net/add-free-text-annotation/
description: В этом примере загружается существующий PDF‑файл, добавляется свободная текстовая аннотация на первую страницу в заданном положении и сохраняется изменённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить свободную текстовую аннотацию в PDF с помощью Python
Abstract: В этом примере демонстрируется, как вставить свободную текстовую аннотацию в PDF‑документ с использованием Aspose.PDF for Python через Facades API. Показывается, как привязать PDF, определить размещение аннотации, добавить пользовательский текст и сохранить обновлённый документ.
---

Свободные текстовые аннотации позволяют размещать видимый текст непосредственно на странице PDF без необходимости всплывающих комментариев. С помощью PdfContentEditor можно указать прямоугольник аннотации, отображаемый текст и целевую страницу.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привязать входной PDF.
1. Определите позицию аннотации.
1. Добавить аннотацию свободного текста.
1. Сохранить обновлённый Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
