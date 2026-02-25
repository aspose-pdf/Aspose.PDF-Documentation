---
title: Использование FloatingBox для генерации текста с Python
linktitle: Использование FloatingBox
type: docs
weight: 30
url: /ru/python-net/floating-box/
description: Эта страница объясняет, как форматировать текст во всплывающем контейнере.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Инструмент FloatingBox для генерации текста
Abstract: В этой статье представлено полное руководство по использованию инструмента FloatingBox в Aspose.PDF для Python, который позволяет разработчикам размещать текст и другой контент в перемещаемых, стилизованных контейнерах на страницах PDF. Охвачены как базовые, так и продвинутые возможности, демонстрируется создание плавающих коробок, применение границ и фоновых цветов, управление многоколоночными раскладками, позиционирование абзацев и выравнивание коробок по вертикали и горизонтали. Статья также выделяет ключевые функции, такие как обрезка текста, повторение содержимого на нескольких страницах, абсолютное позиционирование и расширенный контроль макета, обеспечивая точную настройку контента PDF. Через практические примеры кода читатели узнают, как создавать визуально привлекательные и хорошо структурированные PDF, использующие все возможности контейнера FloatingBox.
---

## Основы использования инструмента FloatingBox

Инструмент [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) — специализированный контейнер для размещения текста и другого контента на странице PDF. Его главная особенность — обрезка текста, когда содержимое выходит за пределы коробки. Создайте и добавьте `FloatingBox` в [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью Aspose.PDF для Python. `FloatingBox` служит перемещаемым текстовым контейнером, позволяя более точно управлять позиционированием макета, границами и стилизацией по сравнению с обычными абзацами текста.

1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавьте [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в документ.
1. Создайте [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Установите границу коробки, используя [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) и [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Управляйте повторением коробки с помощью свойства [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties).
1. Добавьте текстовое содержимое с помощью [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Добавьте `FloatingBox` в [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Сохраните окончательный PDF‑документ, используя [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```  

В приведённом выше примере мы создаём FloatingBox шириной 400 pt и высотой 30 pt.
Также в этом примере было намеренно создано больше текста, чем помещается в заданных размерах.
В результате текст был обрезан.

![Image 1](image01.png)

Свойство [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) со значением `False` ограничивает текст одной страницой.

Если установить это свойство в `True`, текст будет перенесён на последующие страницы в том же положении.

![Image 2](image02.png)

## Расширенные функции FloatingBox

### Поддержка многоколоночного оформления

#### Многоколоночный макет (простой случай)

`FloatingBox` поддерживает многоколоночный макет. Чтобы создать такой макет, нужно задать значения свойств [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/).

* `column_widths` — строка с перечислением ширин в pt.
* `column_spacing` — строка, задающая ширину промежутка между колонками.
* `column_count` — количество колонок.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

В приведённом выше примере мы использовали дополнительную библиотеку LoremNET и создали 20 абзацев. Эти абзацы были распределены по трём колонкам и заполнили последующие страницы, пока текст не закончился.

#### Многоколоночный макет с принудительным началом колонки

Мы сделаем то же самое в следующем примере, как и в предыдущем. Отличие в том, что мы создали 3 абзаца. Мы можем заставить FloatingBox отображать каждый абзац в новой колонке. Для этого нужно установить `is_first_paragraph_in_column` при добавлении текста в объект FloatingBox.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Поддержка фона

Примените цвет фона к FloatingBox в PDF‑документе, используя Aspose.PDF для Python через .NET.
`FloatingBox` — контейнер для текста или других элементов, и присвоив [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) в качестве цвета фона, вы можете визуально выделить содержимое — полезно для заголовков, выделений или стилизованных разделов.

Этот фрагмент кода показывает, как создать простую светло‑зеленую текстовую коробку с примерным содержимым.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Поддержка позиционирования

Расположение FloatingBox на сгенерированной странице определяется свойствами `positioning_mode`, `left`, `top`.
Когда значение `positioning_mode` равно

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (значение по умолчанию)

Расположение определяется ранее размещёнными элементами; добавление элемента влияет на позицию последующих элементов. Если [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) или [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ненулевые, они также учитываются, однако комбинированная логика может быть неочевидной.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

Местоположение задаётся значениями `Left` и `Top`; оно не зависит от предыдущих элементов и не влияет на расположение последующих.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Выравнивание плавающих блоков по вертикали и горизонтали в PDF

Выравнивайте элементы `FloatingBox` на странице PDF, используя различные варианты [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) и [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) в Aspose.PDF для Python via .NET. Показано, как управлять позиционированием макета (верх, центр, низ, слева, справа) для достижения точного визуального выравнивания плавающих контейнеров. Каждому плавающему блоку назначено отдельное положение, чтобы продемонстрировать гибкость выравнивания для макета страницы, размещения заголовка/подвала или боковых аннотаций.

1. Создайте новый PDF‑документ.
1. Добавьте страницу в документ.
1. Создайте первый FloatingBox (выравнивание снизу‑справа).
1. Создайте второй FloatingBox (выравнивание по центру‑справа).
1. Создайте третий FloatingBox (выравнивание сверху‑справа).
1. Сохраните документ.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```
