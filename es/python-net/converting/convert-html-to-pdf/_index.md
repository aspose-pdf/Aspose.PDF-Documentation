---
title: Convertir HTML a PDF en Python
linktitle: Convertir HTML a archivo PDF
type: docs
weight: 40
url: /es/python-net/convert-html-to-pdf/
lastmod: "2026-04-14"
description: Aprenda cómo convertir HTML y MHTML a PDF en Python con Aspose.PDF for Python via .NET, incluidos los ajustes de medios CSS, fuentes incrustadas y salida de PDF etiquetado.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Cómo convertir HTML a PDF en Python con Aspose.PDF
Abstract: Este artículo explica cómo convertir archivos HTML y MHTML a PDF utilizando Aspose.PDF for Python via .NET. Cubre el flujo de trabajo básico de HTML-to-PDF y muestra cómo controlar la renderización con tipos de medios, prioridad de reglas de página CSS, fuentes incrustadas, salida de una sola página y generación de estructura lógica para PDFs etiquetados accesibles.
---

## Conversión de HTML a PDF con Python

**Aspose.PDF for Python via .NET** le permite convertir documentos HTML existentes a PDF con opciones de renderizado flexibles. Puede ajustar finamente cómo se genera la salida para que coincida con sus requisitos de diseño, estilo, accesibilidad y archivado.

## Convertir HTML a PDF

El siguiente ejemplo de Python muestra el flujo de trabajo básico para convertir un documento HTML a PDF.

1. Crear una instancia de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) clase.
1. Inicializar un [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el archivo HTML de origen.
1. Guarde el documento PDF de salida llamando `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Conversiones relacionadas

- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) cuando necesites una salida preparada para la web a partir de archivos PDF existentes.
- [Convertir otros formatos de archivo a PDF](/pdf/es/python-net/convert-other-files-to-pdf/) para flujos de conversión de EPUB, XPS, texto y PostScript.
- [Convertir imágenes a PDF](/pdf/es/python-net/convert-images-format-to-pdf/) cuando su contenido de origen se basa en imágenes en lugar de marcado HTML.

{{% alert color="success" %}}
**Intenta convertir HTML a PDF en línea**

Aspose presenta la aplicación gratuita en línea ["HTML a PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puedes probar la calidad de la conversión y la salida.

[![Aspose.PDF Conversión HTML a PDF usando la aplicación gratuita](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Convertir HTML a PDF usando tipo de medio

Este ejemplo muestra cómo convertir un archivo HTML a PDF usando opciones de renderizado específicas.

1. Crear una instancia de [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) clase.
1. Establecer `html_media_type` para aplicar reglas CSS destinadas a diseños de pantalla o de impresión, como `HtmlMediaType.SCREEN` o `HtmlMediaType.PRINT`.
1. Cargar el HTML en un `ap.Document` usando las opciones de carga.
1. Guarde el documento como un PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Prioriza el CSS `@page` regla durante la conversión de HTML a PDF

Algunos documentos usan [el `@page` regla](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) para el diseño de página. Si esos estilos entran en conflicto con otras configuraciones, puedes controlar la prioridad con `is_priority_css_page_rule`.

1. Crear una instancia de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) clase.
1. Establecer `is_priority_css_page_rule = False` para permitir que otros estilos tengan precedencia sobre `@page` reglas.
1. Cargar el HTML en un `ap.Document` con las opciones configuradas.
1. Guarde el documento como un PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Convertir HTML a PDF con fuentes incrustadas

Este ejemplo muestra cómo convertir un archivo HTML a PDF mientras se incrustan fuentes. Si necesita que el PDF de salida preserve la tipografía original de manera más fiable, establezca `is_embed_fonts` a `True`.

1. Crear `HtmlLoadOptions()` para configurar la conversión de HTML a PDF.
1. Establecer `is_embed_fonts = True` para incrustar las fuentes utilizadas en el HTML directamente en el PDF.
1. Cargar el HTML en un `ap.Document` con estas opciones.
1. Guarde el documento como un PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Renderizar contenido HTML en una sola página PDF

Este ejemplo demuestra cómo convertir un archivo HTML en un PDF de una sola página usando Aspose.PDF for Python via .NET. Utilice el `is_render_to_single_page` propiedad cuando deseas que todo el contenido HTML se renderice en una sola página continua.

1. Crear una instancia de `HtmlLoadOptions()` para configurar el proceso de conversión.
1. Activar `is_render_to_single_page` para renderizar todo el contenido HTML en una sola página.
1. Cargue el documento con las opciones configuradas en un `ap.Document`.
1. Guarde el resultado como un archivo PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Crear estructura lógica a partir de etiquetas HTML

La estructura lógica, también llamada Tagged PDF, conserva la jerarquía semántica del HTML original, como encabezados, párrafos y listas. Esto hace que el PDF resultante sea más accesible, buscable y adecuado para flujos de trabajo de documentos estructurados.

Al habilitar la estructura lógica durante la conversión, el DOM HTML se mapea en un árbol de etiquetas PDF en lugar de renderizarse solo como contenido visual.

Para cumplir con los requisitos de accesibilidad, un PDF debe incluir elementos de estructura lógica que definan el orden de lectura, proporcionen texto alternativo para lectores de pantalla y preserven la jerarquía del contenido.

> La calidad de la estructura lógica en el PDF de salida depende directamente de la calidad del marcado HTML original. Un HTML mal estructurado o no válido puede resultar en un etiquetado incompleto o inexacto en el PDF convertido.

1. Cree una instancia de HtmlLoadOptions para controlar cómo se convierte el HTML.
1. Activar el etiquetado semántico para que el PDF contenga elementos estructurados.
1. Abra el archivo HTML utilizando las opciones configuradas.
1. Guarde el PDF estructurado.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## Convertir MHTML a PDF

Este ejemplo muestra cómo convertir un archivo MHT o MHTML en un documento PDF utilizando Aspose.PDF for Python via .NET con dimensiones de página específicas.

1. Crear una instancia de `ap.MhtLoadOptions()` para configurar el procesamiento de archivos MHTML.
1. Establezca varios parámetros, como el tamaño de página.
1. Inicialice el documento con el archivo de entrada y las opciones de carga configuradas.
1. Guarde el documento resultante como un PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
