---
title: Agregar sellos de imagen en PDF usando Python
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: /es/python-net/image-stamps-in-pdf-page/
description: Agregue el sello de imagen en su documento PDF usando la clase ImageStamp con la biblioteca Aspose.PDF para Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar sellos de imagen en PDF usando Python
Abstract: Este artículo proporciona una guía completa sobre cómo agregar sellos de imagen a archivos PDF usando la biblioteca Aspose.PDF para Python. Detalla el uso de la clase `ImageStamp`, que permite la personalización de sellos basados en imágenes, incluidas propiedades como altura, ancho, opacidad y rotación. El proceso implica crear un objeto `Document` y un objeto `ImageStamp` con las propiedades deseadas, y luego agregar el sello a una página específica del PDF usando el método `add_stamp()`. El artículo incluye fragmentos de código Python que demuestran cómo aplicar un sello de imagen a un PDF y controlar su calidad usando la propiedad `quality`, que ajusta la calidad de la imagen en términos de porcentaje. Además, el artículo explica cómo usar sellos de imagen como fondos en cajas flotantes con la clase `FloatingBox`, proporcionando otro ejemplo de código para mostrar cómo se puede implementar. Esta guía sirve como un recurso útil para desarrolladores que desean mejorar los PDFs con sellos de imagen usando Aspose.PDF.
---

## Agregar sello de imagen en archivo PDF

Puede usar la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para agregar un sello de imagen a un archivo PDF. La clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) proporciona las propiedades necesarias para crear un sello basado en imágenes, como altura, ancho, opacidad, etc. El sello puede posicionarse, redimensionarse, rotarse y hacerse parcialmente transparente, lo que permite la marca de agua, la marca corporativa o anotaciones.

El siguiente fragmento de código muestra cómo agregar un sello de imagen en el archivo PDF.

1. Cargue el PDF usando 'ap.Document()'.
1. Cree un sello de imagen con 'ImageStamp()'.
1. Configure las propiedades del sello.
1. Agregue el sello a la página de destino.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

## Controlar la calidad de la imagen al agregar el sello

Al agregar una imagen como objeto de sello, puede controlar la calidad de la imagen. La propiedad [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) de la clase [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) se usa para este fin. Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).
Al establecer la propiedad quality, puede reducir la resolución de la imagen para optimizar el tamaño del PDF o mantener una mayor fidelidad para una mayor claridad.

1. Abra el documento PDF.
1. Cree un sello de imagen.
1. Establezca la calidad de la imagen.
1. Agregue el sello a la página de destino.
1. Guarde el PDF modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Sello de imagen como fondo en caja flotante

Cree una [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) en un PDF y aplique una imagen como su fondo. También muestra cómo agregar texto, establecer bordes, color de fondo y posicionar la caja con precisión en la página. Esto es útil para crear contenido PDF visualmente rico, como notas, pancartas o secciones destacadas con texto sobre imágenes.

1. Abra o cree un documento PDF.
1. Cree un objeto 'FloatingBox'.
1. Añada contenido de texto a la caja.
1. Establezca el borde de la caja y el color de fondo.
1. Añada una imagen de fondo.
1. Añada el FloatingBox a la página.
1. Guarde el documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
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


