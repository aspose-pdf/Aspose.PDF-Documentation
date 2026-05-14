---
title: Добавить страницы в PDF
type: docs
weight: 10
url: /python-net/append-pages-to-pdf/
description: Добавьте страницы из одного PDF‑документа в другой с использованием Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление страниц из одного PDF в другой на Python
Abstract: Узнайте, как добавить страницы из одного PDF‑документа в другой с помощью Aspose.PDF for Python. В этом примере демонстрируется, как использовать класс PdfFileEditor для объединения страниц из нескольких PDF и создания единого выходного документа.
---

Объединение страниц из разных PDF‑документов является распространенной задачей в рабочих процессах обработки документов. С помощью Aspose.PDF for Python разработчики могут легко добавлять страницы из одного или нескольких PDF‑файлов в существующий документ.

Этот фрагмент кода показывает, как использовать метод append в [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) классе для добавления выбранных страниц из другого PDF‑файла в конец исходного PDF. Указывая диапазон страниц, разработчики могут точно контролировать, какие страницы включаются в окончательный документ.

1. Создайте объект PdfFileEditor.
1. Добавьте страницы из другого PDF.

Указанные страницы из вторичного PDF‑документа добавляются в конец оригинального PDF, создавая объединённый выходной файл.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
