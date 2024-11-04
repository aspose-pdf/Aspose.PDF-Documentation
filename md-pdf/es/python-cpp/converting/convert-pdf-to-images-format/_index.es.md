---
title: Convertir PDF a Diferentes Formatos de Imagen en Python
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: /python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: Este tema le muestra cómo usar Aspose.PDF para Python para convertir PDF a varios formatos de imágenes, por ejemplo, TIFF, BMP, EMF, JPEG, PNG, GIF, SVG con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visión General

Este artículo explica cómo convertir PDF a diferentes formatos de imagen usando Python. Cubre los siguientes temas.

## Python Convertir PDF a Imagen

### Python Convertir PDF a PNG

1. Importe el módulo AsposePdfPython, que proporciona un contenedor de Python para la biblioteca Aspose.PDF.
1. Abra un documento PDF usando la función `document_open`, que toma el nombre del archivo como argumento y devuelve un objeto Document.
1. Obtenga las páginas del documento usando la función `document_get_pages`, que toma un objeto Document como argumento y devuelve un objeto PageCollection.

1. Obtén la página deseada del documento usando la función `page_collection_get_page`, que toma un objeto PageCollection y un índice como argumentos y devuelve un objeto Page.
1. Crea un objeto PngDevice usando la función `png_device_create`, que no toma argumentos. Este objeto puede convertir páginas PDF a imágenes PNG con parámetros predeterminados.
1. Guarda la página deseada del documento como una imagen PNG usando la función `png_device_save_page_to_file`, que toma un objeto PngDevice, un objeto Page y un nombre de archivo como argumentos.
1. Cierra los manejadores de los objetos PngDevice y Document usando la función close_handle, que toma un objeto como argumento y libera sus recursos.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Convertir PDF a JPEG

1. Abra un documento PDF usando la función `document_open`, que toma el nombre del archivo como argumento y devuelve un objeto Document.
1. Obtenga las páginas del documento usando la función `document_get_pages`, que toma un objeto Document como argumento y devuelve un objeto PageCollection.
1. Obtenga la página deseada del documento usando la función `page_collection_get_page`, que toma un objeto PageCollection y un índice como argumentos y devuelve un objeto Page.
1. Cree un objeto Resolution usando la función `resolution_create`, que toma el valor de resolución en puntos por pulgada (DPI) como argumento.
1. Cree un objeto JpegDevice usando la función `jpeg_device_create_from_width_height_resolution`, que toma los valores de ancho, alto y resolución como argumentos. Este objeto puede convertir páginas PDF a imágenes JPEG con los parámetros especificados.

1. Guarda la página deseada del documento como una imagen JPEG usando la función `jpeg_device_save_page_to_file`, que toma un objeto JpegDevice, un objeto Page y un nombre de archivo como argumentos.
1. Cierra los manejadores de los objetos JpegDevice y Document usando la función `close_handle`, que toma un objeto como argumento y libera sus recursos.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```