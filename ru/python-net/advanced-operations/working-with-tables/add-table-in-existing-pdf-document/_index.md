---
title: Добавление таблиц в PDF с помощью Python
linktitle: Добавление таблиц
type: docs
weight: 10
url: /ru/python-net/adding-tables/
description: Aspose.PDF for Python via .NET — это библиотека, используемая для создания, чтения и редактирования таблиц PDF. Ознакомьтесь с другими продвинутыми функциями в этой теме.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить таблицу в PDF с помощью Python
Abstract: В этой статье предоставлено всестороннее руководство по созданию и манипулированию таблицами в PDF‑документах с использованием библиотеки Aspose.PDF for Python via .NET. Описаны шаги по добавлению таблиц в существующие PDF‑файлы, включая настройку границ таблицы, отступов и внутреннего поля. Кроме того, рассматриваются расширенные возможности, такие как объединение столбцов и строк с помощью `col_span` и `row_span`, применение различных настроек AutoFit и динамическое получение ширины таблицы. В статье также демонстрируется вставка SVG‑изображений в ячейки таблицы и принудительное разбиение страниц или вывод таблиц на новых страницах. Фрагменты кода иллюстрируют каждую возможность, показывая, как эффективно управлять макетом и содержимым таблиц в PDF‑документах.
---

Добавление таблиц в существующие PDF‑документы — это распространённая необходимость для улучшения представления данных, структурирования информации или создания отчётов. **Aspose.PDF for Python via .NET** предлагает всестороннее решение этой задачи, позволяя разработчикам без проблем вставлять таблицы в существующие PDF.

Это руководство предоставляет пошаговый подход к добавлению таблиц в существующие PDF‑документы с использованием Aspose.PDF for Python via .NET. Оно охватывает инициализацию таблицы, настройку ширины столбцов, определение границ, заполнение строк и ячеек, а также сохранение изменённого документа. Кроме того, руководство исследует продвинутые функции, такие как управление границами ячеек, применение отступов и внутреннего поля, а также использование настроек AutoFit для динамической настройки размеров таблицы.

Если вы хотите улучшить визуальную привлекательность ваших PDF‑файлов или более эффективно организовать данные, это руководство будет ценным ресурсом для использования мощных возможностей манипуляции таблицами в Aspose.PDF for Python.

## Создание базовых таблиц

## Создание таблицы

Этот пример демонстрирует, как создать таблицу в PDF‑документе с границами и несколькими строками.

1. Создайте новый PDF‑документ.
1. Добавляет пустую страницу в документ.
1. Инициализируйте таблицу.
1. Установите общую границу таблицы.
1. Установите границы для отдельных ячеек.
1. Добавьте строки и ячейки.
1. Вставьте таблицу на страницу.
1. Сохраните PDF по указанному пути.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 5, ap.Color.light_gray
    )
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
    document.save(path_outfile)
```

### Добавление изображений в ячейки таблицы

Этот фрагмент кода показывает, как вставлять изображения в ячейки таблицы в PDF‑документе.

1. Создайте новый PDF‑документ.
1. Инициализируйте таблицу.
1. Установите ширину столбцов в пунктах.
1. Текстовый фрагмент добавлен в первую ячейку.
1. Экземпляр 'ap.Image()' добавлен во вторую ячейку.
1. Установите путь к файлу изображения с помощью 'img.file'.
1. Параметры 'img.fix_width' и 'img.fix_height' управляют размером изображения внутри ячейки.
1. Вставьте таблицу на страницу PDF.
1. Сохраните PDF.

```python

    import aspose.pdf as ap
    from os import path

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
    img.file = path.join(self.data_dir, image)
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
    document.save(path_outfile)
```

Вы можете добавить SVG‑изображения в ячейки таблицы в PDF‑документе:

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

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
        img.file = path.join(self.data_dir, image)
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
    document.save(path_outfile)
```

### ColSpan и RowSpan в таблицах

Этот пример показывает, как объединять ячейки таблицы вертикально и горизонтально для создания сложных макетов таблиц.

1. Установите общую границу таблицы.
1. Установите границы ячеек по умолчанию.
1. Объедините две ячейки горизонтально в одну.
1. Объедините ячейку вертикально через две строки.
1. Строка 5 учитывает rowspan, пропуская объединённый столбец.
1. Вставьте таблицу на страницу.
1. Сохраните PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.black
    )
    # Add 1st row to table
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cellCount))

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
    document.save(path_outfile)
```

![Демонстрация ColSpan и RowSpan](colspan_rowspan.png)

### Применение границ к таблицам и ячейкам

Этот пример показывает, как установить отступы ячеек, поля таблицы и управлять переносом слов для текста в ячейках таблицы.

1. Установите ширину столбцов.
1. Определите границы таблицы и ячеек.
1. Установите отступы внутри ячеек для постоянного расстояния.
1. Примените отступы ко всем ячейкам по умолчанию.
1. Добавьте текст и управление переносом.
1. Добавьте строки и ячейки.
1. Сохраните PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)
    # Load source PDF document
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
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(path_outfile)
```

![Отступ и граница в таблице PDF](margin-border.png)

## Макет и размер таблицы

### Автоподгонка столбцов и строк

Этот фрагмент кода показывает, как автоматически регулировать ширину столбцов таблицы, чтобы они помещались на страницу.
Обратите внимание, что в параметре table.column_widths = "50 50 50" — это пункты. Но также можно указывать сантиметры (cm), дюймы или %.

1. Установите первоначальную ширину столбцов.
1. Автоматически подгоняет столбцы к ширине страницы.
1. Определите границы ячеек и таблицы.
1. Свойство 'table.default_cell_padding' использует 'MarginInfo()' для постоянного расстояния внутри ячеек.
1. Добавьте строки с помощью 'table.rows.add()', и добавьте ячейки с помощью 'row.cells.add()'.
1. Сохраните PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
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

    document.save(path_outfile)
```

### Регулировка отступов вокруг содержимого

Этот пример показывает, как создавать таблицы, охватывающие несколько страниц, обрабатывать длинный текст в ячейках и применять отступы и границы.

1. Добавьте новую таблицу на страницу, используя 'page.paragraphs.add(table)'.
1. Определите ширину столбцов с помощью 'table.column_widths'.
1. Устанавливает отдельные границы ячеек с помощью 'table.default_cell_border'.
1. Устанавливает общую границу таблицы с помощью 'table.border'.
1. Определите отступ по умолчанию для ячеек, используя 'MarginInfo()'.
1. Добавьте текст, используя 'TextFragment'.
1. Добавьте еще одну строку.
1. Сохраните PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    # Add page
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table)

    # Set column widths of the table
    table.column_widths = "50 50 50"

    # Set default cell border using BorderInfo object
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    # Set table border using another customized BorderInfo object
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    # Set the default cell padding to the MarginInfo object
    table.default_cell_padding = margin

    # Create rows and cells
    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()

    # Add a long text fragment into the third cell
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False

    # Add another row
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    # Save PDF document
    document.save(path_outfile)
```

![Границы, поля и отступы](set-border-style-margins-and-padding-of-table_1.png)

### Стилизация углов таблицы

Aspose.PDF for Python via .NET показывает, как применить скругленные углы к таблице и настроить радиус границы.

1. Создайте новый экземпляр таблицы.
1. Инициализируйте границу со всех сторон.
1. Установите радиус угла.
1. Примените стиль скругленных углов.
1. Добавьте строки и ячейки.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохраните документ PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()

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
    document.save(path_outfile)
```

## Добавление содержимого в таблицы

### Использование HTML‑фрагментов в ячейках

Этот пример показывает, как вставлять HTML‑форматированный контент в ячейки таблицы.

1. Определите границы таблицы и ячеек.
1. Добавьте HTML‑контент.
1. Добавьте строки. Цикл добавляет несколько строк с HTML‑форматированным содержимым в каждой ячейке.
1. Вставьте таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохраните документ PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

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
            ap.HtmlFragment(
                f"Column <span style='color:red'>({row_count}, 2)</span>"
            )
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
    document.save(path_outfile)
```

### Использование LaTeX‑фрагментов в ячейках

Этот пример показывает, как вставлять LaTeX‑форматированный контент в ячейки таблицы для математических или стилизованных выражений.

1. Определите границы таблицы и ячеек.
1. Добавить LaTeX‑контент.
1. Добавить строки. Цикл добавляет несколько строк с LaTeX‑форматированным содержимым в каждой ячейке.
1. Вставить таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

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
            ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\underline{{({row_count}, 3)}}$"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## Расширенные возможности таблиц

### Вставка таблиц на несколько страниц

Этот пример показывает, как создать несколько таблиц в PDF, задать поля страницы и принудительно начать таблицу на новой странице.

1. Задать поля страницы с помощью 'page_info.margin'.
1. Установить альбомную ориентацию страницы 'page_info.is_landscape'.
1. Первая таблица:
- определить два столбца с указанными ширинами.
- добавить строки в цикле с помощью 'row.fixed_row_height'.
- заполнить ячейки текстовыми фрагментами.
1. Вторая таблица:
- создать новую таблицу с 'table1.column_widths'.
- принудительно начать таблицу на новой странице.
1. Добавить первую таблицу.
1. Добавить вторую таблицу на новой странице.
1. Сохранить документ

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Set page and margin information
    page_info = document.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37
    page_info.is_landscape = True

    # First table with 120 rows
    table = ap.Table()
    table.column_widths = "50 100"

    cur_page = document.pages.add()

    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 2"))

    cur_page.paragraphs.add(table)

    # Second table with 10 rows
    table1 = ap.Table()
    table1.column_widths = "100 100"

    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 3"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 4"))

    table1.is_in_new_page = True  # Force table to new page
    cur_page.paragraphs.add(table1)

    # Save updated document containing table object
    document.save(path_outfile)
```

### Создание таблиц без границ

Этот пример показывает, как создать большую таблицу, которая может разрываться вертикально по страницам, повторять столбцы и применять разные фоновые цвета к ячейкам заголовка.

1. Инициализировать таблицу.
1. Установить границу по умолчанию для всех ячеек.
1. Ячейки заголовка используют 'col_span' для объединения нескольких столбцов.
1. Задать фон ячеек для лучшего визуального различия с помощью 'background_color set'
1. Добавить строки.
1. Вставить таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

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

    document.save(path_outfile)
```

### Повторяющиеся строки заголовка на нескольких страницах

Этот пример показывает, как создать таблицу, которая охватывает несколько страниц, при этом сохраняет видимыми строки заголовка на каждой странице.

1. Инициализировать таблицу.
1. Повторять строки заголовка, включая шрифт, размер и цвет.
1. Задать ширины столбцов и применить границы к таблице.
1. Добавить строки заголовка.
1. Добавить множество строк данных, чтобы таблица растянулась на несколько страниц.
1. Вставить таблицу на страницу PDF с помощью 'page.paragraphs.add(table)'.
1. Сохранить документ PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

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
    table.repeating_rows_style =  text_state

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
    document.save(path_outfile)
```

### Повторяющиеся столбцы

Функция 'add_repeating_columns' создает PDF‑документ с таблицей, у которой повторяются столбцы. Она настраивает таблицу с границами, добавляет заголовки, заполняет строки данных и сохраняет сгенерированный PDF‑файл в указанное место. Установка этого свойства заставит таблицу разрываться на следующую страницу по столбцам и повторять заданное количество столбцов в начале следующей страницы.

1. Инициализирует новый PDF‑документ.
1. Добавляет страницу с пользовательскими размерами.
1. Задать стиль границы таблицы.
1. Инициализировать таблицу.
1. Добавить таблицу на страницу PDF.
1. Добавить строку заголовка.
1. Добавить строки данных.
1. Сохранить PDF‑документ.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.A5.height, ap.PageSize.A5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
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
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
