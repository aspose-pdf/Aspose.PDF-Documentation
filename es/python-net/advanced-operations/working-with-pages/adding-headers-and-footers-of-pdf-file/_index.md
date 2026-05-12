---
title: Agregar encabezados y pies de página al PDF en Python
linktitle: Agregar encabezado y pie de página al PDF
type: docs
weight: 50
url: /es/python-net/add-headers-and-footers-of-pdf-file/
description: Aprende cómo agregar encabezados y pies de página a archivos PDF en Python usando texto, imágenes y contenido estructurado.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agrega encabezados y pies de página a archivos PDF con Python
Abstract: Este artículo muestra cómo agregar encabezados y pies de página a documentos PDF con Aspose.PDF for Python via .NET. Cubre texto, numeración de páginas, HTML, imagen, tabla y contenido de encabezado y pie de página basado en LaTeX.
---

Utilice esta página para agregar contenido de encabezado y pie de página coherente en todas las páginas del PDF con **Aspose.PDF for Python via .NET**.

Puedes crear encabezados y pies de página con [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), y [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objetos, luego aplícalos a través de [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) en cada página.

## Agregar encabezados y pies de página como fragmentos de texto

Agrega encabezados y pies de página de texto simples a todas las páginas de un PDF. Crea [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos, inserciones [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) elementos en ellos, conjuntos [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para un posicionamiento adecuado y los adjunta a cada página del documento. El resultado es un PDF donde cada página muestra texto de encabezado y pie de página consistentes.

El siguiente fragmento de código muestra cómo agregar encabezados y pies de página como fragmentos de texto en un PDF usando Python:

1. Crear fragmentos de texto para el encabezado y el pie de página.
1. Crear objetos HeaderFooter y agregar los fragmentos de texto a ellos.
1. Defina la configuración de márgenes para controlar la ubicación del encabezado y el pie de página.
1. Cargue el documento PDF desde el archivo de entrada.
1. Iterar a través de todas las páginas del documento.
1. Asigna el encabezado y el pie de página a cada página.
1. Guarde el PDF modificado en el archivo de salida.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Este método es útil para añadir títulos consistentes, indicadores de página o avisos legales en la parte superior e inferior de cada página. También puedes ampliarlo para incluir imágenes o contenido dinámico, como números de página.

## Añadiendo encabezados y pies de página para la numeración de páginas

Agregar numeración automática de páginas a los encabezados y pies de página de un documento PDF usando Aspose.PDF for Python. Usando las variables integradas $p (número de página actual) y $P (número total de páginas), el script inserta dinámicamente la numeración de páginas en cada página. Los encabezados muestran el formato \u0027Page X from Y\u0027, mientras que los pies de página muestran \u0027Page X / Y\u0027. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) garantiza una colocación adecuada en cada página.

1. Cree un TextFragment para el encabezado usando "Page $p from $P" para mostrar la página actual y el total de páginas.
1. Cree un objeto HeaderFooter y añada el texto del encabezado a él.
1. Cree un TextFragment para el pie de página usando \"Page $p / $P\" para un estilo de numeración alternativo.
1. Crea un objeto Footer y añade el texto del pie de página.
1. Definir la configuración de márgenes (izquierda = 50, superior = 20) y aplicarlos tanto al encabezado como al pie de página.
1. Abra el documento PDF del archivo de entrada.
1. Itere a través de todas las páginas y asigne el encabezado y el pie de página a cada una.
1. Guarde el PDF actualizado en la ruta de salida.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como fragmentos HTML

Aplicar encabezados y pies de página con formato HTML a cada página de un documento PDF usando Aspose.PDF for Python. Al usar [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), el script permite que el estilo de texto enriquecido—como negrita y cursiva—aparezca en el encabezado y pie de página. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) se aplica para una colocación adecuada, y los mismos elementos formateados se adjuntan a cada página del documento.

El siguiente fragmento de código demuestra cómo agregar encabezados y pies de página como fragmentos HTML a un PDF usando Python:

1. Crear un fragmento de encabezado HTML usando HtmlFragment—incluyendo texto con estilo como '<strong>' para negrita.
1. Crea un objeto HeaderFooter y añade el encabezado HTML a él.
1. Crea un fragmento de pie de página HTML usando '<i>' para estilo cursiva.
1. Cree un objeto Footer y añada el HTML del pie de página a él.
1. Configure los márgenes (left = 50, top = 20) y asígnelos tanto al encabezado como al pie de página.
1. Cargue el documento PDF usando 'ap.Document()'.
1. Recorra todas las páginas y asigne el encabezado y el pie de página a cada una.
1. Guarda el PDF modificado en la ruta de salida especificada.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Usar HtmlFragment permite un formato enriquecido con estilos en línea o marcado HTML, brindándole mayor flexibilidad de diseño en comparación con texto plano.

## Agregar encabezados y pies de página como imágenes

Agregar encabezados y pies de página basados en imágenes a cada página de un documento PDF usando Aspose.PDF for Python. El mismo archivo de imagen se utiliza tanto para el encabezado como para el pie de página en cada página. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) posiciona las imágenes, y la imagen se ajusta automáticamente para encajar dentro del área del encabezado/pie de página.

El siguiente fragmento de código muestra cómo agregar encabezados y pies de página como imágenes a un PDF usando Python:

1. Cargue la imagen en un objeto 'ap.Image' y prepárela para usarla como encabezado.
1. Cree un objeto HeaderFooter y adjunte la imagen del encabezado a él.
1. Cargue la misma imagen de nuevo para usarla como pie de página.
1. Cree un objeto Footer y agregue la imagen del pie de página a él.
1. Cargue el documento PDF de entrada usando 'ap.Document()'.
1. Iterar a través de todas las páginas del documento.
1. Aplicar márgenes (izquierda = 50) para posicionar tanto el encabezado como el pie de página.
1. Asigne el encabezado y el pie de página a cada página del PDF.
1. Guarde el PDF actualizado en el archivo de salida especificado.

Esta técnica es ideal para marcar documentos con logotipos o marcas de agua en el área de encabezado/pie de página.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como tabla

Agregar encabezados y pies de página estructurados, basados en tablas, a todas las páginas de un documento PDF usando Aspose.PDF for Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) Los objetos ofrecen un mejor control de diseño, alineación y formato consistente para encabezados y pies de página complejos. El texto del encabezado está centrado mientras que el texto del pie de página está alineado a la izquierda, ambos usando la fuente Arial 12pt. Los anchos de columna se calculan dinámicamente según las dimensiones de la página para garantizar una colocación adecuada.

Este fragmento de código agrega encabezados y pies de página (usando tablas) a cada página de un documento PDF con Aspose.PDF for Python via .NET.

1. Definir estilos de texto usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para encabezado y pie de página (fuente, tamaño, alineación).
1. Crear [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos para el encabezado y pie de página.
1. Construir el encabezado [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) con una sola fila y una celda que contiene el texto del encabezado.
1. Construir el pie de página [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) con una única fila y celda que contiene el texto del pie de página.
1. Agregue las tablas a las correspondientes [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos.
1. Establecer pie de página [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para un posicionamiento horizontal adecuado.
1. Abre el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropiados.
1. Iterar a través de todas las páginas y asignar el encabezado y pie de página basados en tabla a cada página.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) al archivo de salida.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Agregar encabezados y pies de página como LaTeX

Agregue encabezados y pies de página que contengan contenido formateado en LaTeX a todas las páginas de un documento PDF usando Aspose.PDF for Python. LaTeX permite la representación de símbolos matemáticos, fechas, marcas de derechos de autor y otros formatos avanzados. El encabezado incluye una fecha dinámica, mientras que el pie de página muestra el símbolo de derechos de autor junto con el número de página actual y el recuento total de páginas.

El siguiente fragmento de código muestra cómo usar [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) en encabezados y pies de página para un PDF usando Aspose.PDF for Python via .NET.

1. Abre el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropiados.
1. Determinar el recuento total de páginas para usar en pies de página dinámicos.
1. Iterar a través de todas las páginas del documento.
1. Cree un [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objeto para el encabezado.
1. Cree un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el texto del encabezado que contiene comandos LaTeX (p. ej., `\\today\\`).
1. Cree un [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objeto para el pie de página.
1. Cree un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para el texto del pie de página que incluye símbolos LaTeX y numeración de página.
1. Agregar el [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) al objeto de encabezado/pie de página correspondiente.
1. Vincula el encabezado y el pie de página a la página actual.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) al archivo de salida.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Agregar números de página al PDF en Python](/pdf/es/python-net/add-page-number/)
- [Estampar páginas PDF en Python](/pdf/es/python-net/stamping/)
- [Formatear documentos PDF en Python](/pdf/es/python-net/formatting-pdf-document/)