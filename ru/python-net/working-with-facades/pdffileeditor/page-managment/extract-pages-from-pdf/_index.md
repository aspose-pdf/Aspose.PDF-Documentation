---
title: Извлечение страниц из PDF
linktitle: Извлечение страниц из PDF
type: docs
weight: 30
url: /ru/python-net/extract-pages-from-pdf/
description: Извлечь выбранные страницы из PDF‑документа с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение определённых страниц из PDF‑документа на Python
Abstract: Узнайте, как извлечь выбранные страницы из PDF‑документа с помощью Aspose.PDF for Python. В этом примере показано, как создать новый PDF, содержащий только необходимые вам страницы, позволяя создавать пользовательские документы и выполнять манипуляции на уровне страниц.
---

Извлечение страниц из PDF полезно, когда необходимо создать подмножество документа, поделиться только определённым содержимым или реорганизовать PDF‑файлы для презентаций, отчетов или печати. С помощью Aspose.PDF for Python разработчики могут программно извлекать страницы из PDF‑файла и сохранять их как новый документ.

Узнайте, как использовать метод extract в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе. Указывая список страниц для извлечения, вы можете создать новый PDF, содержащий только выбранные страницы, при этом сохраняется оригинальное содержание и форматирование.

1. Создайте объект PdfFileEditor.
1. Определите страницы для извлечения.
1. Извлеките страницы.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```

