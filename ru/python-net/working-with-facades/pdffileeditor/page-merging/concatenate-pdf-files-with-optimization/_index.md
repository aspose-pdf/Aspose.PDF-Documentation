---
title: Объединение PDF-файлов с оптимизацией
linktitle: Объединение PDF-файлов с оптимизацией
type: docs
weight: 30
url: /ru/python-net/concatenate-pdf-files-with-optimization/
description: Объедините несколько PDF-файлов в один оптимизированный PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединение PDF-файлов с оптимизированным выводом в Python
Abstract: Узнайте, как объединять несколько PDF-файлов в один оптимизированный PDF с помощью Aspose.PDF for Python. Этот пример демонстрирует, как включить оптимизацию размера, чтобы уменьшить размер выходного файла, сохраняя при этом содержимое и форматирование.
---

При объединении нескольких PDF-файлов получающийся файл может стать крупным, особенно если он содержит изображения или сложный контент. С помощью Aspose.PDF for Python разработчики могут включить оптимизацию во время объединения, чтобы уменьшить размер файла без потери качества. Свойство optimize_size в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе гарантирует, что объединённый PDF является компактным и эффективным, что делает его подходящим для обмена, хранения или архивирования.

1. Создайте объект PdfFileEditor и включите оптимизацию.
1. Объедините PDF-файлы.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```

