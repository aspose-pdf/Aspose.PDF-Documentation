---
title: Объединить большое количество PDF‑файлов
type: docs
weight: 10
url: /python-net/concatenate-large-number-files/
description: Эффективно объединять большое количество PDF‑файлов с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединение больших PDF‑файлов в Python с использованием буферизации на диск
Abstract: Узнайте, как эффективно объединять большое количество PDF‑файлов с помощью Aspose.PDF for Python. Этот пример демонстрирует, как включить буферизацию на диск для обработки больших PDF‑файлов без исчерпания памяти системы, обеспечивая плавное объединение множества файлов.
---

С помощью Aspose.PDF for Python вы можете включить буферизацию на диск в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе для эффективного объединения множества PDF‑файлов. Метод concatenate объединяет входные файлы в один PDF, при этом буфер на диске предотвращает большое потребление памяти. Такой подход идеален для обработки массовых документов, автоматической генерации отчетов или консолидирования больших архивов PDF.

1. Создайте объект PdfFileEditor.
1. Объедините несколько PDF файлов.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
