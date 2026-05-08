---
title: Convertir PDF a formatos de imagen en Python
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/python-net/convert-pdf-to-images-format/
lastmod: "2026-05-08"
description: Aprenda cómo renderizar páginas PDF como archivos TIFF, BMP, EMF, JPEG, PNG, GIF y SVG en Python con Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Convierta páginas PDF a TIFF, PNG, JPEG, GIF, BMP, EMF y SVG en Python
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de imagen comunes con Aspose.PDF for Python via .NET. Cubre la exportación de TIFF a nivel de documento con `TiffDevice`, la generación de imágenes raster por página con subclases de `ImageDevice` como `BmpDevice`, `JpegDevice`, `PngDevice`, `GifDevice` y `EmfDevice`, y la exportación vectorial a SVG con `SvgSaveOptions`. Cada sección incluye los pasos principales y ejemplos de Python necesarios para guardar el contenido PDF como salida de imagen.
---

## Convertir PDF a imágenes en Python

**Aspose.PDF for Python via .NET** admite varias formas de convertir el contenido de PDF a imágenes. En la práctica, la mayoría de los flujos de trabajo utilizan una de dos opciones:

- el enfoque Device para renderizar páginas PDF a formatos de imagen raster
- el enfoque SaveOptions para exportar contenido PDF a SVG

Este artículo muestra cómo convertir archivos PDF a TIFF, BMP, EMF, JPEG, PNG, GIF y SVG.

La biblioteca incluye múltiples clases de renderizado. `DocumentDevice` está diseñado para la conversión de todo el documento, mientras `ImageDevice` apunta a páginas individuales.

## Convertir PDF usando la clase DocumentDevice

Use `DocumentDevice` cuando desee renderizar todo el PDF en un único archivo TIFF de varias páginas.

La clase [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) se basa en `DocumentDevice` y proporciona el método [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) para convertir todas las páginas de un archivo PDF en una sola salida TIFF.

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF for Python via .NET le presenta una aplicación en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a TIFF con Aspose.PDF y App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir páginas PDF a una sola imagen TIFF

Aspose.PDF for Python via .NET puede renderizar cada página de un archivo PDF en una imagen TIFF.

Pasos: Convertir PDF a TIFF en Python

1. Cargue el PDF de origen con la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Cree los objetos [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) y [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Configure las opciones TIFF, como la compresión, la profundidad de color y el manejo de páginas en blanco.
1. Llame al método [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) para escribir el archivo TIFF.

El siguiente fragmento de código muestra cómo convertir todas las páginas del PDF en una sola imagen TIFF.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## Convertir PDF usando la clase ImageDevice

Use `ImageDevice` cuando necesite una salida página por página en un formato de imagen rasterizada.

`ImageDevice` es la clase base para `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) permite convertir páginas PDF en imágenes BMP.
- La clase [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) permite convertir páginas PDF en imágenes EMF.
- La clase [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) permite convertir páginas PDF en imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) permite convertir páginas PDF en imágenes PNG.
- La clase [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) permite convertir páginas PDF en imágenes GIF.

El flujo de trabajo es el mismo para cada formato: cargar el documento, crear el dispositivo apropiado, luego procesar la página requerida.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) expone el método [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) para renderizar una página específica como BMP. Las demás clases de `ImageDevice` siguen el mismo patrón, por lo que puede cambiar el formato cambiando la clase del dispositivo.

Los siguientes enlaces y ejemplos de código muestran cómo renderizar páginas PDF a formatos de imagen comunes:

- [Convertir PDF a BMP en Python](#convertir-pdf-a-bmp)
- [Convertir PDF a EMF en Python](#convertir-pdf-a-emf)
- [Convertir PDF a JPEG en Python](#convertir-pdf-a-jpeg)
- [Convertir PDF a PNG en Python](#convertir-pdf-a-png)
- [Convertir PDF a GIF en Python](#convertir-pdf-a-gif)

Pasos: PDF a Imagen (BMP, EMF, JPG, PNG, GIF) en Python

1. Cargue el archivo PDF con la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Cree una instancia de la subclase requerida de [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/):
    - [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (para convertir PDF a BMP)
    - [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (para convertir PDF a EMF)
    - [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (para convertir PDF a JPG)
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (para convertir PDF a PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (para convertir PDF a GIF)
1. Recorre las páginas que deseas exportar.
1. Llama al [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) método para guardar cada página como una imagen.

### Convertir PDF a BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF a EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Convertir PDF a JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF a PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Convertir PDF a PNG con fuente predeterminada

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Convertir PDF a GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones, por favor revise la siguiente característica.

Aspose.PDF for Python le presenta la aplicación en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Use `SaveOptions` cuando desee exportar contenido PDF a SVG.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF for Python via .NET le presenta una aplicación en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a SVG con App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos vectoriales escalables (SVG)** es un formato basado en XML para gráficos vectoriales bidimensionales. Debido a que SVG sigue siendo vectorial, es útil cuando necesita una salida escalable para la web, la interfaz de usuario o flujos de trabajo de diseño.

Los archivos SVG son de texto, permiten búsquedas y son fáciles de posprocesar en otras herramientas.

Aspose.PDF for Python via .NET puede convertir SVG a PDF y también exportar páginas PDF a SVG. Para la conversión de PDF a SVG, cree un objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) y páselo al método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Los siguientes pasos muestran cómo convertir un archivo PDF a SVG con Python.

Pasos: Convertir PDF a SVG en Python

1. Cargue el PDF de origen con la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Cree un objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) y configure las opciones necesarias.
1. Llame al método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) con la instancia de `SvgSaveOptions` para escribir la salida SVG.

### Convertir PDF a SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## Conversiones relacionadas

- [Convertir formatos de imagen a PDF](/pdf/es/python-net/convert-images-format-to-pdf/) cuando necesites reconstruir PDFs a partir de JPG, PNG, TIFF, SVG o de otras fuentes de imágenes.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para una salida compatible con el navegador en lugar de imágenes raster.
- [Convertir PDF a otros formatos](/pdf/es/python-net/convert-pdf-to-other-files/) para flujos de trabajo de exportación de EPUB, Markdown, texto y XPS.
