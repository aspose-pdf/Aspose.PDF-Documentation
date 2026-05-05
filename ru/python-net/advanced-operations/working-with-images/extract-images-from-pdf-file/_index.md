---
title: Извлечение изображений из PDF‑файла с помощью Python
linktitle: Извлечь изображения
type: docs
weight: 30
url: /ru/python-net/extract-images-from-pdf-file/
description: Узнайте, как извлекать внедрённые изображения из PDF‑файлов с помощью Python.
lastmod: "2026-04-17"
TechArticle: true 
AlternativeHeadline: Извлеките изображения из PDF с помощью Python
Abstract: В этой статье рассматривается процесс извлечения изображений из PDF‑файлов с использованием Aspose.PDF for Python. Подчеркивается полезность разделения изображений для таких целей, как управление, архивирование, анализ или обмен. В статье объясняется, что изображения в PDF хранятся в коллекции ресурсов каждой страницы, конкретно в коллекции XImage. Чтобы извлечь изображение, пользователь может получить доступ к определённой странице и извлечь изображение, используя его индекс из коллекции Images. Объект XImage, полученный по индексу, предоставляет метод `save()`, позволяющий сохранить извлечённое изображение. Приведен фрагмент кода, демонстрирующий шаги, необходимые для открытия PDF‑документа, извлечения конкретного изображения со второй страницы по его индексу и сохранения его в файл.
---

Вам нужно отделить изображения от ваших PDF‑файлов? Для упрощённого управления, архивирования, анализа или обмена изображениями ваших документов используйте **Aspose.PDF for Python** и извлекайте изображения из PDF‑файлов.

Этот рабочий процесс полезен, когда нужно повторно использовать встроенную графику, архивировать графические ресурсы отдельно или проверять содержимое PDF для последующей обработки.

1. Загрузите PDF‑документ с помощью 'ap.Document()'.
1. Получите нужную страницу документа (document.pages[1]).
1. Выберите изображение из ресурсов страницы (например, resources.images[1]).
1. Создайте выходной поток (FileIO) для целевого файла.
1. Сохраните извлечённое изображение, используя 'xImage.save(output_image)'.

```python
import sys
import aspose.pdf as ap
from io import FileIO
from os import path

def extract_image(infile, outfile):
    document = ap.Document(infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(outfile, "w") as output_image:
        xImage.save(output_image)
```

## Извлечение изображений из определённого региона в PDF

В этом примере извлекаются изображения, расположенные в указанном прямоугольном регионе на странице PDF, и сохраняются как отдельные файлы.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Создайте 'ImagePlacementAbsorber' для сбора всех изображений на первой странице.
1. Вызовите 'document.pages[1].accept(absorber)' для анализа размещения изображений.
1. Итерируйте все изображения в 'absorber.image_placements':
    - Получите ограничивающий прямоугольник изображения (llx, lly, urx, ury).
    - Проверьте, находятся ли оба угла прямоугольника изображения внутри целевого прямоугольника (rectangle.contains()).
    - Если true, сохранять изображение в файл с помощью FileIO, заменяя 'index' в имени файла последовательным номером.
1. Увеличивайте индекс для каждого сохранённого изображения.

```python
import sys
import aspose.pdf as ap
from io import FileIO
from os import path

def extract_image_from_specific_region(infile, outfile):
    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.urx)
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Связанные темы изображений

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Заменить изображения в существующих PDF‑файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Удалить изображения из PDF‑файлов](/pdf/ru/python-net/delete-images-from-pdf-file/)
- [Добавить изображения в существующие PDF-файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)
