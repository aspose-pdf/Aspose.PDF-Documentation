---
title: Добавить разрывы страниц в PDF
type: docs
weight: 20
url: /python-net/add-page-breaks-in-pdf/
description: Вставьте разрывы страниц в документ PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Программно добавить разрывы страниц в PDF-страницы на Python
Abstract: Узнайте, как вставить разрывы страниц в документ PDF с помощью Aspose.PDF for Python. Этот пример демонстрирует, как разделить страницу в указанной вертикальной позиции, позволяя разработчикам реорганизовать содержимое и динамически создавать дополнительные страницы.
---

Разрывы страниц полезны, когда необходимо разделить длинные страницы PDF на несколько страниц или контролировать распределение содержимого по документу. С помощью Aspose.PDF for Python разработчики могут вставлять разрывы страниц в конкретных позициях без ручного редактирования PDF.

Эта статья показывает, как использовать метод 'add_page_break' [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класс для вставки разрыва страницы на заданной вертикальной координате выбранной страницы. Метод создает новую страницу и перемещает содержимое ниже точки разрыва на эту страницу.

1. Создать объект PdfFileEditor.
1. Определить позицию разрыва страницы.
1. Вставить разрыв страницы.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
