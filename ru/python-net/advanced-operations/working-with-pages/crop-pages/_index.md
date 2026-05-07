---
title: Обрезать страницы PDF в Python
linktitle: Обрезка страниц PDF
type: docs
weight: 70
url: /ru/python-net/crop-pages/
description: Узнайте, как обрезать страницы PDF-файлов и настраивать параметры обрезки, кадрирования, полей обрезки и медиа-блоков в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить доступ к свойствам страниц в PDF и изменить их с помощью Python
Abstract: Статья предоставляет обзор того, как получить доступ к свойствам страниц и изменить их в PDF‑документе с использованием Aspose.PDF for Python. В ней описываются несколько свойств страниц, включая media box, bleed box, trim box, art box и crop box, с объяснением их роли в определении размеров и границ страницы PDF для печати и отображения. Media box представляет собой наибольший размер страницы, тогда как bleed box обеспечивает покрытие чернилами за пределами края страницы для обрезки. Trim box определяет окончательный размер документа после обрезки, а art box охватывает фактическое содержимое страницы. Crop box задаёт видимую область в Adobe Acrobat. В статье приведён фрагмент кода на Python, демонстрирующий, как установить новый crop box вместе с другими ограничителями для конкретной страницы в PDF‑документе. Визуальные примеры показывают вид страницы до и после применения обрезки, демонстрируя практическое применение изменения этих свойств.
---

## Получить свойства страниц

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, поля обрезки, поля кадрирования и обрезки. Aspose.PDF для Python позволяет получить доступ к этим свойствам.

Используйте эту страницу, когда вам нужно уменьшить видимую область страницы, подготовить файлы для печати или проверить геометрию полей страницы в PDF-документах.

- **media_box**: Поле для медиафайлов — это самое большое поле страницы. Оно соответствует размеру страницы (например, A4, A5, US Letter и т. д.), выбранному при печати документа в PostScript или PDF. Другими словами, поле для медиафайлов определяет физический размер носителя, на котором отображается или печатается PDF-документ.
- **bleed_box**: Если документ имеет поля обрезки, PDF-файл также будет иметь поле обрезки. Поле обрезки — это количество цвета (или изображения), которое выходит за край страницы. Оно используется для того, чтобы при печати и обрезке документа («обрезании») чернила доходили до самого края страницы. Даже если страница обрезана неточно — слегка за пределами меток обрезки — белые края на странице не появятся.
- **trim_box**: Поле обрезки указывает окончательный размер документа после печати и обрезки.
- **art_box**: Поле для изображения — это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка используется при импорте PDF-документов в другие приложения.
- **crop_box**: Поле обрезки — это размер «страницы», в котором ваш PDF-документ отображается в Adobe Acrobat. В обычном режиме просмотра в Adobe Acrobat отображается только содержимое поля обрезки. Для подробного описания этих свойств см. спецификацию Adobe.PDF, в частности, раздел 10.10.1 «Границы страницы».

Обрежьте первую [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) PDF-файла до определенной прямоугольной области с помощью Aspose.PDF для Python. Эта функция регулирует несколько блоков страницы — `crop_box`, `trim_box`, `art_box` и `bleed_box` — для обеспечения единообразного визуального результата. Обрезка может быть полезна для удаления ненужных полей или выделения определенной области страницы.

1. Загрузите PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (использовать `ap.Document()`).
1. Определите прямоугольник обрезки, используя [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) с желаемыми координатами (в пунктах).
1. Установите [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, и `bleed_box` к определённому прямоугольнику.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в новый выходной файл.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

В этом примере мы использовали образец файла [here](crop_page.pdf). Изначально наша страница выглядит, как показано на рисунке 1.
![Рисунок 1. Обрезанная страница](crop_page.png)

После изменения страница будет выглядеть как на рисунке 2.
![Рисунок 2. Обрезанная страница](crop_page2.png)

## Обрезать страницу PDF на основе содержимого первого изображения

Обрезать первый [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) динамически, исходя из границ первого найденного на странице изображения. Используя [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), скрипт определяет первое изображение и корректирует страницу `crop_box` соответствовать размерам изображения. Этот подход полезен, когда вы хотите сосредоточиться на конкретном визуальном контенте, а не на предопределённых координатах.

1. Загрузите PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Найдите изображения на первой странице с помощью [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Проверьте наличие изображений:
    - Если найдено, установите [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` соответствовать первому изображению [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Если нет, оставьте страницу без изменений и уведомите пользователя.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в указанный выходной файл.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Изменить размер страницы PDF в Python](/pdf/ru/python-net/change-page-size/)
- [Получать и устанавливать свойства страниц PDF в Python](/pdf/ru/python-net/get-and-set-page-properties/)
- [Повернуть страницы PDF в Python](/pdf/ru/python-net/rotate-pages/)