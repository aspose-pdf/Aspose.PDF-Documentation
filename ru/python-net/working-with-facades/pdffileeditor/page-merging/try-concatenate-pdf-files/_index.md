---
title: Объединить PDF-файлы
linktitle: Объединить PDF-файлы
type: docs
weight: 70
url: /python-net/try-concatenate-pdf-files/
description: Объедините несколько PDF-файлов с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Безопасное объединение PDF-файлов в Python с обработкой ошибок
Abstract: Узнайте, как безопасно конкатенировать несколько PDF-файлов с помощью Aspose.PDF for Python. Метод try_concatenate пытается объединить PDF без выбрасывания исключений, позволяя разработчикам аккуратно обрабатывать ошибки.
---

Объединение PDF-файлов иногда может завершаться неудачей из‑за повреждённых файлов, несовместимых форматов или других проблем. С помощью Aspose.PDF for Python вы можете использовать метод try_concatenate класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класса для безопасного выполнения конкатенации. Вместо выбрасывания исключения метод возвращает False, если операция не удалась, обеспечивая контролируемую обработку ошибок в автоматизированных рабочих процессах. 

1. Создайте объект PdfFileEditor.
1. Обьедините PDF-файлы.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(files_to_merge, output_file):
        print("Concatenation failed for the provided files.")
```
