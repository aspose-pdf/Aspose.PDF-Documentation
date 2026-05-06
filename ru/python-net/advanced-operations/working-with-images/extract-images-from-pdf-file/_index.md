---
title: Извлечение изображений из PDF-файла с помощью Python
linktitle: Извлечь изображения
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: Узнайте, как извлекать встроенные изображения из PDF‑файлов с помощью Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Извлечение изображений из PDF‑файлов с Python
Abstract: Эта статья демонстрирует, как извлекать изображения из PDF‑документов с помощью Aspose.PDF for Python via .NET. В ней рассматривается извлечение отдельного встроенного изображения и экспорт изображений, найденных в определённом прямоугольном регионе на странице.
---

Используйте эту страницу, когда вам нужно повторно использовать встроенную графику, архивировать графические ресурсы или обрабатывать содержимое изображений вне PDF.

1. Загрузите исходный PDF с `ap.Document(infile)`.
1. Выберите целевую страницу и индекс ресурса изображения.
1. Сохраните объект изображения в выходной поток.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Извлечение изображений из конкретного региона в PDF

Этот пример извлекает изображения, расположенные в заданной прямоугольной области на странице PDF, и сохраняет их в отдельные файлы.

1. Загрузите исходный PDF.
1. Создайте `ImagePlacementAbsorber` и примите его на целевой странице.
1. Определите целевой прямоугольник.
1. Итерируйте размещения изображений и проверьте, помещаются ли границы каждого изображения в область.
1. Сохраните найденные изображения в выходные файлы.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Связанные темы по изображениям

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Замена изображений в существующих PDF-файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Удаление изображений из PDF-файлов](/pdf/ru/python-net/delete-images-from-pdf-file/)
- [Добавление изображений в существующие PDF-файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)
