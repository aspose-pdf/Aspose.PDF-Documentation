---
title: Переместить штамп по ID
type: docs
weight: 80
url: /python-net/move-stamp-by-id-example/
description: В этом примере резиновая печать добавляется на страницу 1, а затем перемещается в новое положение с помощью её ID перед сохранением обновленного документа.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить резиновую печать по ID в PDF с использованием PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как изменить позицию существующей аннотации резиновой печати в PDF с помощью Aspose.PDF for Python через Facades API. Показано, как создать печать, а затем переместить её программно, используя её ID.
---

После добавления аннотации резиновой печати в PDF может понадобиться скорректировать её позицию. Метод 'move_stamp_by_id()' позволяет переместить конкретную печать, указав её уникальный идентификатор, что обеспечивает точный контроль над расположением без необходимости отслеживать её индекс или другие атрибуты.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Добавьте аннотацию резиновой печати.
1. Переместите штамп, используя его ID.
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
