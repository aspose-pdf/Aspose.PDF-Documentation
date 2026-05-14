---
title: Объединить два PDF-файла
linktitle: Объединить два PDF-файла
type: docs
weight: 60
url: /ru/python-net/concatenate-two-files/
description: Объедините два PDF-файла в один документ с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить два PDF-файла в один PDF на Python
Abstract: Узнайте, как объединить два PDF-файла в один документ с помощью Aspose.PDF for Python. Этот пример демонстрирует, как без проблем объединить два PDF, сохраняя их исходное содержание и форматирование.
---

Объединение двух PDF-файлов — обычная задача при объединении отчётов, контрактов или форм. С помощью Aspose.PDF for Python вы можете программно объединять два PDF в один документ, используя метод concatenate класса [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/). Это гарантирует, что все страницы из обоих файлов будут включены в результирующий PDF, при сохранении исходного макета, содержимого и структуры.

1. Создайте объект PdfFileEditor.
1. Объедините два PDF‑файла.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```

