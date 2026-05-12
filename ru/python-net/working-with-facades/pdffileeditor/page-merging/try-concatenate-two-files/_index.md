---
title: Попробовать объединить два PDF-файла
type: docs
weight: 90
url: /python-net/try-concatenate-two-files/
description: Объедините два PDF-файла с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Безопасно объединять два PDF-файла в Python без исключений
Abstract: Узнайте, как безопасно объединять два PDF-файла с помощью Aspose.PDF for Python. Метод try_concatenate объединяет файлы без выброса исключений, позволяя гибко обрабатывать ошибки в случае сбоя операции.
---

Объединение двух PDF-файлов иногда может завершаться неудачей из‑за повреждения файлов, несовместимых форматов или других проблем. При использовании Aspose.PDF for Python метод try_concatenate класса PdfFileEditor позволяет попытаться безопасно объединить два PDF‑файла. Если операция не удаётся, он возвращает False вместо выброса исключения, предоставляя полный контроль над обработкой ошибок в автоматизированных рабочих процессах или пакетной обработке.

1. Создать объект PdfFileEditor.
1. Попытка объединить два PDF-файла.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
