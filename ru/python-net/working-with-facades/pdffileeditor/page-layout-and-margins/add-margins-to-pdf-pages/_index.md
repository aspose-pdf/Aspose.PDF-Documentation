---
title: Добавить поля к страницам PDF
type: docs
weight: 10
url: /python-net/add-margins-to-pdf-pages/
description: Добавить пользовательские поля к выбранным страницам PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить пользовательские поля к определённым страницам PDF в Python
Abstract: Узнайте, как добавить пользовательские поля к выбранным страницам PDF, используя Aspose.PDF for Python. Этот пример демонстрирует, как расширить границы страницы, указывая верхние, нижние, левый и правый поля для отдельных страниц, делая PDF более пригодными для печати или визуально согласованными.
---

Добавление полей к страницам PDF может улучшить читаемость, подготовить документы к печати или выделить место для аннотаций. С помощью Aspose.PDF for Python разработчики могут программно добавлять поля к определённым страницам PDF, не изменяя расположение содержимого.

В этом фрагменте кода, the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Класс используется для добавления полдюймовых полей к страницам 1 и 3 входного документа. Поля задаются в пунктах (1 дюйм = 72 пункта) и применяются индивидуально к левому, правому, верхнему и нижнему краю каждой страницы.

1. Откройте исходный PDF-документ.
1. Создайте экземпляр 'PdfFileEditor'.
1. Определите поля и страницы для изменения.
1. Примените поля, используя метод 'add_margins'.
1. Сохраните обновлённый PDF в выходной файл.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
