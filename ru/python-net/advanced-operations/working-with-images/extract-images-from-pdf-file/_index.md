---
title: Извлечение изображений из PDF-файла с помощью Python
linktitle: Извлечь изображения
type: docs
weight: 30
url: /ru/python-net/extract-images-from-pdf-file/
description: Этот раздел показывает, как извлекать изображения из PDF-файла с помощью библиотеки Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Извлечение изображений из PDF с помощью Python
Abstract: В этой статье рассматривается процесс извлечения изображений из PDF‑файлов с использованием Aspose.PDF для Python. Описывается полезность отделения изображений для таких целей, как управление, архивирование, анализ или обмен. В статье объясняется, что изображения в PDF хранятся в коллекции ресурсов каждой страницы, конкретно в коллекции XImage. Чтобы извлечь изображение, пользователь может получить доступ к определённой странице и извлечь изображение по его индексу из коллекции Images. Объект XImage, возвращённый по индексу, предоставляет метод `save()` для сохранения извлечённого изображения. Приведен фрагмент кода, демонстрирующий шаги, необходимые для открытия PDF‑документа, извлечения конкретного изображения со второй страницы по индексу и сохранения его в файл.
---

Нужно отделить изображения от ваших PDF‑файлов? Для упрощённого управления, архивирования, анализа или обмена изображениями ваших документов используйте **Aspose.PDF for Python** и извлекайте изображения из PDF‑файлов.

1. Загрузите PDF‑документ с помощью 'ap.Document()'.
1. Получите доступ к нужной странице документа (document.pages[1]).
1. Выберите изображение из ресурсов страницы (например, resources.images[1]).
1. Создайте поток вывода (FileIO) для целевого файла.
1. Сохраните извлечённое изображение, используя 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Извлечение изображений из определённого региона в PDF

Этот пример извлекает изображения, находящиеся в указанном прямоугольном регионе на странице PDF, и сохраняет их в отдельные файлы.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на первой странице.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений.
1. Пройдитесь по всем изображениям в 'absorber.image_placements':
- Получите ограничивающий прямоугольник изображения (llx, lly, urx, ury).
- Проверьте, находятся ли обе вершины прямоугольника изображения внутри целевого прямоугольника (rectangle.contains()).
- Если условие истинно, сохраните изображение в файл с помощью FileIO, заменив 'index' в имени файла последовательным номером.
1. Увеличьте индекс для каждого сохранённого изображения.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Извлечение информации об изображении из PDF

Пример ниже демонстрирует, как анализировать изображения, встроенные в страницу PDF, и рассчитывать их эффективное разрешение.

1. Откройте PDF с помощью 'ap.Document'.
1. Отслеживайте состояние графики при чтении содержимого страницы.
1. Обрабатывайте операторы:
- 'GSave'/'GRestore' - добавить/удалить матрицу.
- 'ConcatenateMatrix' - обновить преобразование.
- 'Do' - если это изображение, получить размер и применить преобразование.
1. Рассчитайте эффективное DPI.
1. Выведите имя изображения, масштабированный размер и DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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
