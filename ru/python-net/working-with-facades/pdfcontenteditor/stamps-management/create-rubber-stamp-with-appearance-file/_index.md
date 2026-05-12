---
title: Создать резиновый штамп с файлом внешнего вида
type: docs
weight: 20
url: /python-net/create-rubber-stamp-with-appearance-file/
description: В примере привязывается входной PDF, создаётся резиновый штамп на странице 1 с использованием изображения в качестве внешнего вида штампа, и сохраняется обновлённый PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать резиновый штамп с пользовательским внешним видом в PDF с помощью PdfContentEditor
Abstract: Этот пример демонстрирует, как добавить аннотацию резинового штампа с пользовательским внешним видом (изображение) в документ PDF, используя Aspose.PDF for Python via the Facades API. Пользовательские штампы позволяют включать логотипы, подписи или фирменные визуальные элементы в качестве части штампа.
---

Аннотации резиновых штампов можно настраивать не только с помощью текста, но и используя файл изображения в качестве их внешнего вида. Такой подход полезен для добавления логотипов компании, подписных штампов или любых визуальных индикаторов на страницы вашего PDF.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для печати.
1. Используйте пользовательский файл изображения, чтобы определить внешний вид резинового штампа.
1. Установите текст и цвет штампа.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```
