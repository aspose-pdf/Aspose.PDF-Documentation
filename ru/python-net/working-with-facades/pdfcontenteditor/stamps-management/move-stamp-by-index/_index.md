---
title: Переместить печать по индексу
type: docs
weight: 90
url: /python-net/move-stamp-by-index/
description: Как переместить аннотации в виде резиновой печати в PDF, используя их индекс на странице, с помощью Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Перемещение резиновых печатей в PDF с помощью позиционирования по индексу
Abstract: Этот пример демонстрирует, как переместить аннотации резиновой печати в PDF, используя их индекс на странице, с помощью Aspose.PDF for Python через Facades API. Он подчёркивает создание нескольких печатей и подготовку их к операциям перемещения.
---

При редактировании PDF может потребоваться корректировать положение существующих резиновых печатей. Этот фрагмент кода показывает, как:

- Добавить несколько печатей на одной странице
- Подготовить их к перемещению, используя их индекс
- Опционально переместить штамп, указав его страницу, индекс и новые координаты

Метод 'move_stamp(page_number, stamp_index, new_x, new_y)' может точно перемещать штампы.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) объект.
1. Привязать PDF к редактору.
1. Добавить несколько резиновых штампов на страницу.
1. Сохраните документ перед выполнением операций перемещения.
1. Переместить конкретный штамп по его индексу.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
