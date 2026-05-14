---
title: Изменить размер содержимого страниц PDF
linktitle: Изменить размер содержимого страниц PDF
type: docs
weight: 30
url: /ru/python-net/resize-pdf-page-contents/
description: Измените размер содержимого определённых страниц PDF с помощью Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Программное изменение размера содержимого страниц PDF на Python
Abstract: Узнайте, как изменить размер содержимого определённых страниц PDF с помощью Aspose.PDF for Python. В этом примере демонстрируется, как скорректировать ширину и высоту содержимого страницы, сохраняя структуру документа, что облегчает оптимизацию макетов для печати или просмотра.
---

Регулировка размера содержимого страниц PDF часто необходима при подготовке документов к печати, размещении контента в определённом макете или стандартизации форматов страниц в документе. С помощью Aspose.PDF for Python разработчики могут программно изменять размер содержимого выбранных страниц без ручного редактирования документа.

В этой статье показывается, как использовать метод 'resize_contents' [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) класс для изменения размеров содержимого страницы для конкретных страниц PDF‑файла. Указывая целевую ширину и высоту, содержимое выбранных страниц изменяется соответственно.

1. Создайте объект PdfFileEditor.
1. Измените размер содержимого страниц.

Параметры:

- [1, 3] – список номеров страниц, содержимое которых будет изменено.
- 400 – новая ширина содержимого страницы (в пунктах).
- 750 – новая высота содержимого страницы (в пунктах).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```

