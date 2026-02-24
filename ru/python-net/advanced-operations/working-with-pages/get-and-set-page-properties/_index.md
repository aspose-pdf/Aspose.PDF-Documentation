---
title: Получение и установка свойств страниц с помощью Python
linktitle: Получение и установка свойств страниц
type: docs
weight: 90
url: /ru/python-net/get-and-set-page-properties/
description: Эта секция показывает, как получить количество страниц в PDF‑файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страниц.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить и установить свойства страниц с помощью Python
Abstract: Эта статья обсуждает возможности Aspose.PDF for Python via .NET, сосредотачивая внимание на чтении и установке свойств страниц в PDF‑файлах с помощью Python. В статье рассматриваются различные функции, включая определение количества страниц в PDF, доступ к свойствам страниц и их изменение, а также работу с информацией о цвете. Чтобы получить количество страниц, используются класс `Document` и коллекция `PageCollection`, при этом в примерах кода показано, как получить число страниц, даже без сохранения документа. Статья объясняет различные свойства страниц, такие как MediaBox, BleedBox, TrimBox, ArtBox и CropBox, и предоставляет примеры кода для доступа к этим свойствам. Кроме того, рассматривается извлечение конкретной страницы из PDF и сохранение её как отдельного документа, а также определение типа цвета каждой страницы. Все примеры реализованы на Python, иллюстрируя практические применения этих возможностей.
---

Аспose.PDF for Python via .NET позволяет читать и задавать свойства страниц в PDF‑файле в ваших Python‑приложениях. Эта секция показывает, как получить количество страниц в PDF‑файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страниц. Примеры используют API [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и [`КоллекцияСтраниц`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) и написаны на Python.

## Получить количество страниц в PDF‑файле

Когда работаете с документами, вы часто хотите знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF‑файле:

1. Откройте PDF‑файл, используя класс [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Затем используйте свойство Count коллекции [КоллекцияСтраниц](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (из объекта Документ), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF‑файла.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Получить количество страниц без сохранения документа

Иногда мы генерируем PDF‑файлы «на лету», и при их создании может возникнуть необходимость (создание оглавления и т.п.) получить количество страниц PDF‑файла без его сохранения на диск или в поток. Чтобы удовлетворить эту необходимость, в классе Document был введён метод [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Пожалуйста, ознакомьтесь со следующим фрагментом кода, который показывает шаги для получения количества страниц без сохранения документа.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

Каждая страница PDF‑файла имеет ряд свойств, таких как ширина, высота, bleed‑, crop‑ и trim‑box. Aspose.PDF позволяет получить доступ к этим свойствам.

### Понимание свойств страниц: различия между Artbox, BleedBox, CropBox, MediaBox, TrimBox и свойством Rect

- **Media box**: Media box — это самый большой короб (box) страницы. Он соответствует размеру страницы (например A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором отображается или печатается PDF‑документ.
- **Bleed box**: Если у документа есть bleed, PDF также будет иметь bleed‑box. Bleed — это количество цвета (или графики), которое выходит за пределы края страницы. Это используется, чтобы при печати и обрезке документа («trimmed») краска доходила до самого края страницы. Даже если страница обрезана неправильно — слегка смещена от меток обрезки — на странице не появятся белые края.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box — это короб, охватывающий фактическое содержимое страниц в вашем документе. Этот короб используется при импорте PDF‑документов в другие приложения.
- **Crop box**: Crop box — это размер «страницы», при котором ваш PDF‑документ отображается в Adobe Acrobat. В обычном режиме отображаются только содержимое crop‑box в Adobe Acrobat.
Для подробного описания этих свойств см. спецификацию Adobe.Pdf, в частности раздел 10.10.1 Page Boundaries.
-- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox (`Page.rect`). Смотрите тип [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) для свойств прямоугольника. Ниже изображение иллюстрирует эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Доступ к свойствам страниц

Класс [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) предоставляет все свойства, связанные с конкретной страницей PDF. Все страницы PDF‑файлов находятся в коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Оттуда можно получить доступ к отдельным объектам `Page` по их индексу или перебрать коллекцию, чтобы получить все страницы. После доступа к отдельной странице можно получить её свойства. Следующий фрагмент кода показывает, как получить свойства страницы (API `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Определить цвет страницы

Класс [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) предоставляет свойства, связанные с конкретной страницей PDF‑документа, включая тип цвета, который использует страница — RGB, чёрно‑белый, градации серого или неопределённый.

Все страницы PDF‑файлов находятся в коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). Свойство [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) указывает цвет элементов на странице. Чтобы получить или определить информацию о цвете конкретной страницы PDF, используйте свойство [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) объекта [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

Следующий фрагмент кода показывает, как пройтись по отдельным страницам PDF‑файла для получения информации о цвете.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


