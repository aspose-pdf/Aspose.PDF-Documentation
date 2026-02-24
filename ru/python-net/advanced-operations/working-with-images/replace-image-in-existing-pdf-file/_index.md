---
title: Заменить изображение в существующем PDF файле с помощью Python
linktitle: Заменить изображение
type: docs
weight: 70
url: /ru/python-net/replace-image-in-existing-pdf-file/
description: В этом разделе описывается замена изображения в существующем PDF‑файле с использованием библиотеки Python.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Заменить изображение в PDF
Abstract: Документация Aspose.PDF for Python via .NET предоставляет всестороннее руководство по замене изображений в существующих PDF‑файлах. Эта функция важна для задач, таких как обновление логотипов, графики или других визуальных элементов в PDF‑документе без изменения его текстового содержания.
---

## Заменить изображение в PDF

Как заменить существующее изображение на странице PDF новым изображением? Реализуйте это с помощью Aspose.PDF for Python via .NET.

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

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Заменить конкретное изображение

Этот пример демонстрирует, как заменить конкретное изображение на странице PDF, обнаружив его с помощью определения размещения изображения.

1. Загрузите PDF, используя 'apdf.Document()'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех размещений изображений на странице.
1. Примите поглотитель на первой странице ('document.pages[1].accept(absorber)').
1. Проверьте, существуют ли размещения изображений на странице.
1. Выберите первое размещение изображения (absorber.image_placements[1]) и замените его.
1. Сохраните изменённый PDF в 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
