---
title: Установить метаданные PDF
linktitle: Установить метаданные PDF
type: docs
weight: 50
url: /python-net/set-pdf-metadata/
description: Изменять и сохранять метаданные в PDF‑документах с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновление метаданных PDF с использованием Aspose.PDF for Python
Abstract: Это руководство объясняет, как изменять и сохранять метаданные в PDF‑документах с помощью Aspose.PDF for Python via .NET. В нём демонстрируется, как обновлять стандартные свойства PDF, такие как название, тема, ключевые слова и создатель, а также пользовательские поля метаданных. По завершении вы сможете программно обновлять метаданные PDF и сохранять внесённые изменения.
---

PDF‑документы могут содержать как стандартные метаданные (Title, Subject, Keywords, Creator, Author), так и пользовательские метаданные, сохранённые как свойства XMP. Aspose.PDF предоставляет простой API для изменения этих свойств в Python. Это руководство охватывает обновление этих полей и сохранение изменённого PDF‑файла с использованием [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) класса.

1. Загрузите PDF‑файл.
1. Обновите стандартные метаданные.
1. Добавьте или обновите пользовательские метаданные.
1. Сохраните обновленные метаданные.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
