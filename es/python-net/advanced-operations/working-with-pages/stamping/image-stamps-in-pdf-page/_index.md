---
title: Agregar Image Stamps a PDF en Python
linktitle: Image stamps en archivo PDF
type: docs
weight: 10
url: /es/python-net/image-stamps-in-pdf-page/
description: Aprende cómo agregar image stamps a páginas PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar Image stamps en PDF usando Python
Abstract: Este artículo ofrece una guía completa sobre cómo agregar sellos de imagen a archivos PDF utilizando la biblioteca Aspose.PDF para Python. Detalla el uso de la clase `ImageStamp`, que permite la personalización de sellos basados en imágenes, incluyendo propiedades como altura, ancho, opacidad y rotación. El proceso implica crear un objeto `Document` y un objeto `ImageStamp` con las propiedades deseadas, y luego agregar el sello a una página específica del PDF mediante el método `add_stamp()`. El artículo incluye fragmentos de código Python que demuestran cómo aplicar un sello de imagen a un PDF y controlar su calidad usando la propiedad `quality`, que ajusta la calidad de la imagen en términos porcentuales. Además, el artículo explica cómo usar los sellos de imagen como fondos en cajas flotantes con la clase `FloatingBox`, proporcionando otro ejemplo de código para mostrar cómo se puede implementar. Esta guía sirve como un recurso útil para los desarrolladores que buscan mejorar los PDFs con sellos de imagen usando Aspose.PDF.
---

## Agregar sello de imagen en archivo PDF

Puedes usar el [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) clase para agregar un sello de imagen a un archivo PDF. El [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) La clase proporciona las propiedades necesarias para crear un sello basado en imagen, como altura, anchura, opacidad, etc. El sello puede ser posicionado, redimensionado, rotado y hecho parcialmente transparente, lo que permite marcas de agua, branding o anotaciones.

El siguiente fragmento de código muestra cómo agregar un sello de imagen en el archivo PDF.

1. Cargue el PDF usando 'ap.Document()'.
1. Cree un sello de imagen con 'ImageStamp()'.
1. Configura las propiedades del sello.
1. Agregue el sello a la página de destino.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Controlar la calidad de la imagen al añadir la marca

Al agregar una imagen como objeto de sello, puede controlar la calidad de la imagen. El [calidad](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) propiedad del [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) clase se utiliza para este propósito. Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).
Al establecer la propiedad quality, puedes reducir la resolución de la imagen para optimizar el tamaño del PDF o mantener una mayor fidelidad para una mejor claridad.

1. Abra el documento PDF.
1. Crear una marca de imagen.
1. Establecer la calidad de la imagen.
1. Agregue el sello a la página de destino.
1. Guardar el PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Image Stamp como fondo en Floating Box

Cree un [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) en un PDF y aplicar una imagen como su fondo. También muestra cómo agregar texto, establecer bordes, color de fondo y posicionar la caja precisamente en la página. Esto es útil para crear contenido PDF visualmente rico, como llamados, banners o secciones resaltadas con texto sobre imágenes.

1. Abra o cree un documento PDF.
1. Cree un objeto 'FloatingBox'.
1. Agregue contenido de texto al cuadro.
1. Establezca el borde y el color de fondo del cuadro.
1. Agregar una imagen de fondo.
1. Agregar el FloatingBox a la página.
1. Guarde el documento PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```

## Temas relacionados con el estampado

- [Estampar páginas PDF en Python](/pdf/es/python-net/stamping/)
- [Agregar sellos de página al PDF en Python](/pdf/es/python-net/page-stamps-in-the-pdf-file/)
- [Agregar sellos de texto al PDF en Python](/pdf/es/python-net/text-stamps-in-the-pdf-file/)
- [Agregar números de página al PDF en Python](/pdf/es/python-net/add-page-number/)