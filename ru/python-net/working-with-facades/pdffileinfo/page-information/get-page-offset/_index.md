---
title: Получить смещение страницы
linktitle: Получить смещение страницы
type: docs
weight: 20
url: /python-net/get-page-offset/
description: Этот пример демонстрирует, как использовать PdfFileInfo для получения смещений по осям X и Y конкретной страницы и преобразования их в дюймы для точного анализа макета и позиционирования.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить смещения страниц PDF с помощью Python
Abstract: Функция 'get_page_offsets' извлекает горизонтальные (X) и вертикальные (Y) смещения каждой страницы в PDF‑файле. Эти смещения представляют позицию содержимого страницы относительно начала PDF. Преобразуя пункты в дюймы, функция предоставляет точные, легко читаемые измерения, которые могут быть использованы для точного размещения аннотаций, изображений или текста. Она поддерживает многостраничные PDF и предназначена для разработчиков, работающих над макетом PDF, автоматизацией или выравниванием контента.
---

Функция 'get_page_offsets' предоставляет разработчикам точные горизонтальные (X) и вертикальные (Y) смещения страниц в PDF‑файле. В PDF‑документах каждая страница может иметь внутреннюю точку начала, отличающуюся от верхнего левого угла страницы, что может влиять на позиционирование текста, изображений, аннотаций или другого содержимого.

Используя Aspose.PDF Facades, эта функция извлекает эти смещения в пунктах и преобразует их в дюймы для удобного восприятия. Она поддерживает многостраничные PDF, что делает её подходящей для автоматизированных рабочих процессов, требующих точного размещения контента.

1. Создайте объект фасада PDF.
1. Получите количество страниц в PDF.
1. Пройдите по каждой странице, чтобы получить смещения.
1. Выведите или сохраните смещения.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
