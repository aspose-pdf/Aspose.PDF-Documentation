---
title: Заменить изображение в существующем PDF‑файле с помощью Python
linktitle: Заменить изображение
type: docs
weight: 70
url: /python-net/replace-image-in-existing-pdf-file/
description: Узнайте, как заменять встроенные изображения в существующих PDF‑файлах с помощью Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Заменяйте изображения в существующих PDF‑файлах с помощью Python
Abstract: В этой статье показано, как заменять изображения в PDF‑документах с помощью Aspose.PDF for Python via .NET. Описывается замена изображения по индексу ресурса и замена конкретного найденного изображения с помощью ImagePlacementAbsorber.
---

## Заменить изображение в PDF

Используйте эту страницу, когда нужно обновить логотипы, схемы или другие встроенные графические элементы в PDF без пересборки макета документа.

1. Загрузите исходный PDF с помощью `ap.Document(infile)`.
1. Откройте заменяемое изображение как бинарный поток.
1. Замените графический ресурс по индексу на странице.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Заменить конкретное изображение

Этот пример заменяет конкретное расположение изображения, найденное `ImagePlacementAbsorber`.

1. Загрузите исходный PDF.
1. Создайте `ImagePlacementAbsorber` и соберите размещения изображений на странице.
1. Проверьте, существуют ли какие‑либо размещения изображений на странице.
1. Замените выбранное размещение новым потоком изображения.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Связанные темы по изображениям

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Удалить изображения из PDF‑файлов](/pdf/ru/python-net/delete-images-from-pdf-file/)
- [Извлечь изображения из PDF‑файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
- [Добавить изображения в существующие PDF‑файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)
