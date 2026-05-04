---
title: Получать и искать изображения в PDF
linktitle: Получать и искать изображения
type: docs
weight: 40
url: /python-net/search-and-get-images-from-pdf-document/
description: Узнайте, как искать и проверять изображения в PDF‑документах с помощью Python.
lastmod: "2026-04-17"
TechArticle: true
AlternativeHeadline: Ищите встроенные изображения и проверяйте расположение изображений в PDF‑файлах с помощью Python
Abstract: В этой статье объясняется, как находить и проверять изображения в PDF‑документах с помощью Aspose.PDF for Python via .NET. Узнайте, как использовать ImagePlacementAbsorber для анализа размещения изображений, их размера и разрешения на страницах PDF и программно получать информацию об изображениях в Python.
---

## Проверка свойств размещения изображений на странице PDF

В этом примере показано, как проанализировать и отобразить свойства всех изображений на конкретной странице PDF с использованием Aspose.PDF for Python via .NET.

Используйте эту страницу, когда необходимо провести аудит размещения изображений, проверить разрешение изображений или идентифицировать встроенные объекты изображений на страницах PDF.

1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений на первой странице.
1. Итерируйтесь через 'absorber.image_placements' и выводите ключевые свойства каждого изображения:
    - Ширина и высота (points).
    - Координаты нижнего левого X (LLX) и нижнего левого Y (LLY).
    - Горизонтальное (X) и вертикальное (Y) разрешение (DPI).

```python
import sys
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing
from os import path

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Извлечь и подсчитать типы изображений в PDF

Эта функция анализирует все изображения на первой странице PDF и подсчитывает, сколько из них в градациях серого и RGB.

1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Инициализировать счётчики для изображений в градациях серого и RGB.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений.
1. Выведите общее количество найденных изображений.
1. Переберите каждое изображение в 'absorber.image_placements':
    - Получите тип цвета изображения, используя 'image_placement.image.get_color_type()'.
    - Увеличьте соответствующий счётчик (grayscaled или rgb).
    - Выведите сообщение для каждого изображения, указывающее, является ли оно оттенком серого или RGB.

```python
import sys
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing
from os import path

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.        
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Извлечь подробную информацию об изображениях из PDF

Эта функция анализирует все изображения на первой странице PDF и вычисляет их масштабированные размеры и эффективное разрешение на основе графических преобразований страницы.

1. Загрузить PDF и инициализировать переменные
1. Собрать ресурсы изображений
1. Обрабатывать операторы содержимого страницы:
    - 'GSave' - поместить текущую CTM в стек.
    - 'GRestore' - извлечь последнюю CTM из стека.
    - 'ConcatenateMatrix' - обновить текущую CTM, умножив её на матрицу оператора.
1. Вывести имя изображения, масштабированные размеры и рассчитанное разрешение.

```python
import sys
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing
from os import path

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Извлечь альтернативный текст из изображений в PDF

Эта функция извлекает альтернативный текст (alt text) со всех изображений на первой странице PDF, что полезно для проверок доступности и соответствия PDF/UA.

1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Примите абсорбер на первой странице (page.accept(absorber)).
1. Переберите каждое изображение в 'absorber.image_placements':
    - Выведите имя изображения в коллекции ресурсов страницы (get_name_in_collection()).
    - Получить альтернативный текст, используя 'get_alternative_text(page)'.
    - Выведите первую строку альтернативного текста.

```python
import sys
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing
from os import path

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Связанные темы изображений

- [Работа с изображениями в PDF с помощью Python](/pdf/ru/python-net/working-with-images/)
- [Извлечь изображения из PDF файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
- [Заменить изображения в существующих PDF‑файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Добавить изображения в существующие PDF‑файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)
