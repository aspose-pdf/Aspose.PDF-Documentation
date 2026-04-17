---
title: Convertir PDF a HTML en Python
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Este tema le muestra cómo convertir un archivo PDF al formato HTML con la biblioteca Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Cómo convertir PDF a HTML en Python
Abstract: Este artículo ofrece una guía completa sobre cómo convertir archivos PDF a HTML usando Python, específicamente a través de la librería Aspose.PDF for Python via .NET. Describe los pasos necesarios para lograr esta conversión programáticamente, destacando la creación de un objeto `Document` a partir del PDF de origen y el uso de `HtmlSaveOptions` para guardar el documento en formato HTML. El artículo incluye un fragmento de código Python conciso que demuestra el proceso de conversión. Además, presenta una herramienta en línea, la aplicación "PDF to HTML" de Aspose.PDF, para que los usuarios exploren la funcionalidad y la calidad de la conversión. El artículo está estructurado para abordar diversos temas relacionados, garantizando una comprensión profunda del uso de Python para la conversión de PDF a HTML.
---

## Convertir PDF a HTML

**Aspose.PDF for Python via .NET** proporciona muchas funciones para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo explica cómo convertir un archivo PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Puedes usar solo un par de líneas de código Python para convertir PDF a HTML. Puede que necesites convertir PDF a HTML si deseas crear un sitio web o agregar contenido a un foro en línea. Una forma de convertir PDF a HTML es usar Python programáticamente.

{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a HTML con Aplicación Gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Pasos: Convertir PDF a HTML en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Guárdalo en [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) al llamar [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML guardando las imágenes en la carpeta especificada

Esta función convierte un archivo PDF a formato HTML utilizando Aspose.PDF for Python via .NET. Todas las imágenes extraídas se almacenan en una carpeta especificada en lugar de incrustarse en el archivo HTML.

1. Configurar opciones de guardado HTML.
1. Guardar como HTML con imágenes externas.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_all_images = self.data_dir
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML multipágina

Esta función convierte un archivo PDF en HTML multipágina, donde cada página del PDF se exporta como un archivo HTML separado. Esto hace que la salida sea más fácil de navegar y reduce el tiempo de carga para PDFs grandes.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y 'establezca split_into_pages'.
1. Guarde el documento como HTML con las páginas divididas en archivos separados.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.split_into_pages = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML guardando imágenes SVG en una carpeta especificada

Esta función convierte un PDF a formato HTML mientras almacena todas las imágenes como archivos SVG en una carpeta especificada, en lugar de incrustarlas directamente en el HTML.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y 'set special_folder_for_svg_images' en la carpeta de destino.
1. Guarde el documento como HTML con imágenes SVG externas.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_svg_images = self.data_dir
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML y guardar imágenes SVG comprimidas

Este fragmento convierte un PDF a formato HTML, almacenando todas las imágenes como archivos SVG en una carpeta especificada y comprimiéndolas para reducir el tamaño del archivo.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y:
   - Establezca 'special_folder_for_svg_images' para almacenar imágenes SVG externamente.
   - Habilite 'compress_svg_graphics_if_any' para comprimir imágenes SVG.
1. Guarde el documento como HTML con imágenes SVG externas comprimidas.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_svg_images = self.data_dir
save_options.compress_svg_graphics_if_any = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con control de imágenes ráster incrustadas

Este fragmento convierte un PDF al formato HTML, incrustando imágenes raster como fondos de página PNG. Este enfoque preserva la calidad de la imagen y el diseño de la página dentro del HTML.

1. Cargue el documento PDF usando 'ap.Document'.
1. Cree 'HtmlSaveOptions' y 'set raster_images_saving_mode' a 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Guarde el documento como HTML con imágenes raster incrustadas.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a página HTML de contenido solo del cuerpo

Esta función convierte un PDF a formato HTML, generando contenido 'solo cuerpo' sin etiquetas adicionales 'html' o 'head', y divide la salida en páginas separadas.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y configurar:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' para generar solo el contenido del 'body'.
   - 'split_into_pages' para crear archivos HTML separados para cada página PDF.
1. Guarde el documento como HTML con las opciones especificadas.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.html_markup_generation_mode = (
    apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
)
save_options.split_into_pages = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con renderizado de texto transparente

Esta función convierte un PDF a formato HTML, renderizando todo el texto como transparente, incluidos los textos con sombra, lo que preserva la fidelidad visual mientras permite una estilización flexible en el HTML de salida.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y configurar:
    - 'save_transparent_texts' para renderizar texto normal como transparente.
    - 'save_shadowed_texts_as_transparent_texts' para renderizar texto sombreado como transparente.
1. Guarda el documento como HTML con renderizado de texto transparente.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.save_transparent_texts = True
save_options.save_shadowed_texts_as_transparent_texts = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con renderizado de capas de documento

Esta función convierte un PDF a formato HTML, preservando las capas del documento al convertir el contenido marcado en capas separadas en el HTML de salida. Esto permite que los elementos en capas (como anotaciones, fondos y superposiciones) se representen con precisión.

1. Cargue el documento PDF usando 'ap.Document'.
1. Crea 'HtmlSaveOptions' y habilita 'convert_marked_content_to_layers' para preservar capas.
1. Guarda el documento como HTML con contenido en capas.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.convert_marked_content_to_layers = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

