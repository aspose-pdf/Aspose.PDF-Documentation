---
title: Класс Stamp
linktitle: Класс Stamp
type: docs
weight: 150
url: /python-net/stamp-class/
description: Узнайте, как работать с классом Stamp, чтобы добавлять штампы изображений, PDF и текстовые штампы в PDF‑документы на Python.
lastmod: "2026-04-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET предоставляет [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) класс для размещения переиспользуемого визуального контента на страницах PDF. Штамп может быть основан на тексте, изображении или даже на странице из другого PDF, и его можно позиционировать, вращать, стилизовать и ограничивать конкретными страницами.

В этой статье демонстрируются несколько распространённых рабочих процессов штампов:

1. Создайте переиспользуемые текстовые ресурсы для текстовых штампов.
1. Добавьте штампы изображения и страницы PDF.
1. Добавьте стилизованные текстовые штампы.
1. Ограничьте штамп выбранными страницами.
1. Настройте штамп с фоновым изображением.

В примере используются две вспомогательные функции: одна создает отформатированный текст для текстовых штампов, а другая создает `TextState` объект, используемый для стилизации текстовых штампов.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Добавить штамп изображения

Используйте `bind_image()` когда штамп должен отображать изображение, такое как логотип, значок или иконка. После привязки изображения вы можете установить идентификатор штампа и его исходную точку перед добавлением его в документ.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить страницу PDF в качестве штампа

Используйте `bind_pdf()` когда вы хотите использовать страницу из другого PDF‑файла в качестве содержимого штампа. Это полезно для наложений, таких как утверждения, шаблоны или заранее созданные визуальные элементы, хранящиеся в отдельном документе.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить TextStamp с текстовым состоянием

Используйте `bind_logo()` вместе с `bind_text_state()` когда вы хотите создать текстовую печать с пользовательским оформлением шрифта. Этот подход полезен для отметок одобрения, меток и аннотаций, специфичных для рабочего процесса.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить штамп на определённые страницы

Если штамп не должен отображаться на каждой странице, назначьте целевые номера страниц `pages` свойство. В этом примере добавляется штамп изображения только на первую страницу.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Добавить фоновый ImageStamp

Используйте фоновый штамп, когда изображение должно располагаться позади содержимого страницы. Вы также можете управлять непрозрачностью штампа, его поворотом, качеством, размером и положением, чтобы создать эффекты в стиле водяного знака.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Связанные темы фасадов

- [Работа с фасадами PDF в Python](/pdf/ru/python-net/working-with-facades/)
- [Добавьте заголовки, нижние колонтитулы и штампы с помощью PdfFileStamp](/pdf/ru/python-net/pdffilestamp-class/)
- [Добавьте штамп страницы в PDF‑файлы с помощью Python](/pdf/ru/python-net/add-stamp/)
