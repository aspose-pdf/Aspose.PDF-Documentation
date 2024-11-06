---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 30
url: es/python-net/complex-pdf-example/
description: Aspose.PDF para Python a través de .NET te permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El ejemplo de [Hola, Mundo](/pdf/python-net/hello-world-example/) mostró pasos simples para crear un documento PDF usando Python y Aspose.PDF. En este artículo, echaremos un vistazo a la creación de un documento más complejo con Aspose.PDF para Python. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry de pasajeros. Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo), y una tabla.

Si creamos un documento desde cero, debemos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Añadir una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al objeto documento. Así que, ahora nuestro documento tendrá una página.
1. Añadir una [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) a la Página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Añadir el encabezado a los [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Añadir (descripción) a los Párrafos de la página.
1. Crear una tabla, añadir propiedades de la tabla.

1. Añadir (table) a la página [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Guardar un documento "Complex.pdf".

```python

    import aspose.pdf as ap

    # Inicializar objeto de documento
    document = ap.Document()
    # Añadir página
    page = document.pages.add()

    # Añadir imagen
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Añadir encabezado
    header = ap.text.TextFragment("Nuevas rutas de ferry en otoño 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Añadir descripción
    descriptionText = "Los visitantes deben comprar boletos en línea y los boletos están limitados a 5,000 por día. \
    El servicio de ferry está operando a media capacidad y en un horario reducido. Espere filas."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Añadir tabla
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Sale de la ciudad")
    headerRow.cells.add("Sale de la isla")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(output_pdf)
```