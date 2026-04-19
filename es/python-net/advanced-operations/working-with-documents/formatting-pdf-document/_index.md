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
AlternativeHeadline: Formatear documentos PDF usando Python
Abstract: El artículo ofrece una guía completa sobre la manipulación y el formato de documentos PDF utilizando la biblioteca Aspose.PDF en Python. Cubre varios aspectos de la personalización de PDF, incluyendo la configuración de la ventana del documento y las propiedades de visualización de la página, como centrar la ventana, la dirección de lectura y ocultar los elementos de la interfaz de usuario. El artículo explica cómo recuperar y establecer estas propiedades programáticamente usando la clase `Document`. Además, aborda la gestión de fuentes, detallando cómo incrustar fuentes Standard Type 1 y otras fuentes en PDFs, garantizando la portabilidad del documento y la consistencia visual entre sistemas. También destaca técnicas para establecer un nombre de fuente predeterminado, recuperar todas las fuentes de un PDF y mejorar la incrustación de fuentes usando `FontSubsetStrategy`. Además, el artículo profundiza en el ajuste del factor de zoom de los documentos PDF mediante la clase `GoToAction` y la configuración de las propiedades preestablecidas del cuadro de diálogo de impresión, incluyendo opciones de impresión a doble cara. Los fragmentos de código acompañan cada sección, proporcionando ejemplos prácticos para implementar estas funciones.
---

Esta guía es útil cuando necesita controlar el comportamiento del visor de PDF, la incrustación de fuentes, la configuración de visualización predeterminada o las preferencias de impresión en documentos generados con Python.

## Obtener propiedades de ventana y visualización de página del documento

Este tema le ayuda a comprender cómo obtener las propiedades de la ventana del documento, la aplicación del visor y cómo se muestran las páginas. Para establecer estas propiedades:

Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase. Ahora, puedes establecer las propiedades del objeto Document, como

- CenterWindow – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- Dirección – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran una al lado de la otra. Predeterminado: de izquierda a derecha.
- DisplayDocTitle – Mostrar el título del documento en la barra de título de la ventana del documento. Predeterminado: false (el título se muestra).
- HideMenuBar – Ocultar o mostrar la barra de menús de la ventana del documento. Predeterminado: false (la barra de menús se muestra).
- HideToolBar – Ocultar o mostrar la barra de herramientas de la ventana del documento. Predeterminado: false (la barra de herramientas se muestra).
- HideWindowUI – Ocultar o mostrar los elementos de la ventana del documento como barras de desplazamiento. Predeterminado: false (los elementos de la UI se muestran).
- NonFullScreenPageMode – Cómo el documento cuando no se muestra en modo de página completa.
- PageLayout – El diseño de la página.
- PageMode – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar el panel de adjuntos.

El siguiente fragmento de código le muestra cómo obtener las propiedades usando [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)

# Get different document properties
# Position of document's window - Default: false
print("CenterWindow :", document.center_window)

# Predominant reading order; determins the position of page
# When displayed side by side - Default: L2R
print("Direction :", document.direction)

# Whether window's title bar should display document title
# If false, title bar displays PDF file name - Default: false
print("DisplayDocTitle :", document.display_doc_title)

# Whether to resize the document's window to fit the size of
# First displayed page - Default: false
print("FitWindow :", document.fit_window)

# Whether to hide menu bar of the viewer application - Default: false
print("HideMenuBar :", document.hide_menubar)

# Whether to hide tool bar of the viewer application - Default: false
print("HideToolBar :", document.hide_tool_bar)

# Whether to hide UI elements like scroll bars
# And leaving only the page contents displayed - Default: false
print("HideWindowUI :", document.hide_window_ui)

# Document's page mode. How to display document on exiting full-screen mode.
print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

# The page layout i.e. single page, one column
print("PageLayout :", document.page_layout)

# How the document should display when opened
# I.e. show thumbnails, full-screen, show attachment panel
print("pageMode :", document.page_mode)
```

## Establecer propiedades de la ventana del documento y de visualización de la página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación del visor y la visualización de la página. Para establecer estas diferentes propiedades:

1. Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Establecer las propiedades del objeto Document.
1. Guarde el archivo PDF actualizado utilizando el método save.

Las propiedades disponibles son:

- VentanaCentrada
- Dirección
- DisplayDocTitle
- AjustarVentana
- OcultarBarraDeMenú
- OcultarBarraDeHerramientas
- HideWindowUI
- ModoDePaginaSinPantallaCompleta
- Diseño de página
- Modo de página

Cada uno se usa y se describe en el código a continuación. El siguiente - fragmento de código le muestra cómo establecer las propiedades usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)

# Set different document properties
# Sepcify to position document's window - Default: false
document.center_window = True

# Predominant reading order; determins the position of page
# When displayed side by side - Default: L2R
document.direction = ap.Direction.R2L

# Specify whether window's title bar should display document title
# If false, title bar displays PDF file name - Default: false
document.display_doc_title = True

# Specify whether to resize the document's window to fit the size of
# First displayed page - Default: false
document.fit_window = True

# Specify whether to hide menu bar of the viewer application - Default: false
document.hide_menubar = True

# Specify whether to hide tool bar of the viewer application - Default: false
document.hide_tool_bar = True

# Specify whether to hide UI elements like scroll bars
# And leaving only the page contents displayed - Default: false
document.hide_window_ui = True

# Document's page mode. specify how to display document on exiting full-screen mode.
document.non_full_screen_page_mode = ap.PageMode.USE_OC

# Specify the page layout i.e. single page, one column
document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

# Specify how the document should display when opened
# I.e. show thumbnails, full-screen, show attachment panel
document.page_mode = ap.PageMode.USE_THUMBS

# Save updated PDF file
document.save(output_pdf)
```

## Incrustación de fuentes Type 1 estándar

Algunos documentos PDF tienen fuentes de un conjunto especial de fuentes de Adobe. Las fuentes de este conjunto se llaman “Standard Type 1 Fonts”. Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuentes requiere el uso de banderas especiales, es decir [incrustar_fuentes_estándar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). A continuación se muestra el fragmento de código que se puede usar para obtener un documento con todas las fuentes incrustadas, incluidas las Standard Type 1 Fonts:

```python
import aspose.pdf as ap

# Load an existing PDF Document
document = ap.Document(input_pdf)
# Set EmbedStandardFonts property of document
document.embed_standard_fonts = True
for page in document.pages:
    if page.resources.fonts != None:
        for page_font in page.resources.fonts:
            # Check if font is already embedded
            if not page_font.is_embedded:
                page_font.is_embedded = True

document.save(output_pdf)
```

## Incrustar Font al crear PDF

Si necesita usar cualquier fuente distinta de las 14 fuentes principales admitidas por Adobe Reader, debe incrustar la descripción de la fuente al generar el archivo PDF. Si la información de la fuente no se incrusta, Adobe Reader la tomará del Sistema Operativo si está instalada en el sistema, o construirá una fuente de sustitución según el descriptor de fuente en el PDF.

>Tenga en cuenta que la fuente incrustada debe estar instalada en la máquina host, es decir, en caso del siguiente código la fuente ‘Univers Condensed’ está instalada en el sistema.

Utilizamos la propiedad 'is_embedded' para incrustar la información de la fuente en el archivo PDF. Establecer el valor de esta propiedad en 'True' incrustará el archivo de fuente completo en el PDF, sabiendo que aumentará el tamaño del archivo PDF. A continuación se muestra el fragmento de código que se puede usar para incrustar la información de la fuente en el PDF.

```python
import aspose.pdf as ap

# Instantiate Pdf object by calling its empty constructor
doc = ap.Document()

# Create a section in the Pdf object
page = doc.pages.add()

fragment = ap.text.TextFragment("")
segment = ap.text.TextSegment(" This is a sample text using Custom font.")
ts = ap.text.TextState()
ts.font = ap.text.FontRepository.find_font("Arial")
ts.font.is_embedded = True
segment.text_state = ts
fragment.segments.append(segment)
page.paragraphs.add(fragment)

# Save PDF Document
doc.save(output_pdf)
```

## Establecer el nombre de fuente predeterminado al guardar el PDF

Cuando un documento PDF contiene fuentes que no están disponibles ni en el propio documento ni en el dispositivo, la API reemplaza esas fuentes con la fuente predeterminada. Si la fuente está disponible (instalada en el dispositivo o incrustada en el documento), el PDF de salida debe tener la misma fuente (no debe ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuentes). Hemos implementado una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código se puede usar para establecer la fuente predeterminada:

```python
import aspose.pdf as ap

# Load an existing PDF document with missing font
document = ap.Document(input_pdf)

pdfSaveOptions = ap.PdfSaveOptions()
# Specify Default Font Name
newName = "Arial"
pdfSaveOptions.default_font_name = newName
document.save(output_pdf, pdfSaveOptions)
```

## Obtener todas las fuentes del documento PDF

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar [utilidades_fuente](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) método proporcionado en [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase. Por favor, revise el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```python
import aspose.pdf as ap

doc = ap.Document(input_pdf)
fonts = doc.font_utilities.get_all_fonts()
for font in fonts:
    print(font.font_name)
```

## Mejorar la incrustación de fuentes usando FontSubsetStrategy

El siguiente fragmento de código muestra cómo establecer [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) usado [utilidades_fuente](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propiedad:

```python
import aspose.pdf as ap

doc = ap.Document(input_pdf)
# All fonts will be embedded as subset into document in case of SubsetAllFonts.
doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
# Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
doc.save(output_pdf)
```

## Obtener/Establecer el factor de zoom del archivo PDF

A veces, deseas determinar cuál es el factor de zoom actual de un documento PDF. Con Aspose.Pdf, puedes averiguar el valor actual y también establecer uno.

El [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) La propiedad Destination de la clase permite obtener el valor de zoom asociado a un archivo PDF. De manera similar, puede usarse para establecer el factor de zoom de un archivo.

### Establecer factor de zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```python
import aspose.pdf as ap

# Instantiate new Document object
doc = ap.Document(input_pdf)

action = ap.annotations.GoToAction(
    ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
)
doc.open_action = action
# Save the document
doc.save(output_pdf)
```

### Obtener factor de zoom

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```python
import aspose.pdf as ap

# Instantiate new Document object
doc = ap.Document(input_pdf)

# Create GoToAction object
action = doc.open_action

# Get the Zoom factor of PDF file
print(action.destination.zoom)
```

## Configuración de propiedades preestablecidas del cuadro de diálogo de impresión

Aspoose.PDF permite establecer el [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) miembros de un documento PDF. Permite cambiar la propiedad DuplexMode de un documento PDF, que está configurada en simplex por defecto. Esto se puede lograr utilizando dos metodologías diferentes como se muestra a continuación.

```python
import aspose.pdf as ap

doc = ap.Document()
doc.pages.add()
doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
doc.save(output_pdf)
```

## Configuración de propiedades preestablecidas del cuadro de diálogo de impresión usando PDF Content Editor

```python
import aspose.pdf as ap

ed = ap.facades.PdfContentEditor()
ed.bind_pdf(input_pdf)
if (
    ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE
) > 0:
    print("The file has duplex flip short edge")

ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
ed.save(output_pdf)
```

## Temas relacionados del documento

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Crear archivos PDF en Python](/pdf/es/python-net/create-pdf-document/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)
