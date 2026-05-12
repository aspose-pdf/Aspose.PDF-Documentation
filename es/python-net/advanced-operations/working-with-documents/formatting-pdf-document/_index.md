---
title: Formatear documentos PDF en Python
linktitle: Formatear documento PDF
type: docs
weight: 11
url: /es/python-net/formatting-pdf-document/
description: Aprenda cómo formatear documentos PDF, incrustar fuentes, controlar la configuración del visor y ajustar las opciones de visualización en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formateo de documentos PDF usando Python
Abstract: El artículo proporciona una guía completa sobre la manipulación y el formato de documentos PDF utilizando la biblioteca Aspose.PDF en Python. Cubre varios aspectos de la personalización de PDF, incluido el ajuste de la ventana del documento y las propiedades de visualización de página, como centrar la ventana, la dirección de lectura y ocultar elementos de la interfaz de usuario. El artículo explica cómo obtener y establecer estas propiedades programáticamente usando la clase `Document`. Además, aborda la gestión de fuentes, detallando cómo incrustar fuentes Standard Type 1 y otras fuentes en los PDFs, asegurando la portabilidad del documento y la consistencia visual entre sistemas. También destaca técnicas para establecer un nombre de fuente predeterminado, recuperar todas las fuentes de un PDF y mejorar la incrustación de fuentes usando `FontSubsetStrategy`. Asimismo, el artículo profundiza en el ajuste del factor de zoom de los documentos PDF mediante la clase `GoToAction` y la configuración de propiedades predefinidas del cuadro de diálogo de impresión, incluidas las opciones de impresión a doble cara. Los fragmentos de código acompañan a cada sección, proporcionando ejemplos prácticos para implementar estas funcionalidades.
---

Esta guía es útil cuando necesitas controlar el comportamiento del visor PDF, la incrustación de fuentes, la configuración de visualización predeterminada o las preferencias de impresión en documentos generados con Python.

## Formatear documento PDF

### Obtener propiedades de ventana del documento y de visualización de página

Este tema le ayuda a comprender cómo obtener las propiedades de la ventana del documento, la aplicación del visor y cómo se muestran las páginas. Para establecer estas propiedades:

Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase. Ahora, puedes establecer las propiedades del objeto Document, como

- CenterWindow – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- Dirección – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran una al lado de la otra. Predeterminado: de izquierda a derecha.
- DisplayDocTitle – Mostrar el título del documento en la barra de título de la ventana del documento. Predeterminado: false (el título se muestra).
- HideMenuBar – Ocultar o mostrar la barra de menús de la ventana del documento. Predeterminado: false (la barra de menús se muestra).
- HideToolBar – Ocultar o mostrar la barra de herramientas de la ventana del documento. Predeterminado: false (la barra de herramientas se muestra).
- HideWindowUI – Ocultar o mostrar los elementos de la ventana del documento, como las barras de desplazamiento. Predeterminado: false (los elementos de la UI se muestran).
- NonFullScreenPageMode – Cómo se muestra el documento cuando no está en modo de pantalla completa.
- PageLayout – El diseño de página.
- PageMode – Cómo se muestra el documento al abrirlo por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar el panel de adjuntos.

El siguiente fragmento de código le muestra cómo obtener las propiedades usando [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Establecer propiedades de la ventana del documento y de la visualización de la página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación del visor y la visualización de la página. Para establecer estas diferentes propiedades:

1. Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Establezca las propiedades del objeto Document.
1. Guarde el archivo PDF actualizado usando el método save.

Las propiedades disponibles son:

- CentrarVentana
- Dirección
- DisplayDocTitle
- AjustarVentana
- OcultarBarraDeMenú
- OcultarBarraDeHerramientas
- OcultarVentanaUI
- NonFullScreenPageMode
- Diseño de página
- Modo de página

Cada uno se usa y se describe en el código a continuación. El siguiente - fragmento de código muestra cómo establecer las propiedades usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Incrustación de fuentes estándar Tipo 1

Algunos documentos PDF tienen fuentes de un conjunto especial de fuentes de Adobe. Las fuentes de este conjunto se denominan “Standard Type 1 Fonts”. Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuentes requiere usar banderas especiales, es decir [incorporar_fuentes_estándar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). A continuación se muestra el fragmento de código que se puede usar para obtener un documento con todas las fuentes incrustadas, incluidas las fuentes estándar Type 1:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incrustar fuentes al crear PDF

Si necesita usar cualquier fuente que no sea una de las 14 fuentes básicas admitidas por Adobe Reader, debe incrustar la descripción de la fuente al generar el archivo PDF. Si la información de la fuente no está incrustada, Adobe Reader la tomará del Sistema Operativo si está instalada en el sistema, o construirá una fuente de sustitución según el descriptor de fuente en el PDF.

>Tenga en cuenta que la fuente incrustada debe estar instalada en la máquina host, es decir, en el caso del siguiente código la fuente ‘Univers Condensed’ está instalada en el sistema.

Utilizamos la propiedad 'is_embedded' para incrustar la información de la fuente en el archivo PDF. Establecer el valor de esta propiedad a 'True' incrustará el archivo de fuente completo en el PDF, sabiendo que aumentará el tamaño del archivo PDF. A continuación se muestra el fragmento de código que puede usarse para incrustar la información de la fuente en el PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Establecer nombre de fuente predeterminado al guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el propio documento ni en el dispositivo, la API reemplaza estas fuentes por la fuente predeterminada. Si la fuente está disponible (instalada en el dispositivo o incrustada en el documento), el PDF de salida debe conservar la misma fuente (no debe ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuente). Hemos implementado una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código puede usarse para establecer la fuente predeterminada:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Obtener todas las fuentes del documento PDF

En caso de que quieras obtener todas las fuentes de un documento PDF, puedes usar [utilidades_de_fuente](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) método proporcionado en [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase. Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Mejorar la incrustación de fuentes usando FontSubsetStrategy

El siguiente fragmento de código muestra cómo establecer [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) usado [utilidades_de_fuente](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propiedad:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Obtener-Establecer factor de zoom del archivo PDF

A veces, deseas determinar cuál es el factor de zoom actual de un documento PDF. Con Aspose.Pdf, puedes averiguar el valor actual así como establecer uno.

El [AcciónIrA](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) La propiedad Destination de la clase permite obtener el valor de zoom asociado a un archivo PDF. De manera similar, puede usarse para establecer el factor de zoom de un archivo.

#### Establecer factor de zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Obtener factor de zoom

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Crear archivos PDF en Python](/pdf/es/python-net/create-pdf-document/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
