---
title: Добавить штамп в PDF
type: docs
weight: 40
url: /python-net/add-stamp/
description: Узнайте, как добавить штамп на страницы PDF, используя PdfFileStamp в Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Добавить текстовые штампы в PDF на Python
Abstract: В этой статье объясняется, как добавить содержимое штампа в PDF‑документы с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileStamp. Показано, как создать штамп, разместить его на странице, управлять вращением и прозрачностью, а также сохранить обновлённый PDF.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) Фасад для добавления повторяющегося контента на страницы PDF. Помимо заголовков, нижних колонтитулов и номеров страниц, его можно использовать для размещения текстовых штампов на каждой странице документа.

## Добавить штамп в PDF

После настройки штампа привяжите входной PDF к `PdfFileStamp`, добавить штамп, и сохранить выходной файл. Это применяет настроенный штамп по всему документу.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
