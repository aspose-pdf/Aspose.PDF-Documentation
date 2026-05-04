---
title: Используйте FloatingBox для размещения текста PDF в Python
linktitle: Использование FloatingBox
type: docs
weight: 30
url: /python-net/floating-box/
description: Узнайте, как использовать FloatingBox для верстки текста и стилизованных контейнеров содержимого в PDF‑документах на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Создайте стилизованные плавающие текстовые контейнеры в PDF‑файлах с помощью Python.
Abstract: В этой статье объясняется, как использовать FloatingBox в Aspose.PDF for Python via .NET. Узнайте, как размещать текст и другое содержимое в стилизованных плавающих контейнерах, управлять макетом, границами, выравниванием и отсечением, а также создавать более структурированные дизайны страниц PDF на Python.
---

## Основы использования инструмента FloatingBox

[`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) инструмент является специализированным контейнером для размещения текста и другого контента на странице PDF. Его главная особенность — обрезка текста, когда содержимое превышает границы коробки. Создайте и добавьте `FloatingBox` к a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя Aspose.PDF для Python. A `FloatingBox` служит перемещаемым текстовым контейнером, предоставляя больший контроль над позиционированием макета, границами и стилизацией по сравнению с обычными текстовыми абзацами.

1. Создать новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавить [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в документ.
1. Создать [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Установить границу коробки с помощью [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) и [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Повторение контрольного окна с [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) свойство.
1. Добавить текстовое содержимое с помощью [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Добавить `FloatingBox` к [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Сохраните окончательный PDF документ, используя [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def create_and_add_floating_box(outfile):
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
Кроме того, в этом примере было намеренно создано больше текста, чем могло поместиться в заданный размер.
В результате текст был обрезан.

![Изображение 1](image01.png)

Свойство [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) с `False` значение ограничивает текст одной страницей.

Если установить это свойство в `True` Текст будет переходить на последующие страницы в том же положении.

![Изображение 2](image02.png)

## Расширенные функции FloatingBox

### Поддержка многоколоночного режима

#### Многоколоночный макет (простой случай)

`FloatingBox` поддерживает многоколоночный макет. Чтобы создать такой макет, вы должны определить значения [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) свойства.

* `column_widths` это строка с перечислением ширины в pt.
* `column_spacing` это строка с шириной промежутка между столбцами.
* `column_count` является числом столбцов.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
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

Мы использовали дополнительную библиотеку LoremNET в приведённом выше примере и создали 20 абзацев. Эти абзацы были разделены на три колонки и заполнили последующие страницы, пока не закончился текст.

#### Многоколоночный макет с принудительным началом колонки

Мы сделаем то же самое с следующим примером, как и с предыдущим. Разница в том, что мы создали 3 абзаца. Мы можем заставить FloatingBox отображать каждый абзац в новой колонке. Для этого нам нужно установить `is_first_paragraph_in_column` когда мы добавляем текст в объект FloatingBox.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
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

Применить цвет фона к FloatingBox в PDF‑документе, используя Aspose.PDF for Python via .NET.
А `FloatingBox` является контейнером для текста или других элементов, и при назначении [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) используя цвет фона, вы можете визуально выделить содержимое — это полезно для заголовков, выделений или оформленных разделов.

Этот фрагмент кода показывает, как создать простой светло‑зелёный текстовый блок с примерным содержимым.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
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

Местоположение FloatingBox на сгенерированной странице определяется `positioning_mode`, `left`, `top` свойства.
Когда `positioning_mode` значение равно

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (значение по умолчанию)

Расположение определяется ранее размещёнными элементами; добавление элемента влияет на расположение последующих элементов. Если [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) или [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) не нулевые, они тоже учитываются, но комбинированная логика может быть неочевидна.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

Местоположение указывается `Left` и `Top` значения; они не зависят от предыдущих элементов и не влияют на расположение последующих.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
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

### Выровнять плавающие блоки с вертикальным и горизонтальным выравниванием в PDF

Выровнять `FloatingBox` элементы внутри страницы PDF, используя разные [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) и [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) опции в Aspose.PDF for Python via .NET. Показано, как контролировать позиционирование макета (top, center, bottom, left, right) для точного визуального выравнивания плавающих контейнеров. Каждый плавающий блок получает отдельную позицию, демонстрируя гибкость выравнивания для расположения элементов на странице, размещения заголовков/подвалов или боковых аннотаций.

1. Создайте новый PDF-документ.
1. Добавьте Page в Document.
1. Создайте первый FloatingBox (выравнивание в нижнем правом углу).
1. Создать второй FloatingBox (центр‑правое выравнивание).
1. Создайте третий FloatingBox (выравнивание в верхнем правом углу).
1. Сохранить Document.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
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

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Добавление текста в PDF](/pdf/ru/python-net/add-text-to-pdf-file/)
- [Форматировать текст PDF с помощью Python](/pdf/ru/python-net/text-formatting-inside-pdf/)
- [Добавить всплывающие подсказки к тексту PDF в Python](/pdf/ru/python-net/pdf-tooltip/)