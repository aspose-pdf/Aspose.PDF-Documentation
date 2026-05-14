---
title: Удалить штамп по ID
type: docs
weight: 85
url: /python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить резиновые штампы по одному или нескольким ID в PDF с использованием PdfContentEditor
Abstract: Этот пример демонстрирует, как удалить аннотации резиновых штампов из PDF на основе их уникальных ID с использованием Aspose.PDF for Python via the Facades API. Он охватывает как удаление по одному ID, так и удаление по нескольким ID.
---

При работе с PDF, содержащими несколько штампов, часто необходимо удалить конкретные штампы, не затрагивая остальные. С удалением на основе ID вы можете точно контролировать, какие штампы удалить:

- 'delete_stamp_by_id(stamp_id, page_number)' – удаляет один штамп по его ID на определённой странице
- 'delete_stamp_by_ids(page_number, stamp_ids)' – удаляет несколько штампов по их ID на указанной странице

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавьте две резиновые печати с разными идентификаторами.
1. Удаляйте печати, используя как методы удаления по одному идентификатору, так и методы удаления по нескольким идентификаторам.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

