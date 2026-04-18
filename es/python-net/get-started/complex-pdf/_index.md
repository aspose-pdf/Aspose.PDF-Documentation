---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 30
url: /es/python-net/complex-pdf-example/
description: Aprenda cómo crear un diseño de PDF más completo en Python combinando imágenes, texto con estilo y tablas con Aspose.PDF para Python a través de .NET.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree un PDF complejo con Python
Abstract: Este tutorial amplía el flujo de trabajo Hello World creando un diseño de PDF más detallado. El documento de ejemplo incluye una imagen de logotipo, un encabezado, texto descriptivo de párrafo y una tabla con estilo con datos de horarios. Demuestra cómo combinar componentes habituales de creación de PDF en un único script de Python usando Aspose.PDF para Python a través de .NET.
---

El tutorial [Hola, Mundo](/pdf/es/python-net/hello-world-example/) cubre el flujo básico de creación de PDF. Esta guía se basa en esa base y muestra cómo componer un diseño de documento más realista con varios tipos de contenido.

En este ejemplo, crea un PDF para un servicio de ferry de pasajeros ficticio. La salida incluye:

- Una imagen de logotipo
- Un fragmento de texto de título
- Un párrafo descriptivo
- Una tabla con estilo y horarios de salida

Al crear este documento desde cero, siga estos pasos:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregue una [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al documento.
1. Inserte una [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) en la página.
1. Crear un encabezado [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) con fuente y alineación personalizadas.
1. Agregar el encabezado a la página [párrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Crear un segundo [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) para el texto de la descripción.
1. Agregar la descripción a los párrafos de la página.
1. Crear y dar estilo a una tabla (columnas, bordes, relleno y fuente).
1. Poblar filas de la tabla y agregar la tabla a los párrafos de la página.
1. Guardar la salida como `Complex.pdf`.

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    image_file_name = self.data_dir + "logo.png"
    page.add_image(image_file_name, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    description_text = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(description_text)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    header_row = table.rows.add()
    header_row.cells.add("Departs City")
    header_row.cells.add("Departs Island")

    i = 0
    while i < header_row.cells.count:
        header_row.cells[i].background_color = ap.Color.gray
        header_row.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    inc_time = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        data_row = table.rows.add()
        data_row.cells.add(str(time))
        time = time.__add__(inc_time)
        data_row.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
