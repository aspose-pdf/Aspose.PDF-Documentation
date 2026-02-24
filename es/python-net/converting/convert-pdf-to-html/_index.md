---
title: Convertir PDF a HTML en Python
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: /es/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Este tema le muestra cómo convertir un archivo PDF a formato HTML con la biblioteca Aspose.PDF for Python vía .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a HTML en Python
Abstract: Este artículo ofrece una guía completa sobre la conversión de archivos PDF a HTML usando Python, específicamente a través de la biblioteca Aspose.PDF for Python vía .NET. Describe los pasos necesarios para lograr esta conversión programáticamente, resaltando la creación de un objeto `Document` a partir del PDF origen y el uso de `HtmlSaveOptions` para guardar el documento en formato HTML. El artículo incluye un fragmento conciso de código Python que demuestra el proceso de conversión. Además, presenta una herramienta en línea, la aplicación "PDF a HTML" de Aspose.PDF, para que los usuarios exploren la funcionalidad y la calidad de la conversión. El artículo está estructurado para abordar varios temas relacionados, asegurando una comprensión profunda del uso de Python para la conversión de PDF a HTML.
---

## Convertir PDF a HTML

**Aspose.PDF for Python via .NET** ofrece muchas funciones para convertir diversos formatos de archivos en documentos PDF y para convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF a <abbr title="HyperText Markup Language">HTML</abbr>. Puede usar solo un par de líneas de código Python para convertir PDF a HTML. Es posible que necesite convertir PDF a HTML si desea crear un sitio web o agregar contenido a un foro en línea. Una forma de convertir PDF a HTML es usar Python programáticamente.

{{% alert color="success" %}}
**Intente convertir PDF a HTML en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a HTML con aplicación gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Pasos: Convertir PDF a HTML en Python

1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF origen.
1. Guardarlo con [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

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

### Convertir PDF a HTML guardando imágenes en la carpeta especificada

Esta función convierte un archivo PDF al formato HTML usando Aspose.PDF for Python vía .NET. Todas las imágenes extraídas se almacenan en una carpeta especificada en lugar de incrustarse en el archivo HTML.

1. Configurar las opciones de guardado HTML.
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

1. Cargar el PDF origen usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y establecer 'split_into_pages'.
1. Guardar el documento como HTML con las páginas divididas en archivos separados.
1. Imprimir un mensaje de confirmación.

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

### Convertir PDF a HTML guardando imágenes SVG en la carpeta especificada

Esta función convierte un PDF al formato HTML mientras almacena todas las imágenes como archivos SVG en una carpeta especificada, en lugar de incrustarlas directamente en el HTML.

1. Cargar el PDF origen usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y establecer 'special_folder_for_svg_images' a la carpeta de destino.
1. Guardar el documento como HTML con imágenes SVG externas.
1. Imprimir un mensaje de confirmación.

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

Este fragmento convierte un PDF al formato HTML, almacenando todas las imágenes como archivos SVG en una carpeta especificada y comprimiéndolas para reducir el tamaño del archivo.

1. Cargar el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y:
- Establecer 'special_folder_for_svg_images' para almacenar imágenes SVG externamente.
- Habilitar 'compress_svg_graphics_if_any' para comprimir imágenes SVG.
1. Guardar el documento como HTML con imágenes SVG externas comprimidas.
1. Imprimir un mensaje de confirmación.

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

### Convertir PDF a HTML con control de imágenes raster incrustadas

Este fragmento convierte un PDF al formato HTML, incrustando imágenes raster como fondos de página PNG. Este enfoque preserva la calidad de imagen y el diseño de la página dentro del HTML.

1. Cargar el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y 'set raster_images_saving_mode' a 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Guardar el documento como HTML con imágenes raster incrustadas.
1. Imprimir un mensaje de confirmación.

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

### Convertir PDF a página HTML de contenido solo cuerpo

Esta función convierte un PDF a formato HTML, generando contenido 'solo cuerpo' sin etiquetas extra 'html' o 'head', y divide la salida en páginas separadas.

1. Cargar el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y configurar:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' para generar solo el contenido 'body'.
- 'split_into_pages' para crear archivos HTML separados para cada página PDF.
1. Guardar el documento como HTML con las opciones especificadas.
1. Imprimir un mensaje de confirmación.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF a HTML con renderizado de texto transparente

Esta función convierte un PDF a formato HTML, renderizando todo el texto como transparente, incluidos los textos con sombra, lo que preserva la fidelidad visual mientras permite un estilo flexible en el HTML de salida.

1. Cargar el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y configurar:
- 'save_transparent_texts' para renderizar el texto normal como transparente.
- 'save_shadowed_texts_as_transparent_texts' para renderizar el texto con sombra como transparente.
1. Guardar el documento como HTML con renderizado de texto transparente.
1. Imprimir un mensaje de confirmación.

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

Esta función convierte un PDF a formato HTML, preservando las capas del documento al convertir el contenido marcado en capas separadas en el HTML de salida. Esto permite que los elementos en capas (como anotaciones, fondos y superposiciones) se rendericen con precisión.

1. Cargar el documento PDF usando 'ap.Document'.
1. Crear 'HtmlSaveOptions' y habilitar 'convert_marked_content_to_layers' para preservar las capas.
1. Guardar el documento como HTML con contenido en capas.
1. Imprimir un mensaje de confirmación.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


