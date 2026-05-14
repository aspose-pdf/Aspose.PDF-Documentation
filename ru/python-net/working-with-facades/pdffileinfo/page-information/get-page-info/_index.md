---
title: Получить информацию о странице
linktitle: Получить информацию о странице
type: docs
weight: 10
url: /ru/python-net/get-page-info/
description: Узнайте, как программно получать информацию о странице в PDF с помощью Aspose.PDF for Python. В этом руководстве показывается, как получить ширину, высоту, поворот и смещения конкретной страницы в PDF‑документе.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получение информации о странице PDF с помощью Aspose.PDF for Python
Abstract: Функция извлекает ширину, высоту, угол поворота и горизонтальные (X) и вертикальные (Y) смещения страницы PDF. Эти свойства возвращаются в пунктах и отражают физический размер страницы и позиционирование содержимого внутри PDF. Функция выводит полученные значения, позволяя разработчикам понять раскладку и ориентацию страницы для дальнейшей обработки PDF.
---

Утилитная функция ‘get_page_information’ помогает разработчикам понять структуру и раскладку страниц PDF. Каждая страница PDF может иметь разные размеры, поворот и внутренние смещения, которые могут влиять на размещение содержимого или задачи автоматизации.

Она позволяет извлекать ключевые метаданные и информацию о раскладке конкретной страницы в PDF‑файле. API Aspose.PDF Facades предоставляет детали, такие как ширина, высота, поворот страницы и смещения X/Y. Эта информация важна для задач, таких как анализ раскладки страниц, размещение аннотаций или автоматизированная обработка PDF.

1. Создайте объект фасада PDF.
1. Получите размеры страницы и её разметку.
1. Выведите или сохраните полученные значения.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```

