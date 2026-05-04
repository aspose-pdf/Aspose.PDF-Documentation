---
title: Получить и установить свойства страниц PDF в Python
linktitle: Получение и установка свойств страниц
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: Узнайте, как просматривать и обновлять свойства страниц PDF, такие как размер, количество и информация о цвете, в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить и установить свойства страниц с помощью Python
Abstract: В этой статье рассматриваются возможности Aspose.PDF for Python via .NET, с упором на чтение и установку свойств страниц в PDF‑файлах с помощью Python. Статья охватывает различные функции, включая определение количества страниц в PDF, доступ к свойствам страниц и их изменение, а также работу с информацией о цвете. Для получения количества страниц используются класс `Document` и коллекция `PageCollection`, при этом в примерах кода показывается, как получить число страниц, даже без сохранения документа. В статье объясняются различные свойства страниц, такие как MediaBox, BleedBox, TrimBox, ArtBox и CropBox, и приводятся примеры кода для доступа к этим свойствам. Кроме того, рассматривается получение конкретной страницы из PDF и её сохранение как отдельного документа, а также определение типа цвета каждой страницы. Все примеры реализованы на Python, демонстрируя практическое применение этих возможностей.
---

Aspose.PDF for Python via .NET позволяет читать и устанавливать свойства страниц в PDF‑файле в ваших Python‑приложениях. В этом разделе показано, как получить количество страниц в PDF‑файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страниц. Примеры используют the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API и написаны на Python.

Используйте это руководство, когда вам необходимо просмотреть метаданные страницы, определить количество страниц или обновить характеристики на уровне страницы в рамках анализа или нормализации документов.

## Получить количество страниц в PDF‑файле

При работе с документами часто хочется знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF‑файле:

1. Откройте PDF‑файл, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Затем используйте [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) свойство Count коллекции (из объекта Document), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Получить количество страниц без сохранения документа

Иногда мы генерируем PDF‑файлы «на лету», и во время создания PDF‑файла мы можем столкнуться с требованием (создание оглавления и т.д.) получить количество страниц PDF‑файла без сохранения файла в системе или потоке. Поэтому, чтобы удовлетворить это требование, метод [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) было введено в классе Document. Пожалуйста, ознакомьтесь со следующим фрагментом кода, который показывает шаги для получения количества страниц без сохранения документа.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Получить свойства страниц

Каждая страница в файле PDF имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF позволяет получить доступ к этим свойствам.

### Понимание свойств страниц: различия между Artbox, BleedBox, CropBox, MediaBox, TrimBox и свойством Rect

- **Media box**: Media box — это самая большая область страницы. Она соответствует размеру страницы (например A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором отображается или печатается PDF‑документ.
- **Bleed box**: Если у документа есть вылет, PDF также будет иметь bleed box. Вылет — это количество цвета (или художественного оформления), которое выходит за пределы края страницы. Он используется, чтобы обеспечить, что при печати документа и подрезке до нужного размера (“trimmed”), краска дойдёт до самого края страницы. Даже если страница обрезана с ошибкой — немного смещена от линий обрезки — белые края не появятся на странице.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box — это рамка, обводящая фактическое содержание страниц вашего документа. Этот тип коробки страницы используется при импорте PDF‑документов в другие приложения.
- **Crop box**: Crop box — это размер «page», при котором ваш PDF‑документ отображается в Adobe Acrobat. В обычном режиме отображается только содержимое crop box в Adobe Acrobat.
  Для подробного описания этих свойств читайте спецификацию Adobe.Pdf, в частности раздел 10.10.1 Page Boundaries.
-- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox (`Page.rect`). См. [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) тип для свойств прямоугольника. Ниже изображение иллюстрирует эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Доступ к свойствам страницы

Эта [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) класс предоставляет все свойства, связанные с конкретной страницей PDF. Все страницы PDF‑файлов находятся в [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекция.

Оттуда можно получить доступ к отдельному `Page` объекты, используя их индекс, или перебрать коллекцию, чтобы получить все страницы. Как только отдельная страница будет доступна, мы можем получить её свойства. Следующий фрагмент кода показывает, как получить свойства страницы (the `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Определить цвет страницы

Эта [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class предоставляет свойства, связанные с конкретной страницей PDF‑документа, включая тип цвета — RGB, чёрно‑белый, градации серого или неопределённый — который использует страница.

Все страницы PDF‑файлов находятся в [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) коллекция. Эта [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property указывает цвет элементов на странице. Чтобы получить или определить информацию о цвете для конкретной страницы PDF, используйте the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объекта [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property.

В следующем фрагменте кода показано, как перебрать отдельные страницы PDF‑файла, чтобы получить информацию о цвете.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Изменить размер страницы PDF в Python](/pdf/ru/python-net/change-page-size/)
- [Обрезать страницы PDF в Python](/pdf/ru/python-net/crop-pages/)
- [Повернуть страницы PDF в Python](/pdf/ru/python-net/rotate-pages/)