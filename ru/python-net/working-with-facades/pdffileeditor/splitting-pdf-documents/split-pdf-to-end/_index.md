---
title: Разделить PDF до конца
linktitle: Разделить PDF до конца
type: docs
weight: 40
url: /python-net/split-pdf-to-end/
description: Разделить документ PDF, начиная с указанной страницы и до последней страницы, используя Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделить PDF с определённой страницы до конца на Python
Abstract: Узнайте, как разделить документ PDF, начиная с указанной страницы и до последней, используя Aspose.PDF for Python. Этот пример демонстрирует извлечение всех страниц, начиная с заданной, для создания нового файла PDF.
---

Разделение PDF с определённой страницы до конца полезно, когда вам нужна последняя часть документа как отдельный файл. Используя Aspose.PDF for Python, метод split_to_end класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) позволяет извлекать страницы, начиная с любого номера страницы, до последней страницы документа. Это идеально подходит для создания отрывков, извлечения глав или обработки частей большого PDF без ручного редактирования.

1. Создайте объект PdfFileEditor.
1. Разделите PDF с определённой страницы до конца.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
