---
title: Обрезка страниц PDF с использованием Python
linktitle: Обрезка страниц PDF
type: docs
weight: 70
url: /ru/python-net/crop-pages/
description: Вы можете изменить свойства страницы, такие как ширина, высота, области Bleed, Crop и Trim, используя Aspose.PDF for Python через .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить доступ и изменить свойства страниц в PDF с помощью Python
Abstract: Статья предоставляет обзор того, как получить доступ и изменить свойства страниц в PDF‑документе с использованием Aspose.PDF for Python. В ней описываются несколько свойств страниц, включая media box, bleed box, trim box, art box и crop box, с объяснением их роли в определении размеров и границ страницы PDF для печати и отображения. Media box представляет собой самый большой размер страницы, тогда как bleed box обеспечивает покрытие краёв страницы краской при обрезке. Trim box обозначает окончательный размер документа после обрезки, а art box охватывает фактическое содержимое страницы. Crop box определяет видимую область в Adobe Acrobat. В статье включён фрагмент кода Python, демонстрирующий, как установить новый crop box вместе с другими коробками для конкретной страницы PDF‑документа. Визуальные примеры показывают внешний вид страницы до и после применения обрезки, демонстрируя практическое применение изменения этих свойств.
---

## Получить свойства страницы

Каждая страница PDF‑файла имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF for Python позволяет получать доступ к этим свойствам.

- **media_box**: Media box — самый большой коробочный элемент страницы. Он соответствует размеру страницы (например A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором отображается или печатается PDF‑документ.
- **bleed_box**: Если у документа есть bleed, PDF также будет иметь bleed‑box. Bleed — это количество цвета (или графики), выходящее за пределы края страницы. Он используется, чтобы обеспечить, что при печати и резке ("обрезке") чернила дойдут до самого края страницы. Даже если страница обрезана неточно — слегка смещена от линий обрезки — белые края не появятся.
- **trim_box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **art_box**: Art box — коробка, окружающая фактическое содержание страниц вашего документа. Эта коробка используется при импорте PDF‑документов в другие приложения.
- **crop_box**: Crop box — это «размер страницы», в котором ваш PDF‑документ отображается в Adobe Acrobat. В обычном режиме просмотра отображается только содержимое crop box в Adobe Acrobat. Для подробного описания этих свойств см. спецификацию Adobe.Pdf, особенно раздел 10.10.1 «Границы страниц».

Обрежьте первую [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) PDF до конкретного прямоугольного участка с помощью Aspose.PDF for Python. Функция корректирует несколько коробок страницы — `crop_box`, `trim_box`, `art_box` и `bleed_box` — чтобы обеспечить согласованные визуальные результаты. Обрезка может быть полезна для удаления нежелательных полей или фокусировки на определённом участке страницы.

1. Загрузите PDF как [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (используйте `ap.Document()`).
1. Определите прямоугольник обрезки с помощью [`Прямоугольник`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) с нужными координатами (в пунктах).
1. Установите `crop_box`, `trim_box`, `art_box` и `bleed_box` у [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в определённый прямоугольник.
1. Сохраните изменённый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в новый выходной файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

В этом примере мы использовали примерный файл [здесь](crop_page.pdf). Изначально наша страница выглядит, как показано на рисунке 1.
![Рисунок 1. Обрезанная страница](crop_page.png)

После изменения страница будет выглядеть как на рисунке 2.
![Рисунок 2. Обрезанная страница](crop_page2.png)

## Обрезать страницу PDF на основе содержимого первого изображения

Обрежьте первую [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) динамически, основываясь на границах первого изображения, найденного на странице. С помощью [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/) скрипт определяет первое изображение и корректирует `crop_box` страницы, чтобы он соответствовал размерам изображения. Такой подход полезен, когда вы хотите сосредоточиться на конкретном визуальном содержимом, а не на заранее заданных координатах.

1. Загрузите PDF как [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Найдите изображения на первой странице с помощью [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Проверьте, существуют ли изображения:
- Если найдено, установите `crop_box` у [`Страница`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в соответствии с [`Прямоугольник`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) первого изображения.
- Если нет, оставьте страницу без изменений и уведомьте пользователя.
1. Сохраните изменённый [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в указанный выходной файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
