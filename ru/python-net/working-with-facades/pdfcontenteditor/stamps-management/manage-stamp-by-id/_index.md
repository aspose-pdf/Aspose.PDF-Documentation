---
title: Управление штампом по ID
type: docs
weight: 95
url: /python-net/manage-stamp-by-id/
description: Как управлять аннотациями резиновых штампов в PDF по их уникальным ID с использованием Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление резиновыми штампами по ID в PDF с использованием PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как управлять аннотациями резиновых штампов в PDF по их уникальным ID, используя Aspose.PDF for Python через Facades API. Вы можете скрыть или отобразить определённые штампы на некоторых страницах, не затрагивая другие штампы.
---

В PDF‑файлах с несколькими резиновыми штампами может быть полезно управлять отдельными штампами на основе их ID. Методы 'hide_stamp_by_id()' и 'show_stamp_by_id()' позволяют избирательно контролировать видимость. Этот пример показывает, как:

- Добавить несколько штампов с уникальными ID
- Скрыть штамп на конкретной странице
- Показать штамп на другой странице

Используя операции, основанные на ID, вы избегаете отслеживания штампoв по позиции страницы или другим атрибутам.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавьте резиновые штампы с конкретными ID.
1. Скрывайте и показывайте штампы в зависимости от их ID и номеров страниц.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
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

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
