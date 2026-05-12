---
title: Переместить печать по индексу
type: docs
weight: 50
url: /python-net/move-stamp-by-index/
description: В этом примере создаются две резиновые печати на странице 2. После этого печать можно переместить, указав её индекс и новые координаты.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить резиновую печать по индексу в PDF с помощью PdfContentEditor на Python
Abstract: В этом примере демонстрируется, как изменить позицию аннотации резиновой печати в PDF, используя её индекс с помощью Aspose.PDF for Python via the Facades API. Показано, как добавить несколько печатей и затем переместить одну из них, основываясь на её порядке на странице.
---

Когда на странице присутствует несколько резиновых печатей, вы можете переместить конкретную, используя её индекс. Метод move_stamp() позволяет изменить позицию аннотаций согласно их последовательности, что полезно, если вы не отслеживаете идентификаторы печатей, но знаете их порядок.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавьте две аннотации резиновой печати на одну и ту же страницу.
1. Продемонстрируйте, как переместить штамп, используя его индекс.
1. Сохраните обновлённый PDF‑документ.

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
