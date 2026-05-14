---
title: Добавить вложение из пути
type: docs
weight: 20
url: /python-net/add-attachment-from-path/
description: В этом примере связывается входной PDF, прикрепляется внешний файл с использованием его пути к файлу и сохраняется измененный PDF с встроенным вложением.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Прикрепление файлов к PDF с использованием перегрузки пути к файлу в Python
Abstract: В этом примере показано, как прикреплять внешние файлы к документу PDF с использованием перегрузки пути к файлу функции 'add_document_attachment()' в Aspose.PDF for Python via the Facades API. Это упрощает добавление вложений без ручного открытия файлового потока.
---

PDF может включать встроенные файлы, такие как документы, электронные таблицы или изображения, для справки или распространения. Перегрузка пути к файлу функции 'add_document_attachment()' позволяет добавлять вложения напрямую из пути к файлу, исключая необходимость открывать файл вручную.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привяжите входной PDF.
1. Добавьте вложение, используя путь к файлу.
1. Сохраните обновлённый Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
