---
title: Agregar tablas a PDF usando Python
linktitle: Agregar tablas
type: docs
weight: 10
url: /es/python-net/adding-tables/
description: Aspose.PDF for Python vía .NET es una biblioteca utilizada para crear, leer y editar tablas PDF. Consulte otras funciones avanzadas en este tema.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar una tabla en PDF usando Python
Abstract: Este artículo ofrece una guía completa para crear y manipular tablas en documentos PDF utilizando la biblioteca Aspose.PDF for Python vía .NET. Detalla los pasos para agregar tablas a archivos PDF existentes, incluyendo la configuración de bordes de tabla, márgenes y relleno. Además, explora funcionalidades avanzadas como la unión de columnas y filas usando `col_span` y `row_span`, la aplicación de diferentes configuraciones AutoFit y la obtención dinámica del ancho de la tabla. El artículo también muestra cómo insertar imágenes SVG en celdas de tabla y cómo forzar saltos de página o renderizar tablas en nuevas páginas. Los fragmentos de código ilustran cada funcionalidad, demostrando cómo gestionar eficazmente el diseño y el contenido de tablas en documentos PDF.
---

Agregar tablas a documentos PDF existentes es una necesidad común para mejorar la presentación de datos, estructurar información o generar informes. **Aspose.PDF for Python via .NET** ofrece una solución completa para esta tarea, permitiendo a los desarrolladores insertar tablas en PDF existentes sin problemas.

Esta guía ofrece un enfoque paso a paso para agregar tablas a documentos PDF existentes usando Aspose.PDF for Python vía .NET. Cubre la inicialización de una tabla, la configuración de anchos de columna, la definición de bordes, la población de filas y celdas, y el guardado del documento modificado. Además, la guía explora características avanzadas, como el manejo de bordes de celda, la aplicación de márgenes y relleno, y el uso de configuraciones AutoFit para ajustar dinámicamente las dimensiones de la tabla.

Ya sea que busque mejorar el atractivo visual de sus PDFs o organizar los datos de manera más efectiva, esta guía sirve como un recurso valioso para aprovechar las potentes capacidades de manipulación de tablas de Aspose.PDF for Python.

## Creando tablas básicas

## Creando tabla

Este ejemplo demuestra cómo crear una tabla en un documento PDF con bordes y múltiples filas.

1. Crear un nuevo documento PDF.
1. Añadir una página en blanco al documento.
1. Inicializar la tabla.
1. Establecer el borde general de la tabla.
1. Establecer el borde para celdas individuales.
1. Añadir filas y celdas.
1. Insertar la tabla en la página.
1. Guardar el PDF en la ruta especificada.

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

### Añadiendo imágenes a celdas de tabla

Este fragmento de código muestra cómo insertar imágenes en celdas de tabla en un documento PDF.

1. Crear un nuevo documento PDF.
1. Inicializar la tabla.
1. Establecer anchos de columna en puntos.
1. Se agrega un fragmento de texto a la primera celda.
1. Se añade una instancia de 'ap.Image()' a la segunda celda.
1. Establecer la ruta al archivo de imagen con 'img.file'.
1. Los parámetros 'img.fix_width' y 'img.fix_height' controlan el tamaño de la imagen dentro de la celda.
1. Insertar la tabla en la página PDF.
1. Guardar el PDF.

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

Puede agregar imágenes SVG en celdas de tabla en un documento PDF:

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

### ColSpan y RowSpan en tablas

Este ejemplo muestra cómo combinar celdas de tabla vertical y horizontalmente para crear diseños de tabla complejos.

1. Establecer el borde general de la tabla.
1. Establecer los bordes predeterminados de las celdas.
1. Combinar dos celdas horizontalmente en una.
1. Combinar la celda verticalmente a través de dos filas.
1. La fila 5 tiene en cuenta el rowspan omitiendo la columna combinada.
1. Insertar la tabla en la página.
1. Guardar el PDF.

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

![Demostración de ColSpan y RowSpan](colspan_rowspan.png)

### Aplicando bordes a tablas y celdas

Este ejemplo muestra cómo establecer el relleno de celdas, los márgenes de la tabla y controlar el ajuste de línea para el texto en las celdas de la tabla.

1. Establecer el ancho de las columnas.
1. Definir los bordes de la tabla y de las celdas.
1. Establecer el relleno dentro de las celdas para un espaciado consistente.
1. Aplicar el relleno a todas las celdas por defecto.
1. Añadir texto y controlar el ajuste.
1. Añadir filas y celdas.
1. Guardar el PDF.

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

![Márgenes y bordes en tabla PDF](margin-border.png)

## Diseño y tamaño de la tabla

### Ajuste automático de columnas y filas

Este fragmento de código muestra cómo ajustar automáticamente el ancho de las columnas de la tabla para que se adapten a la página.
Tenga en cuenta que en el parámetro table.column_widths = "50 50 50" - son puntos. Pero también puede especificar centímetros (cm), pulgadas o %.

1. Establecer los anchos iniciales de las columnas.
1. Ajusta automáticamente las columnas para que encajen en el ancho de la página.
1. Definir los bordes de las celdas y de la tabla.
1. El 'table.default_cell_padding' utiliza 'MarginInfo()' para un espaciado consistente dentro de las celdas.
1. Añadir filas con 'table.rows.add()', y añadir celdas con 'row.cells.add()'.
1. Guardar el PDF.

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

### Ajustar el espaciado alrededor del contenido

Este ejemplo muestra cómo crear tablas que abarcan varias páginas, manejar textos largos en las celdas y aplicar relleno y bordes.

1. Añadir una nueva tabla a la página usando 'page.paragraphs.add(table)'.
1. Definir los anchos de las columnas con 'table.column_widths'.
1. Establece bordes individuales de celdas con 'table.default_cell_border'.
1. Establecer el borde general de la tabla con 'table.border'.
1. Definir el relleno predeterminado para las celdas usando 'MarginInfo()'.
1. Añadir texto usando 'TextFragment'.
1. Añadir otra fila.
1. Guardar el PDF.

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

![Bordes, márgenes y relleno](set-border-style-margins-and-padding-of-table_1.png)

### Estilizar esquinas de la tabla

Aspose.PDF for Python via .NET muestra cómo aplicar esquinas redondeadas a una tabla y personalizar el radio del borde.

1. Crear una nueva instancia de tabla.
1. Inicializar un borde para todos los lados.
1. Establecer el radio de la esquina.
1. Aplicar el estilo de esquina redondeada.
1. Añadir filas y celdas.
1. Insertar la tabla en la página PDF con 'page.paragraphs.add(table)'.
1. Guardar el documento PDF.

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

## Añadiendo contenido a tablas

### Usar fragmentos HTML en celdas

Este ejemplo muestra cómo insertar contenido con formato HTML en celdas de tabla.

1. Definir los bordes de la tabla y de las celdas.
1. Añadir contenido HTML.
1. Añadir filas. Un bucle agrega múltiples filas con contenido HTML en cada celda.
1. Insertar la tabla en la página PDF con 'page.paragraphs.add(table)'.
1. Guardar el documento PDF.

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

### Usar fragmentos LaTeX en celdas

Este ejemplo muestra cómo insertar contenido con formato LaTeX en celdas de tabla para expresiones matemáticas o estilizadas.

1. Definir los bordes de la tabla y de las celdas.
1. Añadir contenido LaTeX.
1. Añadir filas. Un bucle agrega múltiples filas con contenido formateado en LaTeX en cada celda.
1. Insertar la tabla en la página PDF con 'page.paragraphs.add(table)'.
1. Guardar el documento PDF.

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

## Funciones avanzadas de tabla

### Insertar tablas a través de páginas

Este ejemplo muestra cómo crear múltiples tablas en un PDF, establecer los márgenes de página y forzar que una tabla comience en una nueva página.

1. Establecer los márgenes de página usando 'page_info.margin'.
1. Establecer la orientación de la página a horizontal 'page_info.is_landscape'.
1. Primera tabla:
- definir dos columnas con anchos especificados.
- agregar las filas en un bucle con 'row.fixed_row_height'.
- llenar celdas con fragmentos de texto.
1. Segunda tabla:
- crear una nueva tabla con 'table1.column_widths'.
- forzar que la tabla comience en una nueva página.
1. Añadir la primera tabla.
1. Añadir la segunda tabla en una nueva página.
1. Guardar el documento

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

### Crear tablas sin bordes

Este ejemplo muestra cómo crear una tabla grande que puede dividirse verticalmente a través de páginas, repetir columnas y aplicar diferentes colores de fondo a las celdas de encabezado.

1. Inicializar la tabla.
1. Establecer un borde predeterminado para todas las celdas.
1. Las celdas de encabezado usan 'col_span' para combinar múltiples columnas.
1. Establecer el fondo de la celda para una mejor distinción visual con 'background_color set'
1. Añadir filas.
1. Insertar la tabla en la página PDF con 'page.paragraphs.add(table)'.
1. Guardar el documento PDF.

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

### Repetir filas de encabezado en múltiples páginas

Este ejemplo muestra cómo crear una tabla que abarca varias páginas manteniendo las filas de encabezado visibles en cada página.

1. Inicializar la tabla.
1. Repetir filas de encabezado incluyendo fuente, tamaño y color.
1. Establecer anchos de columna y aplicar bordes a la tabla.
1. Añadir filas de encabezado.
1. Añadir muchas filas de datos para forzar la tabla a través de múltiples páginas.
1. Insertar la tabla en la página PDF con 'page.paragraphs.add(table)'.
1. Guardar el documento PDF.

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

### Repetir columnas

La función 'add_repeating_columns' crea un documento PDF con una tabla que tiene columnas repetidas. Configura una tabla con bordes, agrega encabezados, llena filas de datos y guarda el archivo PDF generado en la ubicación especificada. Establecer esta propiedad hará que la tabla se divida a la siguiente página por columnas y repita la cantidad de columnas dadas al inicio de la siguiente página.

1. Inicializa un nuevo documento PDF.
1. Añade una página con dimensiones personalizadas.
1. Establecer el estilo del borde de la tabla.
1. Inicializar tabla.
1. Añadir tabla a la página PDF.
1. Añadir fila de encabezado.
1. Añadir filas de datos.
1. Guardar documento PDF.

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
