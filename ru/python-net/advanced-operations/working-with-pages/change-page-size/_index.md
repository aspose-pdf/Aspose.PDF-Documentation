---
title: Изменение размера страницы с помощью Python
linktitle: Изменение размера страницы
type: docs
weight: 40
url: /ru/python-net/change-page-size/
description: Измените размер страницы вашего PDF-документа с помощью библиотеки Aspose.PDF для Python через .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменение размера страницы с использованием Python
Abstract: В этой статье демонстрируется, как читать и изменять размеры страниц PDF с помощью Aspose.PDF. Пример «Get Page Size» извлекает ширину и высоту конкретной страницы PDF, позволяя пользователям просматривать раскладку страницы, проверять форматирование или анализировать структуру документа. Пример «Set Page Size» показывает, как изменить размеры страницы — например, преобразовать первую страницу к формату A4 — одновременно отображая свойства полей (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) до и после изменения.
---

Aspose.PDF для Python через .NET позволяет изменять размер страницы PDF простыми строками кода. Эта тема показывает, как обновить размеры страницы с помощью API [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

Обратите внимание, что свойства высоты и ширины используют пункты как базовую единицу измерения, где 1 дюйм = 72 пункта и 1 см = 1/2.54 дюйма = 0,3937 дюйма = 28,3 пункта.

{{% /alert %}}

### Установить размер страницы PDF в A4

Пример обновляет размер первой страницы PDF‑документа до стандартных размеров A4. Он также выводит размеры полей страницы (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) до и после изменения размера, чтобы вы могли проверить изменения.

Следующий фрагмент кода показывает, как изменить размеры страницы PDF до формата A4:

1. Доступ к первой [`Странице`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из [`Документа`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Показать размеры полей страницы до изменения (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Применить размеры A4 (597,6 × 842,4 пункта) с помощью API страницы.
1. Показать обновлённые размеры полей страницы.
1. Сохранить изменённый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) по указанному пути вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Получить размер страницы PDF

Этот фрагмент читает PDF и получает размеры (ширину и высоту) первой страницы. Он использует API [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) для извлечения ограничивающего [`Прямоугольник`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) страницы и выводит его размер в консоль. Это полезно для проверки раскладки страницы, верификации форматов или подготовки документов к дальнейшей обработке.

1. Загрузить PDF как [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Доступ к первой [`Странице`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Получить ограничивающий прямоугольник страницы с помощью `get_page_rect()`.
1. Извлечь значения ширины и высоты.
1. Вывести размеры страницы.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Получить размер страницы PDF до и после поворота

Получить размеры страницы PDF до и после применения вращения на 90°. Это демонстрирует, как вращение влияет на ширину и высоту и как использовать `get_page_rect()` с учётом вращения или без него.

1. Открыть PDF как [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Доступ к первой [`Странице`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Применить вращение на 90° с помощью `page.rotate = ap.Rotation.ON90` (см. перечисление [`Вращение`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. Получить прямоугольник страницы без учёта вращения, используя `get_page_rect(False)`, и вывести его ширину и высоту.
1. Получить прямоугольник страницы с учётом вращения, используя `get_page_rect(True)`, и вывести его ширину и высоту.
1. Сравнить, как меняются размеры из‑за вращения.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
