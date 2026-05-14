---
title: Добавить заголовок в PDF
linktitle: Добавить заголовок в PDF
type: docs
weight: 20
url: /python-net/add-header/
description: Узнайте, как добавить текстовые и графические заголовки на страницы PDF, используя PdfFileStamp в Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Добавить текстовые и графические заголовки в PDF на Python.
Abstract: В этой статье объясняется, как добавить содержимое заголовка в PDF‑документы с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileStamp. Показано, как добавить текстовый заголовок, разместить заголовок‑изображение и применить пользовательские отступы заголовка перед сохранением обновлённого PDF.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) фасад для добавления повторяющегося контента на страницы PDF. Вы можете использовать его для размещения текста заголовка или изображений в верхней части каждой страницы и настройки отступов заголовка для контроля позиционирования.

## Добавить текстовый заголовок

Используйте `add_header()` с `FormattedText` объект, когда вы хотите разместить один и тот же текст заголовка на каждой странице PDF. Второй аргумент определяет верхний отступ для заголовка.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить заголовок с изображением

Используйте `add_header()` с файлом изображения или потоком изображения, когда в заголовке должен отображаться логотип или другая графика. Это полезно для фирменных макетов документов.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавьте заголовок с пользовательскими отступами

Используйте перегрузку с тремя значениями отступов, когда вам требуется больший контроль над размещением заголовка. В этом примере заголовок добавлен с пользовательскими верхним, левым и правым отступами.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
