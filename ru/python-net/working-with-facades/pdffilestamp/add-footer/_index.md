---
title: Добавить нижний колонтитул в PDF
linktitle: Добавить нижний колонтитул в PDF
type: docs
weight: 10
url: /python-net/add-footer/
description: Узнайте, как добавить текстовые и графические нижние колонтитулы на страницы PDF с помощью PdfFileStamp в Python.
lastmod: "2026-04-13"
TechArticle: true
AlternativeHeadline: Добавить текстовые и графические нижние колонтитулы в PDF на Python
Abstract: В этой статье объясняется, как добавить содержимое нижнего колонтитула в документы PDF с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileStamp. Показано, как добавить текстовый нижний колонтитул, разместить графический нижний колонтитул и применить пользовательские отступы нижнего колонтитула перед сохранением обновлённого PDF.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) фасад для добавления повторяющегося контента на страницы PDF. Вы можете использовать его для размещения текста или изображений в нижнем колонтитуле внизу каждой страницы и настроить отступы нижнего колонтитула для управления размещением.

## Добавить текстовый нижний колонтитул

Используйте `add_footer()` с `FormattedText` объект, когда вы хотите разместить одинаковый текстовый нижний колонтитул на каждой странице PDF. Второй аргумент задает отступ снизу, используемый для размещения нижнего колонтитула.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить изображение в нижний колонтитул

Используйте `add_footer()` с потоковым изображением, когда нижний колонтитул должен отображать логотип или другое изображение вместо текста. В примере файл изображения открывается как бинарный поток и размещается внизу каждой страницы.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавьте нижний колонтитул с пользовательскими отступами

Используйте перегрузку с тремя значениями отступов, когда вам нужен больший контроль над размещением нижнего колонтитула. В этом примере нижний колонтитул добавляется с пользовательскими нижними, левыми и правыми отступами.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
