---
title: Добавить изображение в PDF с помощью Python
linktitle: Добавить изображение
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: Узнайте, как добавить изображения в существующие PDF‑файлы с помощью Python.
lastmod: "2026-04-17"
TechArticle: true 
AlternativeHeadline: Как добавить изображения в PDF с помощью Python
Abstract: В этой статье предоставляются рекомендации по добавлению изображений в существующие PDF‑файлы с использованием Python и библиотеки Aspose.PDF. Описываются два метода достижения этой цели. Первый метод подразумевает использование класса `Document` из Aspose.PDF, где пользователь загружает PDF, указывает номер страницы и использует метод `add_image` класса `Page` для размещения изображения. Затем документ сохраняется с помощью метода `save()`. Второй метод использует класс `PdfFileMend` из пространства имён Aspose.PDF.Facades, который предлагает более простой интерфейс. Здесь вызывается метод `add_image()` для добавления изображения на указанную страницу и координаты, после чего сохраняется обновлённый PDF и закрывается объект `PdfFileMend`. Для обоих методов приведены фрагменты кода, демонстрирующие процесс.
---

## Добавить изображение в существующий PDF‑файл

В этом примере демонстрируется, как вставить изображение в определённую позицию на странице PDF, используя Aspose.PDF for Python via .NET.

Используйте эту страницу, когда нужно разместить логотипы, фотографии или другие графические элементы на фиксированных координатах внутри существующей разметки PDF.

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Выберите целевую страницу 'document.pages[1]' - первая страница.
1. Используйте 'page.add_image()' для размещения изображения:
    - Путь к файлу изображения.
    - Объект 'Rectangle', определяющий координаты изображения (left=20, bottom=730, right=120, top=830).
1. Сохраните обновлённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Add an Image Using Operators

Следующий фрагмент кода показывает низкоуровневый подход к добавлению изображения в страницу PDF, вручную работая с PDF‑операторами, а не используя высокоуровневые вспомогательные методы.

Шаги:

1. Создайте новый пустой 'Document'.
1. Добавьте страницу и задайте её размер (842 × 595 - landscape A4).
1. Получите доступ к ресурсам изображений страницы (page.resources.images).
1. Загрузите файл изображения в поток и добавьте его в ресурсы.
    - Метод возвращает ‘image_id’.
    - Ново добавленный объект изображения извлекается из ресурсов.
1. Определите прямоугольник, сохраняющий соотношение сторон изображения:
1. Соберите последовательность операторов:
    - 'GSave()' - Сохранить текущее графическое состояние.
    - 'ConcatenateMatrix(matrix)' - Применить преобразование (масштабировать и центрировать изображение вертикально на странице).
    - 'Do(image_id)' - Отобразить изображение.
    - 'GRestore()' - Восстановить графическое состояние.
1. Добавьте последовательность операторов в 'page.contents'.
1. Сохраните полученный PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

# Add image to resources
image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
image_id = resources_images.add(image_stream)

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream)

rectangle = ap.Rectangle(
    0,
    0,
    page.media_box.width,
    (page.media_box.width * x_image.height) / x_image.width,
    True,
)

# Create operator sequence for adding image
operators = []

# Save graphics state
operators.append(ap.operators.GSave())

# Set transformation matrix (position and size)
matrix = ap.Matrix(
    rectangle.urx - rectangle.llx,
    0,
    0,
    rectangle.ury - rectangle.lly,
    rectangle.llx,
    rectangle.llx + (page.media_box.height - rectangle.height) / 2,
)
operators.append(ap.operators.ConcatenateMatrix(matrix))

# Draw the image
operators.append(ap.operators.Do(image_id))

# Restore graphics state
operators.append(ap.operators.GRestore())

# Add operators to page contents
page.contents.add(operators)

    # Add operators to page contents
    page.contents.add(operators)

    document.save(outfile)
```

## Добавить изображение с альтернативным текстом

Этот пример показывает, как добавить изображение на страницу PDF и задать альтернативный текст (alt text) для соответствия требованиям доступности (например, PDF/UA).

1. Создайте новый 'Document' и добавьте страницу (842 × 595, альбомный A4).
1. Разместите изображение на странице, используя 'page.add_image()', с прямоугольником, охватывающим всю страницу.
1. Получите доступ к ресурсам изображений страницы ('page.resources.images').
1. Определите строку альтернативного текста (например, 'Alternative text for image').
1. Получите первый объект изображения из ресурсов ('x_image = resources_images[1]').
1. Используйте 'try_set_alternative_text(alt_text, page)' для назначения альтернативного текста изображению.
1. Сохраните полученный PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_set_alternative_text_for_image(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))

# If set is successful, then get the alternative text for the image
if result:
    print("Text has been added successfuly")
document.save(path_outfile)
```

## Добавить изображение в PDF со сжатием Flate

Вставьте изображение в PDF‑документ с помощью Python и Aspose.PDF, используя сжатие Flate. Скрипт добавляет изображение в ресурсы страницы, позиционирует его с помощью матрицы преобразования и отрисовывает на странице для эффективного встраивания изображения в PDF.

1. Создать новый PDF‑документ.
1. Доступ к ресурсам изображений страниц.
1. Загрузить файл изображения.
1. Добавить изображение с Flate‑сжатием.
1. Сохранить состояние графики.
1. Определить координаты размещения.
1. Создать прямоугольник размещения.
1. Создать матрицу преобразования.
1. Применить матрицу к странице.
1. Нарисуйте изображение.
1. Восстановить состояние графики.
1. Сохранить PDF.

```python
import sys
import aspose.pdf as ap
from os import path
from io import FileIO

def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    # Save the current graphics state
    page.contents.add([ap.operators.GSave()])

    # Set coordinates for the image placement
    lowerLeftX = 0
    lowerLeftY = 0
    upperRightX = 600
    upperRightY = 600

    rectangle = ap.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY, True)

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    # Use ConcatenateMatrix operator to define how the image must be placed
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])

    # Restore the graphics state
    page.contents.add([ap.operators.GRestore()])

    # Save the document
    document.save(outfile)
```

## Связанные темы изображений

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Заменить изображения в существующих PDF‑файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Удалить изображения из PDF‑файлов](/pdf/ru/python-net/delete-images-from-pdf-file/)
- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Извлечь изображения из PDF‑файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
