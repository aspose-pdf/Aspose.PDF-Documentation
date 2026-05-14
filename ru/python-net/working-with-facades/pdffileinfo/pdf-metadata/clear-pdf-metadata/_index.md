---
title: Очистить метаданные PDF
type: docs
weight: 10
url: /python-net/clear-pdf-metadata/
description: Удалите все метаданные из PDF‑документа с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Очистка метаданных PDF с использованием Aspose.PDF for Python
Abstract: В этом руководстве объясняется, как удалить все метаданные из PDF‑документа с помощью Aspose.PDF for Python via .NET. Вы научитесь очищать как стандартные, так и пользовательские поля метаданных и сохранять очищенный PDF. Это полезно для обеспечения конфиденциальности, безопасности или подготовки PDF‑файлов к публичному выпуску.
---

PDF часто содержат метаданные, такие как заголовок, автор, ключевые слова, даты создания и пользовательские поля. В некоторых сценариях вы можете захотеть удалить все метаданные из PDF, например перед распространением или архивированием. Aspose.PDF предоставляет метод clear_info() для простого удаления всех метаданных. После очистки вы можете сохранить PDF, используя метод save().

1. Загрузите PDF‑файл.
1. Очистите все метаданные.
1. Сохраните чистый PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
