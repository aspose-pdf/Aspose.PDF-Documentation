---
title: Manipular Tablas en PDF existente
linktitle: Manipular Tablas
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Tablas en PDF existente",
    "alternativeHeadline": "Cómo actualizar el contenido de Tablas en PDF existente",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, manipular tablas",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## Manipular tablas en un PDF existente

Una de las primeras características soportadas por Aspose.PDF para Python a través de .NET es su capacidad de trabajar con tablas y proporciona un gran soporte para agregar tablas en archivos PDF que se generan desde cero o en cualquier archivo PDF existente. En esta nueva versión, hemos implementado una nueva función de búsqueda y análisis de tablas simples que ya existen en la página de un documento PDF. Una nueva clase llamada [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) proporciona estas capacidades. El uso de TableAbsorber es muy similar a la clase existente [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/). El siguiente fragmento de código muestra los pasos para actualizar contenidos en una celda de tabla en particular.

```python

    import aspose.pdf as ap

    # Cargar archivo PDF existente
    pdf_document = ap.Document(input_file)
    # Crear objeto TableAbsorber para encontrar tablas
    absorber = ap.text.TableAbsorber()
    # Visitar la primera página con el absorber
    absorber.visit(pdf_document.pages[1])
    # Obtener acceso a la primera tabla en la página, su primera celda y fragmentos de texto en ella
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Cambiar el texto del primer fragmento de texto en la celda
    fragment.text = "hola mundo"
    pdf_document.save(output_file)
```


## Reemplazar la tabla antigua con una nueva en un documento PDF

En caso de que necesites encontrar una tabla en particular y reemplazarla con la deseada, puedes usar el método [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) de la clase [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para hacerlo. El siguiente ejemplo demuestra la funcionalidad para reemplazar la tabla dentro de un documento PDF:

```python

    import aspose.pdf as ap

    # Cargar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Crear objeto TableAbsorber para encontrar tablas
    absorber = ap.text.TableAbsorber()
    # Visitar la primera página con el absorber
    absorber.visit(pdf_document.pages[1])
    # Obtener la primera tabla en la página
    table = absorber.table_list[0]
    # Crear nueva tabla
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # Reemplazar la tabla con la nueva
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Guardar documento
    pdf_document.save(output_file)
```


## Cómo determinar si la tabla se romperá en la página actual

Este código genera un documento PDF que contiene una tabla, calcula el espacio disponible en la página y verifica si agregar más filas a la tabla provocará un salto de página basado en las restricciones de espacio. El resultado se guarda en un archivo de salida.

```python

    import aspose.pdf as ap

    # Instanciar un objeto de la clase PDF
    pdf = ap.Document()
    # Agregar la sección a la colección de secciones del documento PDF
    page = pdf.pages.add()
    # Instanciar un objeto de tabla
    table1 = ap.Table()
    table1.margin.top = 300
    # Agregar la tabla en la colección de párrafos de la sección deseada
    page.paragraphs.add(table1)
    # Establecer los anchos de columna de la tabla
    table1.column_widths = "100 100 100"
    # Establecer el borde de celda predeterminado usando el objeto BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Crear objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Establecer el relleno de celda predeterminado en el objeto MarginInfo
    table1.default_cell_padding = margin
    # Si incrementas el contador a 17, la tabla se romperá
    # Porque no puede ser acomodada más en esta página
    for row_counter in range(0, 17):
        # Crear filas en la tabla y luego celdas en las filas
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Obtener la información de altura de la página
    page_height = pdf.page_info.height
    # Obtener la información de altura total del margen superior e inferior de la página,
    # margen superior de la tabla y altura de la tabla.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Mostrar información de altura de la página, altura de la tabla, margen superior de la tabla y
    # información del margen superior e inferior de la página
    print("Altura del documento PDF = " + str(pdf.page_info.height) + "\nInformación del margen superior = " + str(page.page_info.margin.top)
          + "\nInformación del margen inferior = " + str(page.page_info.margin.bottom) + "\n\nInformación del margen superior de la tabla = "
          + str(table1.margin.top) + "\nAltura promedio de fila = " + str(table1.rows[0].min_row_height) + " \nAltura de la tabla "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nAltura total de la página ="
          + str(page_height) + "\nAltura acumulada incluyendo la tabla =" + str(total_objects_height))
    # Verificar si al restar la suma del margen superior de la página + margen inferior de la página
    # + margen superior de la tabla y altura de la tabla de la altura de la página es menor
    # A 10 (una fila promedio puede ser mayor a 10)
    if (page_height - total_objects_height) <= 10:
        # Si el valor es menor a 10, entonces mostrar el mensaje.
        # Que muestra que no se puede colocar otra fila y si agregamos una nueva
        # Fila, la tabla se romperá. Depende del valor de la altura de la fila.
        print("Altura de la página - Altura de los objetos < 10, por lo que la tabla se romperá")
    # Guardar el documento PDF
    pdf.save(output_file)
```


## Añadir Columna Repetida en la Tabla

En la clase [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), puede establecer un [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) que repetirá filas si la tabla es demasiado larga verticalmente y se desborda a la siguiente página. Sin embargo, en algunos casos, las tablas son demasiado anchas para caber en una sola página y necesitan continuar en la siguiente página. Para cumplir con el propósito, hemos implementado la propiedad [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) en la clase [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). Establecer esta propiedad hará que la tabla se divida a la siguiente página en columnas y repita el número de columnas dado al inicio de la siguiente página. El siguiente fragmento de código muestra el uso de la propiedad [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties):

```python

    import aspose.pdf as ap

    # Crear un nuevo documento
    doc = ap.Document()
    page = doc.pages.add()
    # Instanciar una tabla externa que ocupa toda la página
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Instanciar un objeto de tabla que se anidará dentro de outerTable que se romperá dentro de la misma página
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Agregar outerTable a los párrafos de la página
    # Agregar mi tabla a outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Agregar fila de encabezado
    row = my_table.rows.add()
    row.cells.add("encabezado 1")
    row.cells.add("encabezado 2")
    row.cells.add("encabezado 3")
    row.cells.add("encabezado 4")
    row.cells.add("encabezado 5")
    row.cells.add("encabezado 6")
    row.cells.add("encabezado 7")
    row.cells.add("encabezado 11")
    row.cells.add("encabezado 12")
    row.cells.add("encabezado 13")
    row.cells.add("encabezado 14")
    row.cells.add("encabezado 15")
    row.cells.add("encabezado 16")
    row.cells.add("encabezado 17")
    for row_counter in range(0, 6):
        # Crear filas en la tabla y luego celdas en las filas
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python a través de .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python a través de .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>