---
title: Добавление таблиц в PDF с помощью Python
linktitle: Добавление таблиц
type: docs
weight: 10
url: /ru/python-net/adding-tables/
description: Узнайте, как добавлять и настраивать таблицы в существующих PDF‑документах с помощью Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить таблицу в PDF с помощью Python
Abstract: Эта статья предоставляет исчерпывающее руководство по созданию и работе с таблицами в PDF‑документах с использованием библиотеки Aspose.PDF for Python via .NET. В ней подробно описаны шаги по добавлению таблиц в существующие PDF‑файлы, включая настройку границ таблицы, отступов и полей. Кроме того, рассматриваются продвинутые функции, такие как объединение колонок и строк с использованием `col_span` и `row_span`, применение различных настроек AutoFit и динамическое получение ширины таблицы. В статье также демонстрируется вставка SVG‑изображений в ячейки таблицы и принудительное разрывание страниц или отображение таблиц на новых страницах. Фрагменты кода иллюстрируют каждую функцию, показывая, как эффективно управлять макетом и содержимым таблиц в PDF‑документах.
---

Добавление таблиц в существующие PDF‑документы является распространённой задачей для улучшения представления данных, структурирования информации или создания отчётов. **Aspose.PDF for Python via .NET** предлагает комплексное решение этой задачи, позволяя разработчикам бесшовно вставлять таблицы в существующие PDF‑файлы.

Это руководство предоставляет пошаговый подход к добавлению таблиц в существующие PDF‑документы с использованием Aspose.PDF for Python via .NET. Оно охватывает инициализацию таблицы, установку ширины столбцов, определение границ, заполнение строк и ячеек, а также сохранение изменённого документа. Кроме того, в руководстве рассматриваются расширенные функции, такие как работа с границами ячеек, применение отступов и внутренних полей, а также использование настроек AutoFit для динамической коррекции размеров таблицы.

Если вы хотите улучшить визуальную привлекательность ваших PDF-файлов или более эффективно организовать данные, это руководство служит ценным ресурсом для использования мощных возможностей управления таблицами в Aspose.PDF for Python.

## Создание базовых таблиц

### Создание таблицы

Этот пример демонстрирует, как создать таблицу в PDF‑документе с границами и несколькими строками.

1. Создайте новый PDF-документ.
1. Добавляет пустую страницу в документ.
1. Инициализировать таблицу.
1. Установите общую границу таблицы.
1. Установите границу для отдельных ячеек.
1. Добавить строки и ячейки.
1. Вставьте таблицу на страницу.
1. Сохраните PDF в указанное место.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Create a loop to add 10 rows
    for row_count in range(10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(outfile)
```

### Добавление изображений в ячейки таблицы

Этот фрагмент кода показывает, как вставлять изображения в ячейки таблицы в PDF‑документе.

1. Создайте новый PDF-документ.
1. Инициализировать таблицу.
1. Установите ширину столбцов в пунктах.
1. Текстовый фрагмент добавлен в первую ячейку.
1. Экземпляр 'ap.Image()' добавлен во вторую ячейку.
1. Установите путь к файлу изображения с 'img.file'.
1. Теги 'img.fix_width' и 'img.fix_height' управляют размером изображения внутри ячейки.
1. Вставьте таблицу на страницу PDF.
1. Сохраните PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_image(image: str, outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = image
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

Вы можете добавлять SVG‑изображения в ячейки таблицы PDF‑документа:

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_svg_image(images: list[str], outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = image
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

### ColSpan и RowSpan в таблицах

Этот пример показывает, как объединять ячейки таблицы вертикально и горизонтально для создания сложных макетов таблиц.

1. Установите общую границу таблицы.
1. Установить границы ячеек по умолчанию.
1. Объединить две ячейки по горизонтали в одну.
1. Объединить ячейку вертикально через две строки.
1. Строка 5 учитывает объединение строк, пропуская объединённый столбец.
1. Вставьте таблицу на страницу.
1. Сохраните PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_rowspan_or_colspan(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Add 1st row to table
    row1 = table.rows.add()
    for cell_count in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cell_count))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

![Демонстрация ColSpan и RowSpan](colspan_rowspan.png)

### Применение границ к таблицам и ячейкам

Этот пример показывает, как установить отступы ячеек, поля таблицы и управлять переносом слов в тексте ячеек таблицы.

1. Установите ширины столбцов.
1. Определите границы таблицы и ячеек.
1. Установите внутренний отступ в ячейках для согласованного интервала.
1. Примените отступ ко всем ячейкам по умолчанию.
1. Добавить текст и управление обтеканием.
1. Добавить строки и ячейки.
1. Сохраните PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_borders(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(outfile)
```

![Отступ и граница в таблице PDF](margin-border.png)

## Разметка таблицы и размеры

### Автоподгонка столбцов и строк

Этот фрагмент кода показывает, как автоматически подгонять ширину столбцов таблицы под страницу.
Обратите внимание, что в параметре table.column_widths = "50 50 50" - его пункты. Но вы также можете указать сантиметры (cm), дюймы или %.

1. Установить начальные ширины столбцов.
1. Автоматически подгоняет столбцы под ширину страницы.
1. Определить границы ячеек и таблицы.
1. Свойство 'table.default_cell_padding' использует 'MarginInfo()' для обеспечения одинакового отступа внутри ячеек.
1. Добавляйте строки с помощью 'table.rows.add()', а ячейки — с помощью 'row.cells.add()'.
1. Сохраните PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def auto_fit(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(outfile)
```

### Создание сложных таблиц PDF с объединёнными ячейками и повторяющимися столбцами

Создайте продвинутую таблицу в PDF с помощью Python и Aspose.PDF. Она включает объединённые ячейки заголовка, цветные фоны, повторяющиеся столбцы и большой структурированный набор данных. Таблица настроена для обработки вертикального разрыва и сложных макетов в документах в стиле отчётов.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_table_hide_borders(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(outfile)
```

![Границы, отступы и заполнение](set-border-style-margins-and-padding-of-table_1.png)

### Оформление углов таблицы

Aspose.PDF for Python via .NET показывает, как применить скруглённые углы к таблице и настроить радиус границы.

1. Создайте новый экземпляр таблицы.
1. Инициализировать границу со всех сторон.
1. Установите радиус скругления.
1. Применить стиль со скруглёнными углами.
1. Добавить строки и ячейки.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table_with_round_corner(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## Добавление содержимого в таблицы

### Использование HTML-фрагментов в ячейках

В этом примере показывается, как вставить контент в формате HTML в ячейки таблицы.

1. Определить границы таблицы и ячеек.
1. Добавить HTML‑контент.
1. Добавить строки. Цикл добавляет несколько строк с HTML-форматированным содержимым в каждой ячейке.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_html_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <span style='color:red'>({row_count}, 2)</span>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

### Использование фрагментов LaTeX в ячейках

В этом примере показано, как вставлять содержимое, отформатированное в LaTeX, в ячейки таблицы для математических или стилизованных выражений.

1. Определить границы таблицы и ячеек.
1. Добавить LaTeX контент.
1. Добавить строки. Цикл добавляет несколько строк с контентом, отформатированным в LaTeX, в каждой ячейке.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_latex_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$"))

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\underline{{({row_count}, 3)}}$")
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## Расширенные возможности таблиц

### Вставить автоматические разрывы страниц в таблице PDF

Создайте большую таблицу в PDF, используя Python и Aspose.PDF, с автоматическими разрывами страниц после определённого количества строк. Он формирует многострочную таблицу, применяет границы и принудительно размещает выбранные строки на новой странице для лучшего контроля макета.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def insert_page_break(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create table instance
    table = ap.Table()

    # Set border style for table
    table.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Set default border style for table with border color as Red
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Specify table columns width
    table.column_widths = "100 100"

    # Create a loop to add 200 rows for table
    for counter in range(201):
        row = ap.Row()
        table.rows.add(row)

        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 0"))
        row.cells.add(cell1)

        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 1"))
        row.cells.add(cell2)

        # When 10 rows are added, render new row in new page
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True

    # Add table to paragraphs collection of PDF file
    page.paragraphs.add(table)

    # Save PDF document
    document.save(outfile)
```

### Повторяющиеся строки заголовка на нескольких страницах

Этот пример показывает, как создать таблицу, которая охватывает несколько страниц, при этом строки заголовка остаются видимыми на каждой странице.

1. Инициализировать таблицу.
1. Повторять строки заголовка, включая шрифт, размер и цвет.
1. Установите ширину столбцов и примените границы к таблице.
1. Добавить строки заголовка.
1. Добавьте много строк данных, чтобы таблица растянулась на несколько страниц.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_rows(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style = text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(outfile)
```

### Повторяющиеся столбцы

Функция ‘add_repeating_columns’ создаёт PDF‑документ с таблицей, в которой повторяются столбцы. Она настраивает ограниченную рамкой таблицу, добавляет заголовки, заполняет строки данными и сохраняет сгенерированный PDF‑файл в указанное место. Установка этого свойства заставит таблицу переходить на следующую страницу столбцами и повторять указанное количество столбцов в начале следующей страницы.

1. Инициализирует новый PDF‑документ.
1. Добавляет страницу с пользовательскими размерами.
1. Установить стиль границы таблицы.
1. Инициализировать таблицу.
1. Добавьте таблицу на страницу PDF.
1. Добавить строку заголовка.
1. Добавить строки данных.
1. Сохранить PDF‑документ.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_columns(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.a5.height, ap.PageSize.a5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(outfile)
```

### Создать таблицу PDF с ячейками, содержащими повернутый текст

Создайте таблицу в PDF с помощью Python и Aspose.PDF, где текст в каждой ячейке повёрнут под разными углами. Это полезно для вертикальных заголовков, креативных макетов, компактных таблиц и пользовательского форматирования отчётов.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def rotated_text_table(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)

    # Add 1st row to table
    row1 = table.rows.add()
    row1.min_row_height = 200

    for cell_count in range(4):
        # Add table cells
        cell = row1.cells.add()

        tf = ap.text.TextFragment(f"Cell 1 {cell_count - 1}")
        tf.text_state.rotation = 90 * cell_count
        tf.horizontal_alignment = HorizontalAlignment.CENTER

        cell.paragraphs.add(tf)

    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save result
    document.save(outfile)
```

## Связанные темы таблицы

- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Извлекать таблицы из PDF‑документов](/pdf/ru/python-net/extracting-table/)
- [Интегрировать таблицы PDF с источниками данных](/pdf/ru/python-net/integrate-table/)
- [Манипулировать таблицами в существующих PDF](/pdf/ru/python-net/manipulating-tables/)
