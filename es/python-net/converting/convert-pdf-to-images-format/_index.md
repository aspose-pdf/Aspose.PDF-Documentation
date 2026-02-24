---
title: Convertir PDF a diferentes formatos de imagen en Python
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Descubra cómo convertir páginas PDF en imágenes como PNG, JPEG o TIFF usando Aspose.PDF en Python a través de .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a formatos de imagen en Python
Abstract: Este artículo ofrece una guía completa sobre cómo convertir archivos PDF a varios formatos de imagen usando Python, específicamente aprovechando la biblioteca Aspose.PDF para Python. El documento describe métodos para convertir PDF a formatos de imagen que incluyen TIFF, BMP, EMF, JPG, PNG, GIF y SVG. Se discuten dos enfoques principales de conversión el enfoque Device y SaveOption. El enfoque Device implica utilizar clases como `DocumentDevice` y `ImageDevice` para conversiones de todo el documento o de páginas específicas. Se proporcionan pasos detallados y ejemplos de código Python para convertir páginas PDF a diferentes formatos, como TIFF usando `TiffDevice`, y BMP, EMF, JPEG, PNG y GIF utilizando sus respectivas clases de dispositivo (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Para la conversión a SVG, se introduce la clase `SvgSaveOptions`. El artículo también destaca herramientas en línea para probar estas conversiones.
---

## Python Convertir PDF a Imagen

**Aspose.PDF for Python** utiliza varios enfoques para convertir PDF a imagen. En general, utilizamos dos enfoques: la conversión mediante el enfoque Device y la conversión mediante SaveOption. Esta sección le mostrará cómo convertir documentos PDF a formatos de imagen como BMP, JPEG, GIF, PNG, EMF, TIFF y SVG usando uno de esos enfoques.

Hay varias clases en la biblioteca que le permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado a la conversión de todo el documento, pero ImageDevice, a una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF for Python** hace posible convertir páginas PDF a imágenes TIFF.

La clase [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (basada en DocumentDevice) le permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) que le permite convertir todas las páginas de un archivo PDF en una única imagen TIFF.

{{% alert color="success" %}}
**Pruebe a convertir PDF a TIFF en línea**

Aspose.PDF para Python a través de .NET le presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puede probar la funcionalidad y la calidad con la que trabaja.

[![Conversión Aspose.PDF PDF a TIFF con aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir páginas PDF a una sola imagen TIFF

Aspose.PDF para Python explica cómo convertir todas las páginas de un archivo PDF en una única imagen TIFF:

Pasos: Convertir PDF a TIFF en Python

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear objetos [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) y [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Llamar al método [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) para convertir el documento PDF a TIFF.
1. Para establecer las propiedades del archivo de salida, use la clase [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

El siguiente fragmento de código muestra cómo convertir todas las páginas PDF en una única imagen TIFF.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) permite convertir páginas PDF a imágenes <abbr title="Bitmap Image File">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) permite convertir páginas PDF a imágenes <abbr title="Enhanced Meta File">EMF</abbr>.
- La clase [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.
- La clase [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Veamos cómo convertir una página PDF a una imagen.

La clase [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) proporciona un método llamado [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) que le permite convertir una página concreta del archivo PDF al formato de imagen BMP. Las demás clases tienen el mismo método. Por lo tanto, si necesitamos convertir una página PDF a una imagen, simplemente instanciamos la clase requerida.

Los siguientes pasos y fragmento de código en Python muestran esta posibilidad:

- [Convertir PDF a BMP en Python](#python-pdf-to-image)
- [Convertir PDF a EMF en Python](#python-pdf-to-image)
- [Convertir PDF a JPG en Python](#python-pdf-to-image)
- [Convertir PDF a PNG en Python](#python-pdf-to-image)
- [Convertir PDF a GIF en Python](#python-pdf-to-image)

Pasos: PDF a Imagen (BMP, EMF, JPG, PNG, GIF) en Python

1. Cargar el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear una instancia de una subclase de [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/), por ejemplo.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (para convertir PDF a BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (para convertir PDF a EMF)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (para convertir PDF a JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (para convertir PDF a PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (para convertir PDF a GIF)
1. Llama al método [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) para realizar la conversión de PDF a Imagen.

### Convertir PDF a BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF a EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Convertir PDF a JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### Convertir PDF a PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF a PNG con fuente predeterminada

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF a GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF for Python te presenta la aplicación gratuita en línea ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes probar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Scalable Vector Graphics">SVG</abbr> usando Python y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF for Python a través de .NET te presenta la aplicación gratuita en línea ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a SVG con la aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha sido desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscadas, indexadas, scriptadas y, si es necesario, comprimidas. Como archivos XML, las imágenes SVG pueden crearse y editarse con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

Aspose.PDF para Python admite la función de convertir una imagen SVG al formato PDF y también ofrece la capacidad de convertir archivos PDF al formato SVG. Para cumplir con este requisito, se ha introducido la clase [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) en el espacio de nombres Aspose.PDF. Instancia un objeto de SvgSaveOptions y pásalo como segundo argumento al método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF al formato SVG con Python.

Pasos: Convertir PDF a SVG en Python

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crea el objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) con la configuración necesaria.
1. Llama al método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pásale el objeto [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) para convertir el documento PDF a SVG.

### Convertir PDF a SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

