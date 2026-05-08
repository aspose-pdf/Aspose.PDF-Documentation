---
title: Convertir formatos de imagen a PDF en Python
linktitle: Convertir imágenes a PDF
type: docs
weight: 60
url: /es/python-net/convert-images-format-to-pdf/
lastmod: "2026-04-14"
description: Aprenda cómo convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG y otros formatos de imagen a PDF en Python con Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir imágenes a PDF en Python
Abstract: Este artículo proporciona una guía completa sobre la conversión de varios formatos de imagen a PDF usando Python, aprovechando específicamente la biblioteca Aspose.PDF for Python via .NET. El artículo cubre una variedad de formatos de imagen incluidos BMP, CGM, DICOM, EMF, GIF, PNG, SVG y TIFF. Cada sección detalla los pasos requeridos para realizar la conversión, proporcionando fragmentos de código para ilustrar el proceso. Por ejemplo, convertir BMP a PDF implica crear un nuevo documento PDF, definir la ubicación de la imagen, insertar la imagen y guardar el documento. De manera similar, para formatos como CGM, DICOM y otros, se describen opciones de carga específicas y pasos de procesamiento. El artículo también destaca las ventajas de usar Aspose.PDF para estas tareas, como su compatibilidad con diferentes métodos de codificación y la capacidad de procesar imágenes tanto de un solo fotograma como de varios fotogramas.
---

## Conversiones relacionadas

- [Convertir PDF a formatos de imagen](/pdf/es/python-net/convert-pdf-to-images-format/) cuando necesites el flujo de trabajo inverso.
- [Convertir HTML a PDF](/pdf/es/python-net/convert-html-to-pdf/) para contenido web y fuentes MHTML.
- [Convertir otros formatos de archivo a PDF](/pdf/es/python-net/convert-other-files-to-pdf/) para EPUB, XPS, texto y otras entradas que no sean imágenes.

## Conversiones de Imágenes a PDF con Python

**Aspose.PDF for Python via .NET** permite convertir diferentes formatos de imágenes a archivos PDF. Nuestra biblioteca muestra fragmentos de código para convertir los formatos de imagen más populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG y formatos TIFF.

## Convertir BMP a PDF

Convertir archivos BMP a documento PDF usando la biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> Las imágenes son archivos con extensión. BMP representa archivos de imagen Bitmap que se utilizan para almacenar imágenes digitales de mapa de bits. Estas imágenes son independientes del adaptador gráfico y también se denominan formato de mapa de bits independiente del dispositivo (DIB).

Puedes convertir archivos BMP a PDF con Aspose.PDF for Python via .NET API. Por lo tanto, puedes seguir los siguientes pasos para convertir imágenes BMP:

Pasos para convertir BMP a PDF en Python:

1. Crea un documento PDF vacío.
1. Cree la página que necesite, por ejemplo, creamos A4, pero puede especificar su propio formato.
1. Coloca la imagen (del archivo de entrada) dentro de la página usando el rectángulo definido.
1. Guarda el documento como PDF.

Así, el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir BMP a PDF en línea**

Aspose le presenta la aplicación en línea ["BMP a PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión BMP a PDF usando App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM a PDF

Convertir un CGM (Computer Graphics Metafile) a PDF (u otro formato compatible) usando Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> es una extensión de archivo para un formato Computer Graphics Metafile que se usa comúnmente en CAD (diseño asistido por computadora) y aplicaciones de gráficos de presentación. CGM es un formato de gráficos vectoriales que admite tres métodos de codificación diferentes: binario (el mejor para la velocidad de lectura del programa), basado en caracteres (produce el archivo de menor tamaño y permite transferencias de datos más rápidas) o codificación en texto claro (permite a los usuarios leer y modificar el archivo con un editor de texto).

Revise el siguiente fragmento de código para convertir archivos CGM al formato PDF.

Pasos para convertir CGM a PDF en Python:

1. Definir rutas de archivo
1. Establecer opciones de carga para CGM.
1. Convertir CGM a PDF
1. Mensaje de Conversión de Impresión

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir DICOM a PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format es el estándar de la industria médica para la creación, almacenamiento, transmisión y visualización de imágenes médicas digitales y documentos de pacientes examinados.

**Aspose.PDF for Python** le permite convertir imágenes DICOM y SVG, pero por razones técnicas, al agregar imágenes necesita especificar el tipo de archivo que se añadirá al PDF.

El siguiente fragmento de código muestra cómo convertir archivos DICOM al formato PDF con Aspose.PDF. Debe cargar la imagen DICOM, colocar la imagen en una página de un archivo PDF y guardar la salida como PDF. Utilizamos la biblioteca adicional pydicom para establecer las dimensiones de esta imagen. Si desea posicionar la imagen en la página, puede omitir este fragmento de código.

1. Cargar el archivo DICOM.
1. Extraer dimensiones de la imagen.
1. Imprimir tamaño de imagen.
1. Crea un nuevo documento PDF.
1. Prepare la imagen DICOM para PDF.
1. Establecer el tamaño de página y los márgenes del PDF.
1. Añade la imagen a la página.
1. Guarda el PDF.
1. Mensaje de conversión de impresión.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir DICOM a PDF en línea**

Aspose le presenta la aplicación en línea ["DICOM a PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de DICOM a PDF con la aplicación Aspose.PDF](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF a PDF

<abbr title="Enhanced metafile format">EMF</abbr> almacena imágenes gráficas de forma independiente del dispositivo. Los metaficheros EMF están compuestos por registros de longitud variable en orden cronológico que pueden renderizar la imagen almacenada después de analizarla en cualquier dispositivo de salida.

El siguiente fragmento de código muestra cómo convertir un EMF a PDF con Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir EMF a PDF en línea**

Aspose le presenta la aplicación en línea ["EMF a PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de EMF a PDF usando App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir GIF a PDF

Convertir archivos GIF a documento PDF usando la biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> es capaz de almacenar datos comprimidos sin pérdida de calidad en un formato de no más de 256 colores. El formato GIF independiente del hardware se desarrolló en 1987 (GIF87a) por CompuServe para transmitir imágenes bitmap a través de redes.

Así, el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir GIF a PDF en línea**

Aspose le presenta la aplicación en línea ["GIF a PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión GIF a PDF usando la aplicación](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Convertir PNG a PDF

**Aspose.PDF for Python via .NET** soporte la función para convertir imágenes PNG a formato PDF. Verifique el siguiente fragmento de código para realizar su tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen raster que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puede convertir PNG a PDF usando los pasos a continuación:

1. Crear un nuevo documento PDF.
1. Definir colocación de la imagen.
1. Guarda el PDF.
1. Mensaje de conversión de impresión.

Además, el fragmento de código a continuación muestra cómo convertir PNG a PDF con Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PNG a PDF en línea**

Aspose le presenta la aplicación en línea ["PNG a PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión PNG a PDF usando App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG a PDF

**Aspose.PDF for Python via .NET** explica cómo convertir imágenes SVG al formato PDF y cómo obtener las dimensiones del archivo SVG de origen.

Scalable Vector Graphics (SVG) es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el World Wide Web Consortium (W3C) desde 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> las imágenes y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscadas, indexadas, scriptadas y, si es necesario, comprimidas. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

{{% alert color="success" %}}
**Intenta convertir el formato SVG a PDF en línea**

Aspose.PDF for Python via .NET te presenta una aplicación en línea ["SVG a PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de SVG a PDF con App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso de convertir un archivo SVG al formato PDF con Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir TIFF a PDF

**Aspose.PDF** formato de archivo compatible, ya sea una imagen TIFF de un solo fotograma o de varios fotogramas. Significa que puedes convertir la imagen TIFF a PDF.

TIFF o TIF, Tagged Image File Format, representa imágenes raster que están destinadas a usarse en una variedad de dispositivos que cumplen con este estándar de formato de archivo. La imagen TIFF puede contener varios fotogramas con diferentes imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea una imagen TIFF de un solo fotograma o de varios fotogramas.

Puede convertir TIFF a PDF de la misma manera que el resto de formatos de archivos raster gráficos:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir CDR a PDF

El siguiente fragmento de código muestra cómo cargar un archivo CorelDRAW (CDR) y guardarlo como PDF usando 'CdrLoadOptions' en Aspose.PDF for Python via .NET.

1. Cree 'CdrLoadOptions()' para configurar cómo se debe cargar el archivo CDR.
1. Inicializa un objeto Document con el archivo CDR y las opciones de carga.
1. Guarde el documento como un PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir JPEG a PDF

Este ejemplo muestra cómo convertir JPEG a archivo PDF usando Aspose.PDF for Python via .NET.

1. Crea un nuevo documento PDF.
1. Añade una nueva página.
1. Defina el rectángulo de ubicación (tamaño A4: 595x842 puntos).
1. Inserte la imagen en la página.
1. Guarda el PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
