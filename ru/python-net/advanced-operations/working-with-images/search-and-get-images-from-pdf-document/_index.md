---
title: Получать и искать изображения в PDF
linktitle: Получать и искать изображения
type: docs
weight: 40
url: /ru/python-net/search-and-get-images-from-pdf-document/
description: Узнайте, как искать и получать изображения из PDF‑документа на Python с помощью Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Поиск и извлечение изображений из PDF
Abstract: Библиотека Aspose.PDF для Python через .NET предоставляет мощные возможности для поиска и извлечения изображений из PDF‑документов. Используя класс 'ImagePlacementAbsorber', разработчики могут эффективно находить и получать доступ к изображениям, встроенным на всех страницах PDF.
---

## Просмотр свойств размещения изображений на странице PDF

Этот пример демонстрирует, как проанализировать и отобразить свойства всех изображений на конкретной странице PDF с использованием Aspose.PDF для Python через .NET.

1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений на первой странице.
1. Пройдите по 'absorber.image_placements' и отобразите ключевые свойства каждого изображения:
- Ширина и высота (в пунктах).
- Координаты нижнего левого угла X (LLX) и Y (LLY).
- Горизонтальное (X) и вертикальное (Y) разрешение (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Извлечение и подсчёт типов изображений в PDF

Эта функция анализирует все изображения на первой странице PDF и подсчитывает, сколько из них в градациях серого и RGB.

1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Инициализируйте счётчики для изображений в градациях серого и RGB.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений.
1. Выведите общее количество найденных изображений.
1. Пройдите по каждому изображению в 'absorber.image_placements':
- Получите тип цвета изображения с помощью 'image_placement.image.get_color_type()'.
- Увеличьте соответствующий счётчик (градации серого или rgb).
- Выведите сообщение для каждого изображения, указывающее, является ли оно черно‑белым или RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## Извлечение подробной информации об изображениях из PDF

Эта функция анализирует все изображения на первой странице PDF и вычисляет их масштабированные размеры и эффективное разрешение на основе графических трансформаций страницы.

1. Загрузите PDF и инициализируйте переменные
1. Соберите ресурсы изображений
1. Обработайте операторы содержимого страницы:
- 'GSave' — поместить текущую матрицу преобразования (CTM) в стек.
- 'GRestore' — извлечь последнюю CTM из стека.
- 'ConcatenateMatrix' — обновить текущую CTM, умножив её на матрицу оператора.
1. Выведите имя изображения, масштабированные размеры и рассчитанное разрешение.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Извлечение альтернативного текста из изображений в PDF

Эта функция извлекает альтернативный текст (alt‑text) из всех изображений на первой странице PDF, полезный для проверок доступности и соответствия PDF/UA.

1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на странице.
1. Примите поглотитель на первой странице (page.accept(absorber)).
1. Пройдите по каждому изображению в 'absorber.image_placements':
- Выведите имя изображения в коллекции ресурсов страницы (get_name_in_collection()).
- Получите альтернативный текст с помощью 'get_alternative_text(page)'.
- Выведите первую строку alt‑текста.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
