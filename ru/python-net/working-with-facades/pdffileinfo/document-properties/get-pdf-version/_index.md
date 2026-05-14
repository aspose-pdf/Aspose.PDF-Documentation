---
title: Получить версию PDF
linktitle: Получить версию PDF
type: docs
weight: 20
url: /ru/python-net/get-pdf-version/
description: Узнайте, как программно определить версию PDF‑документа с помощью Aspose.PDF for Python. Этот учебник демонстрирует, как использовать класс PdfFileInfo для проверки версии PDF файла.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить версию PDF с помощью Aspose.PDF for Python
Abstract: PDF‑документы имеют номера версий, которые указывают на поддерживаемые функции и спецификации (например, 1.4, 1.7, 2.0). Знание версии PDF важно для совместимости, поддержки функций и процессов обработки документов. В этом руководстве вы узнаете, как программно получить версию PDF с помощью класса PdfFileInfo в Aspose.PDF for Python.
---

Версии PDF определяют функции и возможности, поддерживаемые в документе, включая поля формы, шифрование, аннотации и сжатие. Для разработчиков, работающих с несколькими PDF‑файлами, проверка версии обеспечивает совместимость с инструментами, библиотеками или процессами, которые обрабатывают эти файлы.

С помощью Aspose.PDF for Python вы можете легко проверить версию PDF с помощью [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) класса.

1. Загрузите PDF-документ.
1. Получите версию PDF.
1. Отобразите версию в консоли.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```

