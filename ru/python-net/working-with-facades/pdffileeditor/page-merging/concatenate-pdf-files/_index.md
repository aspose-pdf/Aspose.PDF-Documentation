---
title: Объединить несколько PDF-файлов
type: docs
weight: 20
url: /python-net/concatenate-pdf-files/
description: Объедините несколько PDF-файлов в один документ с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить несколько PDF-файлов в один PDF на Python
Abstract: Узнайте, как объединить несколько PDF-файлов в один документ с помощью Aspose.PDF for Python. В этом примере демонстрируется, как использовать метод concatenate для бесшовного слияния нескольких PDF-файлов при сохранении их содержимого и форматирования.
---

Объединение PDF-файлов является распространённой задачей в управлении документами, отчётности и автоматизированных рабочих процессах. С помощью Aspose.PDF for Python разработчики могут легко комбинировать несколько PDF-файлов в единый консолидированный документ. Метод concatenate класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класс гарантирует, что все страницы из входных файлов сохраняются в конечном результате, поддерживая их оригинальное расположение и содержание. Этот подход полезен для создания всесторонних отчётов, объединения форм или эффективного архивирования нескольких документов.

1. Создать объект PdfFileEditor.
1. Объединить несколько PDF‑файлов.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
