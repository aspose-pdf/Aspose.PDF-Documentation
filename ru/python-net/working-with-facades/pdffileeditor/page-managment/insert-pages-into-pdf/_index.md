---
title: Вставить страницы в PDF
linktitle: Вставить страницы в PDF
type: docs
weight: 40
url: /ru/python-net/insert-pages-into-pdf/
description: Вставьте страницы из одного PDF в другой с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Вставить страницы из другого PDF в существующий PDF на Python
Abstract: Узнайте, как вставлять страницы из одного PDF в другой с использованием Aspose.PDF for Python. В этом примере демонстрируется, как добавить выбранные страницы из вторичного PDF в определённое место оригинального документа, создавая объединённый PDF с точным размещением страниц.
---

Вставка страниц в существующий PDF является распространённой задачей при объединении документов, добавлении содержимого или реорганизации отчётов. С помощью Aspose.PDF for Python разработчики могут программно вставлять страницы из одного PDF в другой в указанном месте.

Эта статья показывает, как использовать метод insert в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе. Указывая номера страниц для вставки и целевое местоположение, вы можете объединять содержимое разных PDF, сохраняя оригинальное форматирование и структуру.

1. Создайте объект PdfFileEditor.
1. Определите позицию вставки и страницы.
1. Вставьте страницы.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```

