---
title: Переместить штамп по ID
type: docs
weight: 80
url: /python-net/move-stamp-by-id-example/
description: В этом примере резиновый штамп добавляется на страницу 1, а затем перемещается в новое положение с использованием его ID перед сохранением обновленного документа.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить резиновый штамп по ID в PDF с использованием PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как изменить положение существующей аннотации резинового штампа в PDF, используя Aspose.PDF for Python через Facades API. Показано, как создать штамп и затем программно переместить его, используя его ID.
---

После добавления аннотации резинового штампа в PDF может потребоваться скорректировать её положение. Метод 'move_stamp_by_id()' позволяет переместить штамп по его идентификатору, не создавая его заново. Это полезно в автоматизированных рабочих процессах, где размещение штампа должно динамически корректироваться.

1. Создать [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавить аннотацию резинового штампа.
1. Переместить штамп, используя его идентификатор.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
