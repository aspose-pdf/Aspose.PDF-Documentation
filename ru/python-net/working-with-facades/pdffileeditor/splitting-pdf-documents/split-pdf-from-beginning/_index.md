---
title: Разделить PDF с начала
type: docs
weight: 10
url: /python-net/split-pdf-from-beginning/
description: Разделите документ PDF с начала, используя Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделить PDF с начала в Python с использованием Aspose.PDF
Abstract: Узнайте, как разделить документ PDF с начала, используя Aspose.PDF for Python. Этот пример демонстрирует извлечение определённого количества страниц, начиная с первой, для создания нового PDF‑документа.
---

Разделение PDF‑файлов с начала полезно, когда вам нужны первые несколько страниц документа как отдельный файл. С использованием Aspose.PDF for Python метод split_from_first в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе позволяет извлекать заданное количество страниц, начиная с первой. Эта функция идеальна для создания отрывков, предварительных просмотров или меньших разделов большого PDF без ручного редактирования исходного файла.

1. Создайте объект PdfFileEditor.
1. Разделите PDF с первой страницы.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
