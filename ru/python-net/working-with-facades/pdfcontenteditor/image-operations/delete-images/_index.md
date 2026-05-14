---
title: Удалить изображения из PDF
linktitle: Удалить изображения из PDF
type: docs
weight: 20
url: /python-net/delete-images/
description:
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить определённые изображения со страницы PDF с помощью PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как удалить конкретные изображения из PDF‑документа с использованием Aspose.PDF for Python через Facades API. Он показывает, как выбрать изображения на определённой странице и сохранить обновлённый документ.
---

Иногда вы можете захотеть удалить только определённые изображения из PDF, а не очищать все визуальные элементы. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете удалить выбранные изображения, указав номер страницы и индекс изображения.

Этот фрагмент кода привязывает входной PDF, удаляет второе изображение на странице 1 и сохраняет изменённый PDF, оставляя остальные изображения нетронутыми.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Удалите определённые изображения с указанной страницы.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
