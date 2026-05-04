---
title: Заменить изображение в существующем PDF‑файле с использованием Python
linktitle: Заменить изображение
type: docs
weight: 70
url: /python-net/replace-image-in-existing-pdf-file/
description: Узнайте, как заменить встроенные изображения в существующих PDF‑файлах с помощью Python.
lastmod: "2026-04-17"
TechArticle: true
AlternativeHeadline: Заменить встроенное изображение PDF новым в Python
Abstract: В этой статье объясняется, как заменить существующее изображение в документе PDF с использованием Aspose.PDF for Python via .NET. Узнайте, как загрузить PDF, открыть поток заменяемого изображения, обновить ресурс изображения на целевой странице и сохранить изменённый документ в Python.
---

## Заменить изображение в PDF

Как заменить существующее изображение на странице PDF новым изображением? Реализуйте это с помощью Aspose.PDF for Python via .NET.

Используйте эту страницу, когда необходимо обновить логотипы, схемы или другие встроенные графические элементы в PDF без перестройки макета документа.

1. Импортируйте необходимые модули (aspose.pdf, os.path, FileIO).
1. Определите пути для:
    - Входной PDF (infile)
    - Новый файл изображения (image_file)
    - Выходной PDF (outfile)
1. Загрузите PDF‑документ, используя 'apdf.Document(path_infile)'.
1. Откройте новый файл изображения в бинарном режиме чтения.
1. Замените первое изображение на первой странице:
    - 'document.pages[1].resources.images.replace(1, image_stream)'
1. Сохраните обновлённый PDF в 'path_outfile'.

```python
import sys
import aspose.pdf as ap
from io import FileIO
from os import path

def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Заменить конкретное изображение

В этом примере демонстрируется, как заменить конкретное изображение на странице PDF, находя его с помощью обнаружения размещения изображения.

1. Загрузите PDF, используя 'apdf.Document()'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех размещений изображений на странице.
1. Примите поглотитель на первой странице ('document.pages[1].accept(absorber)').
1. Проверьте, существуют ли размещения изображений на странице.
1. Выберите первое размещение изображения (absorber.image_placements[1]) и замените его.
1. Сохраните изменённый PDF в 'path_outfile'.

```python
import sys
import aspose.pdf as ap
from io import FileIO
from os import path

def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = ap.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Связанные темы изображений

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Извлечь изображения из PDF‑файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
- [Добавить изображения в существующие PDF-файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)
