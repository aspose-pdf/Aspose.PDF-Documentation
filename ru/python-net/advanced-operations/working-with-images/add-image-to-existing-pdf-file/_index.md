---
title: Добавить изображение в существующий PDF с помощью Python
linktitle: Добавить изображение в PDF
type: docs
weight: 10
url: /ru/python-net/add-image-to-existing-pdf-file/
description: Узнайте, как добавить изображение в существующий PDF‑файл с помощью Python, разместить его в фиксированных координатах, задать альтернативный текст и использовать сжатие изображения.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Добавлять изображения в существующие PDF‑файлы с помощью Python
Abstract: В этой статье показано, как добавлять изображения в PDF‑документы с помощью Aspose.PDF for Python via .NET. Рассматривается размещение изображения по фиксированным координатам, отрисовка изображений с помощью низкоуровневых PDF‑операторов, назначение альтернативного текста для доступности и внедрение изображений с использованием сжатия Flate.
---

## Добавить изображение в существующий PDF‑файл на Python

В этом примере показано, как разместить изображение в фиксированной позиции на существующей странице PDF с использованием Aspose.PDF for Python via .NET.

Используйте эти примеры, когда необходимо добавить логотип, фотографию, штамп, диаграмму или другое графическое изображение в существующую компоновку PDF. Вы можете разместить изображение с помощью координат страницы, отрисовать его операторами, добавить текст доступности или управлять сжатием изображения.

1. Загрузите существующий PDF с `ap.Document(infile)`.
1. Выберите целевую страницу (`document.pages[1]` для первой страницы).
1. Вызов `page.add_image()` с:
    - Путь к файлу изображения.
    - A `Rectangle` определение координат размещения.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Добавить изображение в PDF с помощью операторов

Этот подход добавляет изображение с помощью низкоуровневых операторов PDF вместо высокоуровневых `add_image()` помощник.

1. Создайте новый `Document` и добавить страницу.
1. Добавьте изображение в ресурсы страницы (`page.resources.images`).
1. Создайте операторы преобразования (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Добавьте операторы в содержимое страницы.
1. Сохраните полученный PDF.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Добавить изображение в PDF с альтернативным текстом

В этом примере добавляется изображение и задаётся альтернативный текст для доступности.

1. Создайте новый `Document` и добавить страницу.
1. Добавьте изображение на страницу с `page.add_image()`.
1. Получите ресурсы изображений из `page.resources.images`.
1. Установите альтернативный текст с помощью `try_set_alternative_text()`.
1. Сохраните полученный PDF.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Добавить изображение в PDF с Flate‑сжатием

Этот пример встраивает изображение с помощью `ImageFilterType.FLATE` сжатие.

1. Создайте новый `Document` и добавить страницу.
1. Добавьте изображение к ресурсам страницы с Flate‑сжатием.
1. Используйте матричные операторы для размещения и отрисовки изображения.
1. Сохраните документ.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Связанные темы изображений

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Замена изображений в существующих PDF‑файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Удалить изображения из PDF‑файлов](/pdf/ru/python-net/delete-images-from-pdf-file/)
- [Извлечь изображения из PDF‑файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
