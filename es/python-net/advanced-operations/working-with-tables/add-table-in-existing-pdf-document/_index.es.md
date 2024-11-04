---
title: Crear o Agregar Tabla en PDF usando Python 
linktitle: Crear o Agregar Tabla
type: docs
weight: 10
url: /python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF para Python via .NET es una biblioteca utilizada para crear, leer y editar tablas PDF. Consulta otras funciones avanzadas en este tema.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crear o Agregar Tabla en PDF usando Python ",
    "alternativeHeadline": "Cómo agregar Tabla en PDF con Python via .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, crear tabla en pdf, agregar tabla",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF para Python via .NET es una biblioteca utilizada para crear, leer y editar tablas PDF. Consulta otras funciones avanzadas en este tema."
}
</script>


## Creación de Tabla usando Python

Las tablas son importantes cuando se trabaja con documentos PDF. Proporcionan grandes características para mostrar información de manera sistemática. El espacio de nombres Aspose.PDF contiene clases llamadas [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), y [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) que proporcionan funcionalidad para crear tablas al generar documentos PDF desde cero.

La tabla se puede crear creando un objeto de la Clase Table.

```python

    table = ap.Table()
```

### Añadiendo Tabla en Documento PDF Existente

Para agregar una tabla a un archivo PDF existente con Aspose.PDF para Python a través de .NET, siga los siguientes pasos:

1. Cargue el archivo fuente.
1. Inicialice una tabla y configure sus columnas y filas.
1. Establezca la configuración de la tabla (hemos establecido los bordes).
1. Llene la tabla.
1. Agregue la tabla a una página.
1. Guarde el archivo.

Los siguientes fragmentos de código muestran cómo agregar texto en un archivo PDF existente.

```python

    import aspose.pdf as ap

    # Cargar documento PDF fuente
    doc = ap.Document(input_file)
    # Inicializa una nueva instancia de la Tabla
    table = ap.Table()
    # Establecer el color del borde de la tabla como LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Establecer el borde para las celdas de la tabla
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Crear un bucle para agregar 10 filas
    for row_count in range(0, 10):
        # Agregar fila a la tabla
        row = table.rows.add()
        # Agregar celdas a la tabla
        row.cells.add("Columna (" + str(row_count) + ", 1)")
        row.cells.add("Columna (" + str(row_count) + ", 2)")
        row.cells.add("Columna (" + str(row_count) + ", 3)")
    # Agregar objeto tabla a la primera página del documento de entrada
    doc.pages[1].paragraphs.add(table)
    # Guardar documento actualizado que contiene el objeto tabla
    doc.save(output_file)
```

### ColSpan y RowSpan en Tablas

Aspose.PDF para Python a través de .NET proporciona la propiedad [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) para fusionar las columnas en una tabla y la propiedad [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) para fusionar las filas.


Usamos la propiedad `col_span` o `row_span` en el objeto `Cell` que crea la celda de la tabla. Después de aplicar las propiedades requeridas, la celda creada se puede agregar a la tabla.

```python

    import aspose.pdf as ap

    # Inicializar el objeto Document llamando a su constructor vacío
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Inicializa una nueva instancia de la Tabla
    table = ap.Table()
    # Establecer el color del borde de la tabla como LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Establecer el borde para las celdas de la tabla
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Agregar la 1ra fila a la tabla
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Agregar celdas a la tabla
        row1.cells.add("Test 1" + str(cellCount))

    # Agregar la 2da fila a la tabla
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Agregar la 3ra fila a la tabla
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Agregar la 4ta fila a la tabla
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Agregar la 5ta fila a la tabla
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Agregar el objeto tabla a la primera página del documento de entrada
    pdf_document.pages[1].paragraphs.add(table)
    # Guardar el documento actualizado que contiene el objeto tabla
    pdf_document.save(output_file)
```


El resultado del código de ejecución a continuación es la tabla representada en la siguiente imagen:

![Demostración de ColSpan y RowSpan](colspan_rowspan.png)

## Trabajando con Bordes, Márgenes y Relleno

Por favor, tenga en cuenta que también se admite la función para establecer el estilo de borde, márgenes y relleno de celdas para tablas. Antes de entrar en más detalles técnicos, es importante entender los conceptos de borde, márgenes y relleno que se presentan a continuación en un diagrama:

![Bordes, márgenes y relleno](set-border-style-margins-and-padding-of-table_1.png)

En la figura anterior, puedes ver que los bordes de la tabla, fila y celda se superponen. Usando Aspose.PDF, una tabla puede tener márgenes y las celdas pueden tener relleno. Para establecer márgenes de celda, tenemos que establecer el relleno de celda.

### Bordes

Para establecer los bordes de los objetos [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) y [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), use las propiedades Table.border, Row.border y Cell.border.
 Los bordes de las celdas también se pueden establecer usando la propiedad [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) de la clase [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) o Row. Todas las propiedades relacionadas con los bordes discutidas anteriormente se asignan a una instancia de la clase Row, que se crea llamando a su constructor. La clase Row tiene muchas sobrecargas que toman casi todos los parámetros necesarios para personalizar el borde.

### Márgenes o Relleno

El relleno de las celdas se puede gestionar utilizando la propiedad [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) de la clase Table. Todas las propiedades relacionadas con el relleno se asignan a una instancia de la clase [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) que toma información sobre los parámetros `left`, `right`, `top` y `bottom` para crear márgenes personalizados.
En el siguiente ejemplo, el ancho del borde de la celda se establece en 0.1 puntos, el ancho del borde de la tabla se establece en 1 punto y el relleno de la celda se establece en 5 puntos.

![Margen y Borde en Tabla PDF](margin-border.png)

```python

    import aspose.pdf as ap

    # Instanciar el objeto Document llamando a su constructor vacío
    doc = ap.Document()
    page = doc.pages.add()
    # Instanciar un objeto de tabla
    tab1 = ap.Table()
    # Agregar la tabla en la colección de párrafos de la sección deseada
    page.paragraphs.add(tab1)
    # Establecer los anchos de columna de la tabla
    tab1.column_widths = "50 50 50"
    # Establecer el borde de celda predeterminado usando el objeto BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Crear un objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Establecer el relleno de celda predeterminado en el objeto MarginInfo
    tab1.default_cell_padding = margin
    # Crear filas en la tabla y luego celdas en las filas
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 con una larga cadena de texto")
    # Row1.Cells.Add("col3 con una larga cadena de texto para ser colocado dentro de la celda")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Guardar el Pdf
    doc.save(output_file)
```


Para crear una tabla con esquinas redondeadas, utiliza el valor [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) de la [clase BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) y establece el estilo de las esquinas de la tabla a redondeado.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # Crear un objeto BorderInfo en blanco
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # Establecer el borde como un borde redondeado donde el radio del redondeo es 15
    b_info.rounded_border_radius = 15
    # Establecer el estilo de esquina de la tabla como Redondeado
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # Establecer la información del borde de la tabla
    tab1.border = b_info
```

## Aplicar Diferentes Configuraciones de AutoAjuste a una Tabla

Al diseñar una tabla utilizando una herramienta visual como Microsoft Word, frecuentemente utilizarás una de las características de AutoAjuste para ajustar convenientemente el tamaño de la tabla al ancho deseado.
 Por ejemplo, puedes emplear la opción "AUTO_FIT_TO_WINDOW" para ajustar el ancho de la tabla a la página o AUTO_FIT_TO_CONTENT. Por defecto, al usar Aspose.Pdf para crear una nueva tabla, utiliza el [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) con un valor "Customized". En el siguiente fragmento de código, establecemos los parámetros del objeto [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) y los objetos [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) en la tabla. Prueba el ejemplo y evalúa el resultado.

```python

    import aspose.pdf as ap

    # Instanciar el objeto Pdf llamando a su constructor vacío
    doc = ap.Document()
    # Crear la sección en el objeto Pdf
    sec1 = doc.pages.add()
    # Instanciar un objeto de tabla
    tab1 = ap.Table()
    # Agregar la tabla en la colección de párrafos de la sección deseada
    sec1.paragraphs.add(tab1)
    # Establecer anchos de columna de la tabla
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # Establecer el borde de celda predeterminado usando el objeto BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Crear un objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Establecer el relleno de celda predeterminado al objeto MarginInfo
    tab1.default_cell_padding = margin
    # Crear filas en la tabla y luego celdas en las filas
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Guardar el documento actualizado que contiene el objeto tabla
    doc.save(output_file)
```

### Obtener Ancho de la Tabla

A veces, es necesario obtener el ancho de la tabla dinámicamente. La clase Aspose.PDF.Table tiene un método [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) para este propósito. Por ejemplo, no has establecido el ancho de las columnas de la tabla explícitamente y has configurado [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) a 'AUTO_FIT_TO_CONTENT'. En este caso, puedes obtener el ancho de la tabla de la siguiente manera.

```python

    import aspose.pdf as ap

    # Crear un nuevo documento
    doc = ap.Document()
    # Agregar página en el documento
    page = doc.pages.add()
    # Inicializar nueva tabla
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Agregar fila en la tabla
    row = table.rows.add()
    # Agregar celda en la tabla
    cell = row.cells.add("Texto de la Celda 1")
    cell = row.cells.add("Texto de la Celda 2")
    # Obtener ancho de la tabla
    print(table.get_width())
```

## Agregar Imagen SVG a la Celda de la Tabla

Aspose.PDF para Python a través de .NET proporciona la capacidad de insertar celdas de tabla en un archivo PDF.
 Al construir una tabla, puede incluir tanto texto como imágenes dentro de estas celdas. Además, la API ofrece la funcionalidad de transformar archivos SVG en formato PDF. Al aprovechar estas funcionalidades juntas, puede cargar una imagen SVG y colocarla dentro de una celda de la tabla.

El siguiente fragmento de código demuestra el proceso de crear un objeto de tabla e incrustar una imagen SVG dentro de una de sus celdas.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    doc = ap.Document()
    # Crear una instancia de imagen
    img = ap.Image()
    # Establecer tipo de imagen como SVG
    img.file_type = ap.ImageFileType.SVG
    # Ruta para el archivo fuente
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # Establecer ancho para la instancia de imagen
    img.fix_width = 50
    # Establecer altura para la instancia de imagen
    img.fix_height = 50
    # Crear instancia de tabla
    table = ap.Table()
    # Establecer ancho para las celdas de la tabla
    table.column_widths = "100 100"
    # Crear objeto fila y añadirlo a la instancia de tabla
    row = table.rows.add()
    # Crear objeto celda y añadirlo a la instancia de fila
    cell = row.cells.add()
    # Añadir fragmento de texto a la colección de párrafos del objeto celda
    cell.paragraphs.add(ap.text.TextFragment("Primera celda"))
    # Añadir otra celda al objeto fila
    cell = row.cells.add()
    # Añadir imagen SVG a la colección de párrafos de la instancia de celda recientemente añadida
    cell.paragraphs.add(img)
    # Crear objeto página y añadirlo a la colección de páginas de la instancia de documento
    page = doc.pages.add()
    # Añadir tabla a la colección de párrafos del objeto página
    page.paragraphs.add(table)
    # Guardar archivo PDF
    doc.save(output_file)
```

## Insertar un salto de página entre las filas de la tabla

Por defecto, cuando creas una tabla dentro de un archivo PDF, la tabla se extenderá a través de múltiples páginas si se extiende más allá del margen inferior de la tabla. Sin embargo, hay situaciones en las que necesitamos forzar saltos de página después de que un número específico de filas se haya agregado a la tabla. El siguiente fragmento de código describe el proceso de insertar un salto de página cuando se han incluido 10 filas en la tabla.

```python

    import aspose.pdf as ap

    # Instanciar la instancia del documento
    doc = ap.Document()
    # Añadir página a la colección de páginas del archivo PDF
    doc.pages.add()
    # Crear instancia de tabla
    tab = ap.Table()
    # Establecer estilo de borde para la tabla
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Establecer estilo de borde predeterminado para la tabla con color de borde rojo
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Especificar el ancho de las columnas de la tabla
    tab.column_widths = "100 100"
    # Crear un bucle para añadir 200 filas a la tabla
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # Cuando se añaden 10 filas, renderizar nueva fila en nueva página
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # Añadir tabla a la colección de párrafos del archivo PDF
    doc.pages[1].paragraphs.add(tab)
    # Guardar el documento PDF
    doc.save(output_file)
```


## Representar una Tabla en una Nueva Página

Por defecto, los párrafos se añaden a la colección de Párrafos de un objeto Página. Sin embargo, es posible representar una tabla en una nueva página en lugar de directamente después del objeto de nivel de párrafo añadido anteriormente en la página.

### Ejemplo: Cómo Representar una Tabla en una Nueva Página usando Python

Para representar una tabla en una nueva página, use la propiedad [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) en la clase [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). El siguiente fragmento de código muestra cómo hacerlo.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # Página añadida.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Contenido 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # Quiero mantener la tabla 1 en la siguiente página por favor...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python a través de la Biblioteca .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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