---
title: Manipular Documento PDF en Python a través de .NET
linktitle: Manipular Documento PDF
type: docs
weight: 20
url: /es/python-net/manipulate-pdf-document/
description: Este artículo contiene información sobre cómo validar un Documento PDF para el Estándar PDF A usando Python, cómo trabajar con el índice, cómo establecer la fecha de caducidad del PDF, etc.
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Documento PDF a través de Python",
    "alternativeHeadline": "Cómo manipular un archivo PDF con Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, dotnet, python, manipular archivo pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentos de Aspose.PDF",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Este artículo contiene información sobre cómo validar un Documento PDF para el Estándar PDF A usando Python, cómo trabajar con el índice, cómo establecer la fecha de caducidad del PDF, etc."
}
</script>


## Manipular Documento PDF en Python

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad con PDF/A-1a o PDF/A-1b, utiliza el método [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Este método te permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerida enumeración PdfFormat: PDF_A_1A o PDF_A_1B.

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1A.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Validar PDF para PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1b.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Validar PDF para PDF/A-1b
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## Trabajando con TOC

### Agregar TOC a un PDF Existente

TOC en PDF significa "Tabla de Contenidos". Es una característica que permite a los usuarios navegar rápidamente a través de un documento proporcionando una visión general de sus secciones y encabezados.

Para agregar un TOC a un archivo PDF existente, use la clase Heading en el espacio de nombres [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). El espacio de nombres [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) puede tanto crear nuevos archivos PDF como manipular archivos PDF existentes. Para agregar un TOC a un PDF existente, use el espacio de nombres Aspose.Pdf. El siguiente fragmento de código muestra cómo crear una tabla de contenidos dentro de un archivo PDF existente usando Python a través de .NET.

```python

    import aspose.pdf as ap

    # Cargar un archivo PDF existente
    doc = ap.Document(input_pdf)

    # Acceder a la primera página del archivo PDF
    tocPage = doc.pages.insert(1)

    # Crear objeto para representar la información del TOC
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Tabla de Contenidos")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Establecer el título para el TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Crear objetos de cadena que se usarán como elementos del TOC
    titles = ["Primera página", "Segunda página", "Tercera página", "Cuarta página"]
    for i in range(0, 2):
        # Crear objeto Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Especificar la página de destino para el objeto heading
        heading2.destination_page = doc.pages[i + 2]

        # Página de destino
        heading2.top = doc.pages[i + 2].rect.height

        # Coordenada de destino
        segment2.text = titles[i]

        # Agregar encabezado a la página que contiene el TOC
        tocPage.paragraphs.add(heading2)

    # Guardar el documento actualizado
    doc.save(output_pdf)
```


### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF para Python también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesitas establecer la propiedad [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # establecer LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Tabla de Contenidos")
    title.text_state.font_size = 30
    toc_info.title = title

    # Añadir la sección de la lista a la colección de secciones del documento Pdf
    tocPage.toc_info = toc_info
    # Definir el formato de los cuatro niveles de lista estableciendo los márgenes izquierdos
    # y
    # configuraciones de formato de texto de cada nivel

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Crear una sección en el documento Pdf
    page = doc.pages.add()

    # Añadir cuatro encabezados en la sección
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Encabezado de Ejemplo" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Añadir el encabezado en la Tabla de Contenidos.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # guardar el Pdf
    doc.save(output_pdf)
```


### Ocultar Números de Página en el TOC

En caso de que no desees mostrar los números de página, junto con los encabezados en el TOC, puedes usar la propiedad [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la Clase [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) como falso. Por favor, revisa el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Tabla de Contenidos")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Agregar la sección de la lista a la colección de secciones del documento Pdf
    toc_page.toc_info = toc_info
    # Definir el formato de la lista de cuatro niveles configurando los márgenes
    # a la izquierda y la configuración del formato del texto de cada nivel

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Agregar cuatro encabezados en la sección
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "este es el encabezado de nivel " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### Personalizar los Números de Página al Agregar un Índice

Es común personalizar la numeración de las páginas en el índice al agregarlo en un documento PDF. Por ejemplo, puede ser necesario añadir algún prefijo antes del número de página como P1, P2, P3, etc. En tal caso, Aspose.PDF para Python proporciona la propiedad [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la clase [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) que se puede utilizar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```python

    import aspose.pdf as ap

    # Cargar un archivo PDF existente
    doc = ap.Document(input_pdf)
    # Acceder a la primera página del archivo PDF
    toc_page = doc.pages.insert(1)
    # Crear objeto para representar la información del índice
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Tabla de Contenidos")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Establecer el título para el índice
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Crear objeto de encabezado
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Especificar la página de destino para el objeto de encabezado
        heading2.destination_page = doc.pages[i + 1]
        # Página de destino
        heading2.top = doc.pages[i + 1].rect.height
        # Coordenada de destino
        segment2.text = "Página " + str(i)
        # Añadir encabezado a la página que contiene el índice
        toc_page.paragraphs.add(heading2)

    # Guardar el documento actualizado
    doc.save(output_pdf)

```


## Cómo establecer la fecha de vencimiento de un PDF

Aplicamos privilegios de acceso a archivos PDF para que un cierto grupo de usuarios pueda acceder a características/objetos particulares de documentos PDF. Para restringir el acceso al archivo PDF, usualmente aplicamos cifrado y podemos tener el requerimiento de establecer la expiración del archivo PDF, de modo que el usuario que accede/visualiza el documento reciba un aviso válido sobre la expiración del archivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    doc = ap.Document()
    # Agregar página a la colección de páginas del archivo PDF
    doc.pages.add()
    # Agregar fragmento de texto a la colección de párrafos del objeto página
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hola Mundo..."))
    # Crear objeto JavaScript para establecer la fecha de vencimiento del PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('El archivo ha expirado. Necesitas uno nuevo.');"
    )
    # Establecer JavaScript como acción de apertura del PDF
    doc.open_action = javaScript

    # Guardar Documento PDF
    doc.save(output_pdf)
```


## Aplanar PDF Rellenable en Python

Los documentos PDF a menudo incluyen formularios con widgets interactivos rellenables como botones de opción, casillas de verificación, cuadros de texto, listas, etc. Para hacerlo no editable para varios propósitos de aplicación, necesitamos aplanar el archivo PDF. Aspose.PDF proporciona la función para aplanar tu PDF en Python con solo unas pocas líneas de código:

```python

    import aspose.pdf as ap

    # Cargar el formulario PDF de origen
    doc = ap.Document(input_pdf)

    # Aplanar PDF Rellenable Aplanado
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Guardar el documento actualizado
    doc.save(output_pdf)
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python a través de .NET",
    "downloadUrl": "https://releases.aspose.com/pdf/python-net",
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