---
title: Получить метаданные PDF
linktitle: Получить метаданные PDF
type: docs
weight: 20
url: /python-net/get-pdf-metadata/
description: Извлекать и отображать метаданные из PDF‑документов с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получение метаданных PDF с использованием Aspose.PDF for Python.
Abstract: В этом руководстве демонстрируется, как извлекать и отображать метаданные из PDF‑документов с помощью Aspose.PDF for Python. Вы узнаете, как получать доступ к стандартным свойствам PDF, таким как заголовок, автор, ключевые слова, даты создания/изменения, а также к пользовательским полям метаданных. Кроме того, руководство охватывает проверки действительности PDF, шифрования и статуса портфеля.
---

PDF‑документы часто содержат ценные метаданные, описывающие содержание документа, авторство и права доступа. Aspose.PDF предоставляет удобный API для получения как стандартных, так и пользовательских свойств метаданных. Этот фрагмент кода показывает, как использовать [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) класс для программного анализа PDF‑файлов, включая пошаговые примеры на Python.

1. Загрузите PDF‑файл.
1. Получите стандартные метаданные.
1. Проверьте статус PDF и безопасность.
1. Получите пользовательские метаданные.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
