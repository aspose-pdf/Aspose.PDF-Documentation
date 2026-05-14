---
title: Заменить изображения в PDF
type: docs
weight: 30
url: /python-net/replace-image/
description: В этом примере привязывается входной PDF, заменяется первое изображение на странице 1 новым изображением и сохраняется измененный документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заменить изображение в PDF с помощью PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как заменить существующее изображение в PDF‑документе с использованием Aspose.PDF for Python через Facades API. Показано, как выбрать конкретное изображение на странице и заменить его новым изображением, а затем сохранить обновлённый PDF.
---

PDF‑файлы часто содержат изображения, которые могут потребоваться обновить или заменить, такие как логотипы, схемы или фотографии. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете заменить конкретное изображение на заданной странице, указав номер страницы, индекс изображения и путь к файлу нового изображения.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Замените конкретное изображение на указанной странице.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
