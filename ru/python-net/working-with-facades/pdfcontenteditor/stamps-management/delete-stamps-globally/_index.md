---
title: Удалить штампы глобально
type: docs
weight: 60
url: /python-net/delete-stamps-globally/
description: В этом примере демонстрируется, как глобально удалить аннотации резиновых штампов на всех страницах PDF с помощью Aspose.PDF for Python via the Facades API. Показано, как удалять штампы по ID без указания отдельных страниц.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить резиновые штампы глобально в PDF с помощью PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как глобально удалить аннотации резиновых штампов на всех страницах PDF с помощью Aspose.PDF for Python via the Facades API. Показано, как удалять штампы по ID без указания отдельных страниц.
---

При работе с несколькими страницами может потребоваться удалить определённые штампы по всему документу. Методы 'delete_stamp_by_id()' и 'delete_stamp_by_ids()' позволяют глобально удалять штампы по их идентификаторам, исключая необходимость проходить каждую страницу вручную.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавьте резиновые штампы на несколько страниц.
1. Удалить штампы глобально, используя их ID.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
