---
title: Создать резиновый штамп с потоком внешнего вида
type: docs
weight: 30
url: /python-net/create-rubber-stamp-with-appearance-stream/
description: В этом примере загружается PDF, создаётся резиновый штамп на странице 1 с использованием файла изображения для его внешнего вида, и сохраняется изменённый документ. ✨
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать резиновый штамп с пользовательским изображением внешнего вида с использованием PdfContentEditor в Python
Abstract: В этом примере показано, как создать аннотацию резинового штампа с пользовательским изображением внешнего вида в PDF с использованием Aspose.PDF for Python via the Facades API. Этот подход позволяет применять фирменные или визуально богатые штампы, такие как логотипы, печати или подписи.
---

Аннотации резиновых штампов можно настраивать с помощью внешнего файла изображения. Вместо того чтобы полагаться только на штампы, основанные на тексте, вы можете задать визуальное отображение (например, логотип компании или знак одобрения) и разместить его на странице.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для размещения штампа.
1. Используйте файл изображения в качестве внешнего вида штампа.
1. Примените настройки текста и цвета.
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
