---
title: Разделить PDF на отдельные страницы
linktitle: Разделить PDF на отдельные страницы
type: docs
weight: 30
url: /ru/python-net/split-pdf-into-single-pages/
description: Разделить документ PDF на отдельные одностраничные PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделить PDF на отдельные страницы в Python
Abstract: Узнайте, как разделить документ PDF на отдельные одностраничные PDF с помощью Aspose.PDF for Python. Этот метод извлекает каждую страницу из оригинального PDF и сохраняет её в отдельный файл для гибкого управления документами и обработки.
---

Разделение PDF на отдельные страницы полезно для обработки на уровне страниц, печати или распределения разделов документа по отдельности. Используя Aspose.PDF for Python, метод 'split_to_pages' класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) создаёт отдельные PDF‑файлы для каждой страницы исходного документа. Такой подход позволяет автоматически извлекать страницы для архивирования, рецензирования или индивидуального распространения, сохраняя оригинальное расположение и содержание.

1. Создайте объект PdfFileEditor.
1. Разделите PDF на отдельные страницы.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```

