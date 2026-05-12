---
title: Удалить все изображения из PDF
type: docs
weight: 10
url: /python-net/delete-all-images/
description: Удалить все изображения из PDF‑документа с помощью Aspose.PDF for Python через Facades API.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить все изображения из PDF с использованием PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как удалить все изображения из PDF‑документа с помощью Aspose.PDF for Python через Facades API. Он показывает, как привязать PDF, удалить все встроенные изображения и сохранить обновлённый документ.
---

PDF‑документы часто содержат изображения для иллюстраций, брендинга или декора. Может возникнуть необходимость удалить все изображения из PDF, например, чтобы уменьшить размер файла, защитить конфиденциальные визуальные материалы или подготовить версию только с текстом.

Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно удалить все изображения из PDF, обеспечивая, что документ содержит только текстовое содержимое. В этом примере привязывается входной PDF, удаляются все изображения и сохраняется изменённый файл.

1. Создайте объект PdfContentEditor.
1. Привязать входной PDF.
1. Удалить все изображения.
1. Сохранить обновлённый Document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
