---
title: Изменить размер страницы PDF в Python
linktitle: Изменение размера страницы
type: docs
weight: 40
url: /python-net/change-page-size/
description: Узнайте, как читать и изменять размеры страниц PDF в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменение размера страницы с помощью Python
Abstract: Эта статья демонстрирует, как читать и изменять размеры страниц PDF с помощью Aspose.PDF. Пример «Get Page Size» извлекает ширину и высоту конкретной страницы PDF, позволяя пользователям проверять макет страницы, валидировать форматирование или анализировать структуру документа. Пример «Set Page Size» показывает, как изменить размеры страницы — например, преобразовать первую страницу к формату A4 — одновременно отображая свойства коробки (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) до и после изменения.
---

Aspose.PDF for Python via .NET позволяет менять размер страниц PDF простыми строками кода. Эта тема показывает, как обновлять размеры страниц с помощью [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API.

Используйте это руководство, когда вам необходимо изменить размер существующих страниц PDF, нормализовать размеры документа или проверить настройки коробок страниц в Python.

{{% alert color="primary" %}}

Обратите внимание, что свойства высоты и ширины используют точки в качестве базовой единицы, где 1 дюйм = 72 точки, а 1 см = 1/2,54 дюйма = 0,3937 дюйма = 28,3 точки.

{{% /alert %}}

## Установите размер страницы PDF на A4

В примере размер первой страницы PDF‑документа обновляется до стандартных размеров A4. Он также выводит размеры коробки страницы (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) до и после изменения размера, чтобы вы могли проверить изменения.

Следующий фрагмент кода показывает, как изменить размеры страницы PDF до формата A4:

1. Получите доступ к первой [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Отобразить размеры коробок страницы до изменения (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Применить размеры A4 (597.6 × 842.4 points) с помощью API страницы.
1. Отобразить обновленные размеры коробок страницы.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) к указанному пути вывода.

```python
import sys
import aspose.pdf as ap
from os import path

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

Этот фрагмент кода читает PDF и получает размеры (ширину и высоту) первой страницы. Он использует [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API для извлечения границ страницы [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) и выводит его размер в консоль. Это полезно для просмотра макета страницы, проверки форматов или подготовки документов к дальнейшей обработке.

1. Загрузите PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Получите доступ к первой [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Получить ограничивающий прямоугольник страницы с помощью `get_page_rect()`.
1. Извлеките значения ширины и высоты.
1. Выведите размеры страницы.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Получить размер страницы PDF до и после поворота

Получите размеры страницы PDF до и после применения поворота на 90°. Это демонстрирует, как поворот влияет на ширину и высоту и как использовать `get_page_rect()` с учётом или без учёта вращения.

1. Откройте PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Получите доступ к первой [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Применить вращение на 90° используя `page.rotate = ap.Rotation.ON90` (см. [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Получить прямоугольник страницы без учета поворота с использованием `get_page_rect(False)` и вывести её ширину и высоту.
1. Получить прямоугольник страницы с учётом поворота, используя `get_page_rect(True)` и вывести её ширину и высоту.
1. Сравните, как изменяются размеры из‑за поворота.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Обрезать страницы PDF в Python](/pdf/ru/python-net/crop-pages/)
- [Получать и устанавливать свойства страниц PDF в Python](/pdf/ru/python-net/get-and-set-page-properties/)
- [Повернуть страницы PDF в Python](/pdf/ru/python-net/rotate-pages/)