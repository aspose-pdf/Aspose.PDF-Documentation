---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 30
url: /es/python-net/complex-pdf-example/
description: Aspose.PDF para Python a través de .NET le permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un PDF complejo usando Python
Abstract: Este artículo amplía el proceso básico de creación de PDF demostrado en el ejemplo "Hello, World" al ilustrar cómo crear un documento PDF más complejo usando Python y Aspose.PDF. El documento de ejemplo se desarrolla para una empresa ficticia de servicios de ferris de pasajeros e incluye una imagen, dos fragmentos de texto (un encabezado y un párrafo) y una tabla. El proceso implica varios pasos instanciar un objeto `Document` para crear un PDF vacío, agregar una `Page` y luego insertar una `Image` en la página. Se crea un `TextFragment` para el encabezado usando la fuente Arial con tamaño de 24 pt y alineación centrada, que luego se agrega a los párrafos de la página. Se agrega un segundo `TextFragment` para la descripción, usando la fuente Times New Roman con tamaño de 14 pt y alineación a la izquierda. A continuación, se crea y formatea una tabla con anchuras de columna específicas, bordes y relleno. La tabla incluye una fila de encabezado con celdas resaltadas y múltiples filas de datos generadas mediante iteración
---

El ejemplo [Hello, World](/pdf/python-net/hello-world-example/) mostró pasos simples para crear un documento PDF usando Python y Aspose.PDF. En este artículo, veremos cómo crear un documento más complejo con Aspose.PDF para Python. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferris de pasajeros. Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo) y una tabla.

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Añadir una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al objeto documento. Así, ahora nuestro documento tendrá una página.
1. Añadir una [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) a la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño 24 pt y alineación centrada.
1. Añadir el encabezado a los [párrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para la descripción. Para la descripción usaremos la fuente Arial con tamaño 24 pt y alineación centrada.
1. Añadir (descripción) a los párrafos de la página.
1. Crear y dar estilo a la tabla. Establecer ancho de columna, bordes, relleno y fuente.
1. Añadir (tabla) a los [párrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) de la página.
1. Guardar el documento "Complex.pdf".

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
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

    document.save(self.data_dir + "Complex.pdf")
```

