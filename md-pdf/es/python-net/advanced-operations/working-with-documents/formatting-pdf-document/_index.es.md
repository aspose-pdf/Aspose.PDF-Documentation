---
title: Formateo de Documento PDF usando Python
linktitle: Formateo de Documento PDF
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Crear y formatear el Documento PDF con Aspose.PDF para Python vía .NET. Use el siguiente fragmento de código para resolver sus tareas.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formateo de Documento PDF usando Python",
    "alternativeHeadline": "Cómo formatear Documento PDF en Python vía .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, dotnet, python, formatear documento pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentos Aspose.PDF",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Crear y formatear el Documento PDF con Aspose.PDF para Python vía .NET. Use el siguiente fragmento de código para resolver sus tareas."
}
</script>


## Formateo de Documento PDF

### Obtener Propiedades de la Ventana del Documento y de la Visualización de Páginas

Este tema te ayuda a entender cómo obtener las propiedades de la ventana del documento, la aplicación de visualización y cómo se muestran las páginas. Para establecer estas propiedades:

Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Ahora, puedes establecer las propiedades del objeto Document, tales como

- CenterWindow – Centrar la ventana del documento en la pantalla. Por defecto: falso.
- Direction – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran lado a lado. Por defecto: de izquierda a derecha.
- DisplayDocTitle – Mostrar el título del documento en la barra de título de la ventana del documento. Por defecto: falso (el título se muestra).
- HideMenuBar – Ocultar o mostrar la barra de menú de la ventana del documento. Por defecto: falso (la barra de menú se muestra).
- HideToolBar – Ocultar o mostrar la barra de herramientas de la ventana del documento. Por defecto: falso (la barra de herramientas se muestra).
- HideWindowUI – Ocultar o mostrar elementos de la ventana del documento como las barras de desplazamiento.
 Default: false (se muestran los elementos de la interfaz de usuario).
- NonFullScreenPageMode – Cómo se muestra el documento cuando no está en modo de pantalla completa.
- PageLayout – El diseño de la página.
- PageMode – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar panel de adjuntos.

El siguiente fragmento de código te muestra cómo obtener las propiedades usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obtener diferentes propiedades del documento
    # Posición de la ventana del documento - Predeterminado: falso
    print("CenterWindow :", document.center_window)

    # Orden de lectura predominante; determina la posición de la página
    # Cuando se muestra lado a lado - Predeterminado: L2R
    print("Direction :", document.direction)

    # Si la barra de título de la ventana debe mostrar el título del documento
    # Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: falso
    print("DisplayDocTitle :", document.display_doc_title)

    # Si se redimensiona la ventana del documento para ajustarse al tamaño de
    # La primera página mostrada - Predeterminado: falso
    print("FitWindow :", document.fit_window)

    # Si se oculta la barra de menú de la aplicación del visor - Predeterminado: falso
    print("HideMenuBar :", document.hide_menubar)

    # Si se oculta la barra de herramientas de la aplicación del visor - Predeterminado: falso
    print("HideToolBar :", document.hide_tool_bar)

    # Si se ocultan elementos de la interfaz de usuario como barras de desplazamiento
    # Y solo se muestran los contenidos de la página - Predeterminado: falso
    print("HideWindowUI :", document.hide_window_ui)

    # Modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # El diseño de la página, es decir, una sola página, una columna
    print("PageLayout :", document.page_layout)

    # Cómo debe mostrarse el documento cuando se abre
    # Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    print("pageMode :", document.page_mode)

```

### Configurar Propiedades de Ventana de Documento y Visualización de Página

Este tema explica cómo configurar las propiedades de la ventana del documento, la aplicación de visualización y la visualización de la página. Para configurar estas diferentes propiedades:

1. Abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Configure las propiedades del objeto Document.
1. Guarde el archivo PDF actualizado usando el método save.

Las propiedades disponibles son:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada una se utiliza y describe en el código a continuación. El siguiente fragmento de código le muestra cómo configurar las propiedades usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Configurar diferentes propiedades del documento
    # Especificar la posición de la ventana del documento - Predeterminado: false
    document.center_window = True

    # Orden de lectura predominante; determina la posición de la página
    # Cuando se muestra lado a lado - Predeterminado: L2R
    document.direction = ap.Direction.R2L

    # Especificar si la barra de título de la ventana debe mostrar el título del documento
    # Si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    document.display_doc_title = True

    # Especificar si redimensionar la ventana del documento para ajustar el tamaño de
    # La primera página mostrada - Predeterminado: false
    document.fit_window = True

    # Especificar si ocultar la barra de menú de la aplicación de visualización - Predeterminado: false
    document.hide_menubar = True

    # Especificar si ocultar la barra de herramientas de la aplicación de visualización - Predeterminado: false
    document.hide_tool_bar = True

    # Especificar si ocultar elementos de la interfaz de usuario como barras de desplazamiento
    # Y dejar solo el contenido de la página mostrado - Predeterminado: false
    document.hide_window_ui = True

    # Modo de página del documento. especificar cómo mostrar el documento al salir del modo de pantalla completa.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Especificar el diseño de página, es decir, página única, una columna
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Especificar cómo se debe mostrar el documento al abrirse
    # Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    document.page_mode = ap.PageMode.USE_THUMBS

    # Guardar archivo PDF actualizado
    document.save(output_pdf)
```


### Incrustación de Fuentes Tipo 1 Estándar

Algunos documentos PDF tienen fuentes de un conjunto especial de fuentes de Adobe. Las fuentes de este conjunto se llaman "Fuentes Tipo 1 Estándar". Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuentes requiere el uso de banderas especiales, es decir, [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). A continuación se muestra el fragmento de código que se puede usar para obtener un documento con todas las fuentes incrustadas, incluidas las Fuentes Tipo 1 Estándar:

```python

    import aspose.pdf as ap

    # Cargar un documento PDF existente
    document = ap.Document(input_pdf)
    # Establecer la propiedad EmbedStandardFonts del documento
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Verificar si la fuente ya está incrustada
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incrustación de Fuentes al crear PDF

Si necesita usar cualquier fuente que no sean las 14 fuentes principales compatibles con Adobe Reader, debe incrustar la descripción de la fuente al generar el archivo PDF. Si la información de la fuente no está incrustada, Adobe Reader la tomará del Sistema Operativo si está instalada en el sistema, o construirá una fuente sustituta de acuerdo con el descriptor de fuente en el PDF.

>Tenga en cuenta que la fuente incrustada debe estar instalada en la máquina anfitriona, es decir, en el caso del siguiente código, la fuente 'Univers Condensed' está instalada en el sistema.

Usamos la propiedad 'is_embedded' para incrustar la información de la fuente en el archivo PDF. Establecer el valor de esta propiedad en 'True' incrustará el archivo completo de la fuente en el PDF, sabiendo que aumentará el tamaño del archivo PDF. A continuación se muestra el fragmento de código que se puede usar para incrustar la información de la fuente en el PDF.

```python

    import aspose.pdf as ap

    # Crear una instancia del objeto Pdf llamando a su constructor vacío
    doc = ap.Document()

    # Crear una sección en el objeto Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" Este es un texto de ejemplo usando una fuente personalizada.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Guardar documento PDF
    doc.save(output_pdf)
```


### Establecer el Nombre de Fuente Predeterminado al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el documento mismo y en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Si la fuente está disponible (instalada en el dispositivo o incrustada en el documento), el PDF de salida debería tener la misma fuente (no debería ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuente). Hemos implementado una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código puede usarse para establecer la fuente predeterminada:

```python

    import aspose.pdf as ap

    # Cargar un documento PDF existente con fuente faltante
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Especificar el Nombre de Fuente Predeterminado
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Obtener Todas las Fuentes de un Documento PDF

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) proporcionado en la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 Por favor, revise el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Mejorar la Incrustación de Fuentes usando FontSubsetStrategy

El siguiente fragmento de código muestra cómo establecer la propiedad [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) utilizada en [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # Todas las fuentes se incrustarán como subconjunto en el documento en caso de SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # El subconjunto de fuentes se incrustará para las fuentes completamente incrustadas, pero las fuentes que no están incrustadas en el documento no se verán afectadas.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Obtener-Establecer Factor de Zoom de un Archivo PDF

A veces, deseas determinar cuál es el factor de zoom actual de un documento PDF. Con Aspose.Pdf, puedes averiguar el valor actual así como establecer uno.

La propiedad Destination de la clase [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) te permite obtener el valor de zoom asociado con un archivo PDF. De manera similar, puede ser utilizada para establecer el factor de zoom de un archivo.

#### Establecer Factor de Zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar nuevo objeto Document
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Guardar el documento
    doc.save(output_pdf)
```

#### Obtener Factor de Zoom

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar nuevo objeto Document
    doc = ap.Document(input_pdf)

    # Crear objeto GoToAction
    action = doc.open_action

    # Obtener el factor de Zoom del archivo PDF
    print(action.destination.zoom)
```


### Configuración de Propiedades Preestablecidas del Diálogo de Impresión

Aspose.PDF permite configurar los miembros [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) de un documento PDF. Esto te permite cambiar la propiedad DuplexMode de un documento PDF, que está configurada como simplex por defecto. Esto se puede lograr utilizando dos metodologías diferentes como se muestra a continuación.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Configuración de Propiedades Preestablecidas del Diálogo de Impresión usando el Editor de Contenido PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("El archivo tiene dúplex con el borde corto")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```