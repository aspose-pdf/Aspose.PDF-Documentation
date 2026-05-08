---
title: Convertir PDF a HTML en Python
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /es/python-net/convert-pdf-to-html/
lastmod: "2026-04-14"
description: Aprenda cómo convertir PDF a HTML en Python con Aspose.PDF for Python via .NET, incluyendo salida de varias páginas, imágenes externas, manejo de SVG y renderizado de HTML en capas.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a HTML en Python
Abstract: Este artículo ofrece una guía completa sobre la conversión de archivos PDF a HTML usando Python, específicamente a través de la biblioteca Aspose.PDF for Python via .NET. Describe los pasos necesarios para lograr esta conversión programáticamente, resaltando la creación de un objeto `Document` a partir del PDF de origen y el uso de `HtmlSaveOptions` para guardar el documento en formato HTML. El artículo incluye un fragmento de código Python conciso que demuestra el proceso de conversión. Además, presenta una herramienta en línea, la aplicación "PDF a HTML" de Aspose.PDF, para que los usuarios exploren la funcionalidad y la calidad de la conversión. El artículo está estructurado para abarcar varios temas relacionados, garantizando una comprensión profunda del uso de Python para la conversión de PDF a HTML.
---

## Convertir PDF a HTML

**Aspose.PDF for Python via .NET** proporciona muchas funcionalidades para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo explica cómo convertir un archivo PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Puedes usar solo un par de líneas de código Python para convertir PDF a HTML. Es posible que necesites convertir PDF a HTML si deseas crear un sitio web o añadir contenido a un foro en línea. Una forma de convertir PDF a HTML es usar Python de forma programática.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a HTML con App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Pasos: Convertir PDF a HTML en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Guárdalo en [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversiones relacionadas

- [Convertir HTML a PDF](/pdf/es/python-net/convert-html-to-pdf/) cuando necesitas el flujo de trabajo inverso de web a documento.
- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) si la salida de documento editable es más útil que HTML.
- [Convertir PDF a formatos de imagen](/pdf/es/python-net/convert-pdf-to-images-format/) para escenarios de exportación raster.

### Convertir PDF a HTML guardando imágenes en la carpeta especificada

Esta función convierte un archivo PDF a formato HTML usando Aspose.PDF for Python via .NET. Todas las imágenes extraídas se almacenan en una carpeta especificada en lugar de incrustarse en el archivo HTML.

1. Configura las opciones de guardado de HTML.
1. Guardar como HTML con imágenes externas.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML multipágina

Esta función convierte un archivo PDF en HTML de varias páginas, donde cada página del PDF se exporta como un archivo HTML separado. Esto hace que la salida sea más fácil de navegar y reduce el tiempo de carga para PDFs grandes.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y establece `split_into_pages`.
1. Guarde el documento como HTML con las páginas divididas en archivos separados.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML guardando las imágenes SVG en la carpeta especificada

Esta función convierte un PDF a formato HTML mientras almacena todas las imágenes como archivos SVG en una carpeta especificada, en lugar de incrustarlas directamente en el HTML.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y establece `special_folder_for_svg_images' en la carpeta de destino.
1. Guarde el documento como HTML con imágenes SVG externas.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML y guardar imágenes SVG comprimidas

Este fragmento convierte un PDF al formato HTML, almacenando todas las imágenes como archivos SVG en una carpeta especificada y comprimiéndolas para reducir el tamaño del archivo.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y:
   - Establezca 'special_folder_for_svg_images' para almacenar imágenes SVG externamente.
   - Habilitar 'compress_svg_graphics_if_any' para comprimir imágenes SVG.
1. Guarde el documento como HTML con imágenes SVG externas comprimidas.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con control de imágenes raster incrustadas

Este fragmento convierte un PDF a formato HTML, incrustando imágenes raster como fondos de página PNG. Este enfoque preserva la calidad de la imagen y el diseño de la página dentro del HTML.

1. Cargue el documento PDF usando 'ap.Document'.
1. Cree "HtmlSaveOptions" y establezca "raster_images_saving_mode" a "AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND".
1. Guarde el documento como HTML con imágenes raster incrustadas.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a página HTML solo con el contenido del cuerpo

Esta función convierte un PDF al formato HTML, generando contenido 'body-only' sin etiquetas adicionales 'html' o 'head', y divide la salida en páginas separadas.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y configura:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' para generar solo el contenido del 'body'.
   - 'split_into_pages' para crear archivos HTML separados para cada página de PDF.
1. Guarde el documento como HTML con las opciones especificadas.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con renderizado de texto transparente

Esta función convierte un PDF a formato HTML, renderizando todo el texto como transparente, incluidos los textos con sombra, lo que conserva la fidelidad visual mientras permite un estilo flexible en el HTML de salida.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y configura:
    - 'save_transparent_texts' para renderizar texto normal como transparente.
    - 'save_shadowed_texts_as_transparent_texts' para renderizar texto sombreado como transparente.
1. Guarde el documento como HTML con renderizado de texto transparente.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con renderizado de capas de documento

Esta función convierte un PDF al formato HTML, preservando las capas del documento al convertir el contenido marcado en capas separadas en el HTML de salida. Esto permite que los elementos en capas (como anotaciones, fondos y superposiciones) se rendericen con precisión.

1. Cargue el documento PDF usando 'ap.Document'.
1. Cree 'HtmlSaveOptions' y habilite 'convert_marked_content_to_layers' para preservar capas.
1. Guarde el documento como HTML con contenido en capas.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

