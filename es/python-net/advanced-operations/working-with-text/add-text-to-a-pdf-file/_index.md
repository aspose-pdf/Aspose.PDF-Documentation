---
title: Añadir Texto a PDF usando Python
linktitle: Añadir Texto a PDF
type: docs
weight: 10
url: /es/python-net/add-text-to-pdf-file/
description: Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprende cómo añadir texto a PDF, añadir fragmentos HTML o usar fuentes OTF personalizadas.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Texto a PDF usando Python",
    "alternativeHeadline": "Cómo añadir Texto a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, añadir texto a pdf",
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
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF para Python. Aprende cómo añadir texto a PDF, añadir fragmentos HTML o usar fuentes OTF personalizadas."
}
</script>


## Agregar Texto

1. Abra el documento PDF de entrada usando Aspose.PDF.
1. Seleccione la página en particular a la que desea agregar el texto.
1. Cree un objeto TextFragment. Se crea un fragmento de texto con el contenido 'texto principal'. Este fragmento se posiciona en las coordenadas (100, 600) en la página.
1. Configuración de Propiedades de Texto. Se establecen varias propiedades del texto, como tamaño de fuente, tipo de fuente (Times New Roman), color de fondo (gris claro) y color de primer plano (rojo).
1. Crear el Objeto TextBuilder. Se instancia un objeto TextBuilder con la página seleccionada.
1. Anexar el Fragmento de Texto. El fragmento de texto creado anteriormente se adjunta a la página PDF usando el objeto TextBuilder.
1. Llamar al método [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y guardar el archivo PDF de salida.

El siguiente fragmento de código le muestra cómo agregar texto en un archivo PDF existente:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obtener página en particular
    page = document.pages[1]

    # Crear fragmento de texto
    text_fragment = ap.text.TextFragment("texto principal")
    text_fragment.position = ap.text.Position(100, 600)

    # Establecer propiedades del texto
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Crear objeto TextBuilder
    builder = ap.text.TextBuilder(page)

    # Anexar el fragmento de texto a la página PDF
    builder.append_text(text_fragment)

    # Guardar el documento PDF resultante.
    document.save(output_pdf)             
```


## Cargando Fuente desde un Flujo

El siguiente fragmento de código muestra cómo cargar una fuente desde un objeto de flujo al agregar texto a un documento PDF.

```python

    import aspose.pdf as ap

    # Cargar archivo PDF de entrada
    document = ap.Document()
    document.pages.add()
    # Crear objeto constructor de texto para la primera página del documento
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Crear fragmento de texto con cadena de ejemplo
    text_fragment = ap.text.TextFragment("Hola mundo")

    if input_ttf != "":
        # Cargar la fuente TrueType en el objeto de flujo
        font_stream = open(input_ttf, "rb")
        # Establecer el nombre de la fuente para la cadena de texto
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Especificar la posición para el Fragmento de Texto
        text_fragment.position = ap.text.Position(10, 10)
        # Agregar el texto al TextBuilder para que pueda colocarse sobre el archivo PDF
        text_builder.append_text(text_fragment)
        # Guardar el documento PDF resultante.
        document.save(output_pdf)
```


## Añadir Texto usando TextParagraph

El siguiente fragmento de código te muestra cómo agregar texto en un documento PDF utilizando la clase [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document()
    # Añadir página a la colección de páginas del objeto Document
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Crear párrafo de texto
    paragraph = ap.text.TextParagraph()
    # Establecer la sangría de las líneas subsiguientes
    paragraph.subsequent_lines_indent = 20
    # Especificar la ubicación para añadir TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Especificar el modo de ajuste de palabras
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Crear fragmento de texto
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Añadir fragmento al párrafo
    paragraph.append_line(fragment1)
    # Añadir párrafo
    builder.append_paragraph(paragraph)

    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


## Añadir Hipervínculo a TextSegment

Este código demuestra cómo crear contenido dinámico e interactivo dentro de un documento PDF, incluyendo hipervínculos a recursos externos.

Una página PDF puede componerse de uno o más objetos TextFragment, donde cada objeto TextFragment puede tener una o más instancias de [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

Por favor, intente usar el siguiente fragmento de código para cumplir con este requisito:

```python

    import aspose.pdf as ap

    # Crear una instancia de documento
    document = ap.Document()
    # Añadir página a la colección de páginas del archivo PDF
    page1 = document.pages.add()
    # Crear una instancia de TextFragment
    tf = ap.text.TextFragment("Fragmento de Texto de Ejemplo")
    # Establecer alineación horizontal para TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Crear un textsegment con texto de ejemplo
    segment = ap.text.TextSegment(" ... Segmento de Texto 1...")
    # Añadir segmento a la colección de segmentos de TextFragment
    tf.segments.append(segment)
    # Crear un nuevo TextSegment
    segment = ap.text.TextSegment("Enlace a Google")
    # Añadir segmento a la colección de segmentos de TextFragment
    tf.segments.append(segment)
    # Establecer hipervínculo para TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Establecer color de primer plano para el segmento de texto
    segment.text_state.foreground_color = ap.Color.blue
    # Establecer formato de texto como cursiva
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Crear otro objeto TextSegment
    segment = ap.text.TextSegment("TextSegment sin hipervínculo")
    # Añadir segmento a la colección de segmentos de TextFragment
    tf.segments.append(segment)
    # Añadir TextFragment a la colección de párrafos del objeto de página
    page1.paragraphs.add(tf)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


## Usar Fuente OTF

Aspose.PDF para Python a través de .NET ofrece la función de usar fuentes Personalizadas/TrueType al crear/manipular los contenidos de archivos PDF para que los contenidos del archivo se muestren utilizando fuentes distintas a las fuentes del sistema predeterminadas.

```python

    import aspose.pdf as ap

    # Crear una nueva instancia de documento
    document = ap.Document()
    # Agregar página a la colección de páginas del archivo PDF
    page = document.pages.add()
    # Crear instancia de TextFragment con texto de muestra
    fragment = ap.text.TextFragment("Texto de muestra en fuente OTF")
    # O incluso puede especificar la ruta de la fuente OTF en el directorio del sistema
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Especificar para embeber la fuente dentro del archivo PDF, para que se muestre correctamente,
    # Incluso si la fuente específica no está instalada/presente en la máquina de destino
    fragment.text_state.font.is_embedded = True
    # Agregar TextFragment a la colección de párrafos de la instancia de Page
    page.paragraphs.add(fragment)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


## Agregar cadena HTML utilizando DOM

El siguiente código de Python utiliza la biblioteca Aspose.PDF para crear un documento PDF con un fragmento HTML.

1. Instanciar Document. Se crea una instancia de la clase Document, que representa el documento PDF.
1. Agregar página al documento PDF.
1. Instanciar un objeto HtmlFragment con contenido HTML.
1. Establecer márgenes para el fragmento HTML. En este caso, el margen inferior se establece en 10 puntos y el margen superior en 200 puntos.
1. Agregar fragmento HTML a la página.
1. Guardar archivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    doc = ap.Document()
    # Agregar una página a la colección de páginas del archivo PDF
    page = doc.pages.add()
    # Instanciar HtmlFragment con contenido HTML
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # Establecer información del margen inferior
    title.margin.bottom = 10
    # Establecer información del margen superior
    title.margin.top = 200
    # Agregar fragmento HTML a la colección de párrafos de la página
    page.paragraphs.add(title)
    # Guardar archivo PDF
    doc.save(output_pdf)
```


### Estilo de línea personalizado para FootNote

El siguiente ejemplo demuestra cómo agregar notas al pie en la parte inferior de la página PDF y definir un estilo de línea personalizado.

```python

    import aspose.pdf as ap

    # Crear una instancia de Documento
    doc = ap.Document()
    # Agregar página a la colección de páginas del PDF
    page = doc.pages.add()
    # Crear objeto GraphInfo
    graph = ap.GraphInfo()
    # Establecer el ancho de línea como 2
    graph.line_width = 2
    # Establecer el color para el objeto gráfico
    graph.color = ap.Color.red
    # Establecer el valor del array de guiones como 3
    graph.dash_array = [3]
    # Establecer el valor de fase de guiones como 1
    graph.dash_phase = 1
    # Establecer el estilo de línea de la nota al pie de la página como gráfico
    page.note_line_style = graph
    # Crear una instancia de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Establecer el valor de FootNote para TextFragment
    text.foot_note = ap.Note("nota al pie para el texto de prueba 1")
    # Agregar TextFragment a la colección de párrafos de la primera página del documento
    page.paragraphs.add(text)
    # Crear el segundo TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Establecer la nota al pie para el segundo fragmento de texto
    text.foot_note = ap.Note("nota al pie para el texto de prueba 2")
    # Agregar el segundo fragmento de texto a la colección de párrafos del archivo PDF
    page.paragraphs.add(text)
    # Guardar el documento PDF resultante.
    doc.save(output_pdf)
```


### Personalizar etiqueta de nota al pie

El siguiente fragmento de código muestra cómo crear un documento PDF con un fragmento de texto que contiene una nota al pie.

Por defecto, el número de la nota al pie es incremental comenzando desde 1. Sin embargo, podemos tener el requerimiento de establecer una etiqueta de nota al pie personalizada. Para cumplir con este requisito, intenta usar el siguiente fragmento de código

```python

    import aspose.pdf as ap

    # Crear una instancia de Document
    document = ap.Document()
    # Agregar página a la colección de páginas del PDF
    page = document.pages.add()
    # Crear objeto GraphInfo
    graph = ap.GraphInfo()
    # Establecer el ancho de línea como 2
    graph.line_width = 2
    # Establecer el color para el objeto graph
    graph.color = ap.Color.red
    # Establecer el valor del array de guiones como 3
    graph.dash_array = [3]
    # Establecer el valor de fase de guiones como 1
    graph.dash_phase = 1
    # Establecer el estilo de línea de nota al pie para la página como graph
    page.note_line_style = graph
    # Crear una instancia de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Establecer el valor de FootNote para TextFragment
    text.foot_note = ap.Note("nota al pie para el texto de prueba 1")
    # Especificar etiqueta personalizada para FootNote
    text.foot_note.text = " Aspose"
    # Agregar TextFragment a la colección de párrafos de la primera página del documento
    page.paragraphs.add(text)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


## Añadir Imagen y Tabla a la Nota al Pie

Este código demuestra cómo crear un documento PDF con un fragmento de texto que contiene una nota al pie compleja que incluye una imagen, texto y una tabla utilizando Aspose.PDF para Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("algún texto")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("texto de la nota al pie")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Fila 1 Celda 1"))
    text.foot_note.paragraphs.add(table)

    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```

## Cómo Crear Notas al Final

Una Nota al Final es una cita de fuente que refiere a los lectores a un lugar específico al final del documento donde pueden encontrar la fuente de la información o palabras citadas o mencionadas en el documento.
 Cuando se utilizan notas al final, la oración citada o parafraseada o el material resumido es seguido por un número en superíndice.

Este código demuestra cómo agregar un fragmento de texto con una nota al final a un documento PDF usando Aspose.PDF para Python:

```python

    import aspose.pdf as ap

    # Crear instancia de Document
    document = ap.Document()
    # Agregar página a la colección de páginas del PDF
    page = document.pages.add()
    # Crear instancia de TextFragment
    text = ap.text.TextFragment("Hola Mundo")
    # Establecer valor de EndNote para TextFragment
    text.end_note = ap.Note("nota al final de ejemplo")
    # Especificar etiqueta personalizada para FootNote
    text.end_note.text = " Aspose"
    # Agregar TextFragment a la colección de párrafos de la primera página del documento
    page.paragraphs.add(text)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```

## Texto e Imagen como Párrafo en Línea

El diseño predeterminado del archivo PDF es diseño de flujo (de arriba a la izquierda a abajo a la derecha). Por lo tanto, cada nuevo elemento que se añade al archivo PDF se agrega en el flujo inferior derecho. Sin embargo, podemos tener un requisito para mostrar varios elementos de la página, es decir, Imagen y Texto al mismo nivel (uno tras otro). Un enfoque puede ser crear una instancia de Tabla y agregar ambos elementos a objetos de celda individuales. Sin embargo, otro enfoque puede ser el párrafo InLine. Al establecer la propiedad IsInLineParagraph de Imagen y Texto como verdadera, estos párrafos aparecerán como en línea con otros elementos de la página.

El siguiente fragmento de código te muestra cómo agregar texto e imagen como párrafos en línea en un archivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar instancia de Documento
    document = ap.Document()
    # Añadir página a la colección de páginas de la instancia de Documento
    page = document.pages.add()
    # Crear TextFragment
    text = ap.text.TextFragment("Hola Mundo.. ")
    # Añadir fragmento de texto a la colección de párrafos del objeto Page
    page.paragraphs.add(text)
    # Crear una instancia de imagen
    image = ap.Image()
    # Establecer imagen como párrafo en línea para que aparezca justo después
    # del objeto de párrafo anterior (TextFragment)
    image.is_in_line_paragraph = True
    # Especificar la ruta del archivo de imagen
    image.file = input_jpg
    # Establecer altura de imagen (opcional)
    image.fix_height = 30
    # Establecer ancho de imagen (opcional)
    image.fix_width = 100
    # Añadir imagen a la colección de párrafos del objeto de página
    page.paragraphs.add(image)
    # Re-inicializar objeto TextFragment con diferentes contenidos
    text = ap.text.TextFragment(" Hola de nuevo..")
    # Establecer TextFragment como párrafo en línea
    text.is_in_line_paragraph = True
    # Añadir el nuevo TextFragment creado a la colección de párrafos de la página
    page.paragraphs.add(text)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```

## Especificar el Espaciado de Caracteres al agregar Texto

El siguiente fragmento de código muestra cómo generar un documento PDF que contiene un fragmento de texto con espaciado de caracteres aumentado.

El texto se puede agregar dentro de una colección de párrafos de archivos PDF usando la instancia de TextFragment o utilizando el objeto TextParagraph e incluso puedes estampar el texto dentro del PDF usando la clase TextStamp.

### Usando TextBuilder y TextFragment

```python

    import aspose.pdf as ap

    # Crear instancia de Document
    document = ap.Document()
    # Agregar página a la colección de páginas del Documento
    document.pages.add()
    # Crear instancia de TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Crear instancia de fragmento de texto con contenido de ejemplo
    wide_fragment = ap.text.TextFragment("Texto con espaciado de caracteres aumentado")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Especificar el espaciado de caracteres para TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Especificar la posición de TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Agregar TextFragment a la instancia de TextBuilder
    builder.append_text(wide_fragment)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


### Usando TextParagraph

```python

    import aspose.pdf as ap

    # Crear instancia de Document
    document = ap.Document()
    # Añadir página a la colección de páginas del Document
    document.pages.add()
    # Crear instancia de TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Instanciar instancia de TextParagraph
    paragraph = ap.text.TextParagraph()
    # Crear instancia de TextState para especificar el nombre y tamaño de la fuente
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Especificar el espaciado de caracteres
    state.character_spacing = 1.5
    # Añadir texto al objeto TextParagraph
    tt = "Este es un párrafo con espaciado de caracteres"
    paragraph.append_line(tt, state)
    # Especificar la posición para TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Añadir TextParagraph a la instancia de TextBuilder
    builder.append_paragraph(paragraph)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```

### Usando TextStamp

```python

    import aspose.pdf as ap

    # Crear instancia de Document
    document = ap.Document()
    # Añadir página a la colección de páginas del Document
    page = document.pages.add()
    # Instanciar instancia de TextStamp con texto de muestra
    stamp = ap.TextStamp("Este es un sello de texto con espaciado de caracteres")
    # Especificar el nombre de la fuente para el objeto Stamp
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Especificar el tamaño de la fuente para TextStamp
    stamp.text_state.font_size = 12
    # Especificar espaciado de caracteres como 1
    stamp.text_state.character_spacing = 1
    # Establecer la x_indent para Stamp
    stamp.x_indent = 100
    # Establecer la y_indent para Stamp
    stamp.y_indent = 500
    # Añadir sello textual a la instancia de página
    stamp.put(page)
    # Guardar el documento PDF resultante.
    document.save(output_pdf)
```


## Crear documento PDF de varias columnas

[Aspose.PDF para Python a través de .NET](https://docs.aspose.com/pdf/python-net/) también ofrece la función de crear múltiples columnas dentro de las páginas de documentos PDF. Para crear un archivo PDF de varias columnas, podemos hacer uso de la clase FloatingBox ya que proporciona la propiedad column_info para especificar el número de columnas dentro de FloatingBox y también podemos especificar el espacio entre columnas y los anchos de las columnas usando las propiedades column_spacing y width respectivamente.

El espacio entre columnas significa el espacio entre las columnas y el espacio predeterminado entre las columnas es de 1,25 cm. Si no se especifica el ancho de la columna, entonces [Aspose.PDF para Python a través de .NET](https://docs.aspose.com/pdf/python-net/) calcula el ancho de cada columna automáticamente de acuerdo con el tamaño de la página y el espacio entre columnas.

A continuación se da un ejemplo para demostrar la creación de dos columnas con objetos Graphs (Line) y se añaden a la colección de párrafos de FloatingBox, que luego se añade a la colección de párrafos de la instancia Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Especificar la información del margen izquierdo para el archivo PDF
    document.page_info.margin.left = 40
    # Especificar la información del margen derecho para el archivo PDF
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Agregar la línea a la colección de párrafos del objeto sección
    page.paragraphs.add(graph1)

    # Especificar las coordenadas para la línea
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Crear variables string con texto que contiene etiquetas html
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> Cómo evitar las estafas de dinero</<strong> "
        + "</font>"
    )
    # Crear párrafos de texto que contienen texto HTML
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Añadir cuatro columnas en la sección
    box.column_info.column_count = 2
    # Establecer el espacio entre las columnas
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("Por Un Googler (El Blog Oficial de Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Crear un objeto de gráficos para dibujar una línea
    graph2 = ap.drawing.Graph(50, 10)
    # Especificar las coordenadas para la línea
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Añadir la línea a la colección de párrafos del objeto sección
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Guardar archivo PDF
    document.save(output_pdf)
```


## Trabajando con Tabulaciones Personalizadas

Este fragmento de código en Python muestra cómo crear un documento PDF que contiene fragmentos de texto organizados utilizando tabulaciones para simular una estructura de tabla.

Aquí hay un ejemplo de cómo establecer tabulaciones personalizadas.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "Este es un ejemplo de formación de tabla con tabulaciones", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## Cómo Agregar Texto Transparente en PDF

Un archivo PDF contiene objetos de Imagen, Texto, Gráfico, adjuntos, Anotaciones y al crear un TextFragment, puedes establecer información de color de primer plano, color de fondo, así como el formato de texto. Aspose.PDF para Python a través de .NET admite la característica de agregar texto con canal de color Alpha.

El siguiente fragmento de código muestra cómo agregar texto con color transparente.

```python

    import aspose.pdf as ap

    # Crear instancia de Documento
    document = ap.Document()
    # Crear página para la colección de páginas del archivo PDF
    page = document.pages.add()

    # Crear instancia de TextFragment con un valor de ejemplo
    text = ap.text.TextFragment(
        "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente "
    )
    # Crear objeto de color desde el canal Alpha
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Establecer información de color para la instancia de texto
    text.text_state.foreground_color = color
    # Agregar texto a la colección de párrafos de la instancia de página
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## Especificar el Espaciado entre Líneas para Fuentes

Cada fuente tiene un cuadrado abstracto, cuya altura es la distancia prevista entre líneas de texto en el mismo tamaño de fuente. Este cuadrado se llama el cuadrado em y es la cuadrícula de diseño en la que se definen los contornos de los glifos. Muchas letras de la fuente de entrada tienen puntos que están colocados fuera de los límites del cuadrado em de la fuente, por lo que para mostrar la fuente correctamente, se necesita el uso de una configuración especial.

El siguiente fragmento de código carga un PDF, agrega un fragmento de texto con un espaciado entre líneas específico usando una fuente TrueType, y guarda el documento PDF modificado:

```python

    import aspose.pdf as ap

    # Cargar archivo PDF de entrada
    document = ap.Document()
    # Crear TextFormattingOptions con LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Crear fragmento de texto con cadena de ejemplo
    text_fragment = ap.text.TextFragment("Hola mundo")

    # Cargar la fuente TrueType en el objeto stream
    font_stream = open(input_ttf, "rb")
    # Establecer el nombre de la fuente para la cadena de texto
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Especificar la posición para el Fragmento de Texto
    text_fragment.position = ap.text.Position(100, 600)
    # Establecer TextFormattingOptions del fragmento actual a predefinido (que apunta a LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Guardar el documento PDF resultante
    document.save(output_pdf)
```


## Obtener el Ancho del Texto Dinámicamente

Este fragmento de código en Python realiza una comparación entre las mediciones de cadenas obtenidas de un objeto de fuente y un objeto de estado de texto en Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("¡Medición de cadena de fuente inesperada!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("¡Medición de cadena de fuente inesperada!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("¡La medición de cadenas de fuente y estado no coincide!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>