---
title: Convertir PDF a Diferentes Formatos de Imagen en Python
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: /python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: Este tema le muestra cómo usar Aspose.PDF para Python para convertir PDF a varios formatos de imágenes, por ejemplo, TIFF, BMP, EMF, JPEG, PNG, GIF, SVG con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visión General

Este artículo explica cómo convertir PDF a diferentes formatos de imagen usando Python. Cubre los siguientes temas.

_Formato de Imagen_: **TIFF**
- [Python PDF a TIFF](#python-pdf-to-tiff)
- [Python Convertir PDF a TIFF](#python-pdf-to-tiff)
- [Python Convertir Páginas Únicas o Particulares de PDF a TIFF](#python-pdf-to-tiff-pages)


_Formato de Imagen_: **BMP**
- [Python PDF a BMP](#python-pdf-to-bmp)
- [Python Convertir PDF a BMP](#python-pdf-to-bmp)
- [Python Convertidor de PDF a BMP](#python-pdf-to-bmp)

_Formato de Imagen_: **EMF**
- [Python PDF a EMF](#python-pdf-to-emf)

- [Python Convertir PDF a EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_Formato de Imagen_: **JPG**
- [Python PDF a JPG](#python-pdf-to-jpg)
- [Python Convertir PDF a JPG](#python-pdf-to-jpg)
- [Python PDF a Convertidor JPG](#python-pdf-to-jpg)

_Formato de Imagen_: **PNG**
- [Python PDF a PNG](#python-pdf-to-png)
- [Python Convertir PDF a PNG](#python-pdf-to-png)
- [Python PDF a Convertidor PNG](#python-pdf-to-png)

_Formato de Imagen_: **GIF**
- [Python PDF a GIF](#python-pdf-to-gif)
- [Python Convertir PDF a GIF](#python-pdf-to-gif)
- [Python PDF a Convertidor GIF](#python-pdf-to-gif)

_Formato de Imagen_: **SVG**
- [Python PDF a SVG](#python-pdf-to-svg)
- [Python Convertir PDF a SVG](#python-pdf-to-svg)
- [Python PDF a Convertidor SVG](#python-pdf-to-svg)

## Python Convertir PDF a Imagen

**Aspose.PDF para Python** utiliza varios enfoques para convertir PDF a imagen.
 Generalmente hablando, usamos dos enfoques: conversión usando el enfoque de Dispositivo y conversión usando SaveOption. Esta sección te mostrará cómo convertir documentos PDF a formatos de imagen como BMP, JPEG, GIF, PNG, EMF, TIFF y SVG usando uno de esos enfoques.

Hay varias clases en la biblioteca que te permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado a la conversión de todo el documento, pero ImageDevice - para una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF para Python** hace posible convertir páginas de PDF a imágenes TIFF.

La clase [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (basada en DocumentDevice) te permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) que te permite convertir todas las páginas en un archivo PDF a una sola imagen TIFF.

{{% alert color="success" %}}

**Intenta convertir PDF a TIFF en línea**
Aspose.PDF para Python a través de .NET te presenta la aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a TIFF con Aplicación Gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir Páginas de PDF a Una Imagen TIFF

Aspose.PDF para Python explica cómo convertir todas las páginas en un archivo PDF a una sola imagen TIFF:

<a name="csharp-pdf-to-tiff"><strong>Pasos: Convertir PDF a TIFF en Python</strong></a>

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Crear objetos [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) y [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)

3. Llama al método [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) para convertir el documento PDF a TIFF.  
4. Para establecer las propiedades del archivo de salida, utiliza la clase [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).

El siguiente fragmento de código muestra cómo convertir todas las páginas del PDF en una sola imagen TIFF.

```python
from asposepdf import Api, Device

# inicializar licencia
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Abrir documento PDF
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# Abrir documento PDF
document = Api.Document(input_pdf)
# Crear objeto Resolution
resolution = Device.Resolution(300)

# Crear objeto TiffSettings
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# Crear dispositivo TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# Convertir una página en particular y guardar la imagen en el flujo
tiffDevice.process(document, output_image)
```


## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) te permite convertir páginas PDF a imágenes <abbr title="Bitmap Image File">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) te permite convertir páginas PDF a imágenes <abbr title="Enhanced Meta File">EMF</abbr>.
- La clase [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) te permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) te permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.

- La clase [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) te permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Echemos un vistazo a cómo convertir una página PDF a una imagen.

La clase [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) proporciona un método llamado [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) que te permite convertir una página particular del archivo PDF al formato de imagen BMP. Las otras clases tienen el mismo método. Así que, si necesitamos convertir una página PDF a una imagen, simplemente instanciamos la clase requerida.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Los siguientes pasos y fragmento de código en Python muestran esta posibilidad
 
 - [Convertir PDF a BMP en Python](#python-pdf-to-image)
 - [Convertir PDF a EMF en Python](#python-pdf-to-image)
 - [Convertir PDF a JPG en Python](#python-pdf-to-image)
 - [Convertir PDF a PNG en Python](#python-pdf-to-image)
 - [Convertir PDF a GIF en Python](#python-pdf-to-image)


<a name="csharp-pdf-to-image"><strong>Pasos: PDF a Imagen (BMP, EMF, JPG, PNG, GIF) en Python</strong></a>

1. Cargue el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Cree una instancia de una subclase de [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/), es decir,
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (para convertir PDF a BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (para convertir PDF a Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (para convertir PDF a JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (para convertir PDF a PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (para convertir PDF a GIF)
3. Llame al método [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) para realizar la conversión de PDF a Imagen.

### Convertir PDF a BMP

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Crear objeto de resolución
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # Crear nombre de archivo para guardar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # Convertir una página particular y guardar la imagen en archivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Convertir PDF a EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Crear objeto de Resolución
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # Crear nombre de archivo para guardar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # Convertir una página en particular y guardar la imagen en el archivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### Convertir PDF a JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Crear objeto de Resolución
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # Crear nombre de archivo para guardar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # Convertir una página en particular y guardar la imagen en el archivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### Convertir PDF a PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Crear objeto de resolución
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # Crear nombre de archivo para guardar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # Convertir una página particular y guardar la imagen en el archivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### Convertir PDF a GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Abrir documento PDF
document = Api.Document(input_pdf)

# Crear objeto de resolución
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # Crear nombre de archivo para guardar
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # Convertir una página particular y guardar la imagen en el archivo
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para Python te presenta la aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Gráficos Vectoriales Escalables">SVG</abbr> usando Python y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para Python a través de .NET te presenta la aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a SVG con la aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos están definidos en archivos de texto XML. Esto significa que pueden ser buscados, indexados, programados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

Aspose.PDF para Python admite la función de convertir imágenes SVG al formato PDF y también ofrece la capacidad de convertir archivos PDF al formato SVG.
 Para cumplir con este requisito, la clase [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) ha sido introducida en el espacio de nombres Aspose.PDF. Instancie un objeto de SvgSaveOptions y páselo como segundo argumento al método [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF a formato SVG con Python.

<a name="csharp-pdf-to-svg"><strong>Pasos: Convertir PDF a SVG en Python</strong></a>

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Cree un objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) con las configuraciones necesarias.
3. Llame al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y páselo al objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) para convertir el documento PDF a SVG.

### Convertir PDF a SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```