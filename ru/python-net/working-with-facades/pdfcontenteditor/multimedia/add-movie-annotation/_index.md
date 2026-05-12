---
title: Добавить аннотацию с фильмом
type: docs
weight: 10
url: /python-net/add-movie-annotation/
description: В этом примере привязывается входной PDF, добавляется аннотация с фильмом на странице 1 и сохраняется обновлённый PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить аннотацию с фильмом в PDF с использованием PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как встроить фильм (видео) в документ PDF с использованием Aspose.PDF for Python via the Facades API. Показано, как добавить кликабельную аннотацию, которая воспроизводит видео непосредственно внутри PDF.
---

Аннотации с фильмом в PDF позволяют внедрять мультимедийный контент, такой как видео, в ваши документы. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить прямоугольник на странице, где будет отображаться видео. При клике видео может воспроизводиться непосредственно из PDF, делая ваши документы более интерактивными и привлекательными.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для аннотации фильма.
1. Укажите видеофайл для встраивания.
1. Назначьте номер страницы для аннотации.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
