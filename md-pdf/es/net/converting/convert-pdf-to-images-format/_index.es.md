---
title: Convertir PDF a Diferentes Formatos de Imagen en C#
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Este tema te muestra cómo usar Aspose.PDF para convertir PDF a varios formatos de imágenes como TIFF, BMP, EMF, JPEG, PNG, GIF, SVG con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visión General

Este artículo explica cómo convertir PDF a diferentes formatos de imagen usando C#. Cubre los siguientes temas.

_Formato de Imagen_: **TIFF**
- [C# PDF a TIFF](#csharp-pdf-to-tiff)
- [C# Convertir PDF a TIFF](#csharp-pdf-to-tiff)
- [C# Convertir Páginas Individuales o Específicas de PDF a TIFF](#csharp-pdf-to-tiff-pages)

_Formato de Imagen_: **BMP**
- [C# PDF a BMP](#csharp-pdf-to-bmp)
- [C# Convertir PDF a BMP](#csharp-pdf-to-bmp)
- [C# Conversor de PDF a BMP](#csharp-pdf-to-bmp)

_Formato de Imagen_: **EMF**
- [C# PDF a EMF](#csharp-pdf-to-emf)
- [C# Convertir PDF a EMF](#csharp-pdf-to-emf)
- [C# Conversor de PDF a EMF](#csharp-pdf-to-emf)
- [Conversor de PDF a EMF en C#](#csharp-pdf-to-emf)

_Formato de Imagen_: **JPG**
- [C# PDF a JPG](#csharp-pdf-to-jpg)
- [C# Convertir PDF a JPG](#csharp-pdf-to-jpg)
- [Conversor de PDF a JPG en C#](#csharp-pdf-to-jpg)

_Formato de Imagen_: **PNG**
- [C# PDF a PNG](#csharp-pdf-to-png)
- [C# Convertir PDF a PNG](#csharp-pdf-to-png)
- [Conversor de PDF a PNG en C#](#csharp-pdf-to-png)

_Formato de Imagen_: **GIF**
- [C# PDF a GIF](#csharp-pdf-to-gif)
- [C# Convertir PDF a GIF](#csharp-pdf-to-gif)
- [Conversor de PDF a GIF en C#](#csharp-pdf-to-gif)

_Formato de Imagen_: **SVG**
- [C# PDF a SVG](#csharp-pdf-to-svg)
- [C# Convertir PDF a SVG](#csharp-pdf-to-svg)
- [Conversor de PDF a SVG en C#](#csharp-pdf-to-svg)

## C# Convertir PDF a Imagen

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF para .NET** utiliza varios enfoques para convertir un PDF a imagen.
**Aspose.PDF para .NET** utiliza varios enfoques para convertir PDF a imagen.

Hay varias clases en la biblioteca que permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado para la conversión de todo el documento, pero ImageDevice - para una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF para .NET** hace posible convertir páginas PDF a imágenes TIFF.

La clase TiffDevice (basada en DocumentDevice) te permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado `Process` que te permite convertir todas las páginas en un archivo PDF a una sola imagen TIFF.

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes probar a investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a TIFF con aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir páginas de PDF a una imagen TIFF

Aspose.PDF para .NET explica cómo convertir todas las páginas de un archivo PDF en una única imagen TIFF:

<a name="csharp-pdf-to-tiff"><strong>Pasos: Convertir PDF a TIFF en C#</strong></a>

1. Crear un objeto de la clase **Document**.
2. Crear objetos **TiffSettings** y **TiffDevice**.
3. Llamar al método **TiffDevice.Process()** para convertir el documento PDF a TIFF.
4. Para establecer las propiedades del archivo de salida, usar la clase **TiffSettings**.

El siguiente fragmento de código muestra cómo convertir todas las páginas del PDF en una única imagen TIFF.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Crear objeto Resolution
    Resolution resolution = new Resolution(300);

    // Crear objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Crear dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convertir una página en particular y guardar la imagen en stream
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### Convertir una página a imagen TIFF

Aspose.PDF para .NET permite convertir una página específica de un archivo PDF a imagen TIFF, utiliza una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF a formato TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Pasos: Convertir Páginas Individuales o Específicas de PDF a TIFF en C#</strong></a>

1. Crear un objeto de la clase **Document**.
2. Crear objetos **TiffSettings** y **TiffDevice**
3. Llamar al método sobrecargado **TiffDevice.Process()** con los parámetros **fromPage** y **toPage** para convertir las páginas del documento PDF a TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Crear objeto Resolution
    Resolution resolution = new Resolution(300);

    // Crear objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Crear dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Convertir una página específica y guardar la imagen en stream
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Utiliza el algoritmo de Bradley durante la conversión

Aspose.PDF para .NET ha estado soportando la función de convertir PDF a TIF usando compresión LZW y luego con el uso de AForge, se puede aplicar la Binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral usando Otsu, por lo que también les gustaría usar Bradley.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // Abrir documento
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Crear objeto Resolution
    Resolution resolution = new Resolution(300);
    // Crear objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Crear dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Convertir una página en particular y guardar la imagen en stream
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) te permite convertir páginas PDF a imágenes <abbr title="Bitmap Image File">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) te permite convertir páginas PDF a imágenes <abbr title="Enhanced Meta File">EMF</abbr>.
- La clase [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) te permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) te permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.
- La clase [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) te permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos a ver cómo convertir una página de PDF a una imagen.
Vamos a ver cómo convertir una página de PDF en una imagen.

La clase `BmpDevice` proporciona un método llamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que permite convertir una página específica del archivo PDF al formato de imagen BMP. Las otras clases tienen el mismo método. Por lo tanto, si necesitamos convertir una página de PDF a una imagen, simplemente instanciamos la clase requerida.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

Los siguientes pasos y fragmento de código en C# muestran esta posibilidad

 - [Convertir PDF a BMP en C#](#csharp-pdf-to-image)
 - [Convertir PDF a EMF en C#](#csharp-pdf-to-image)
 - [Convertir PDF a JPG en C#](#csharp-pdf-to-image)
 - [Convertir PDF a PNG en C#](#csharp-pdf-to-image)
 - [Convertir PDF a GIF en C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Pasos: PDF a Imagen (BMP, EMF, JPG, PNG, GIF) en C#</strong></a>

1.
1.
2. Crea una instancia de una subclase de **ImageDevice**, es decir:
   * **BmpDevice** (para convertir PDF a BMP)
   * **EmfDevice** (para convertir PDF a Emf)
   * **JpegDevice** (para convertir PDF a JPG)
   * **PngDevice** (para convertir PDF a PNG)
   * **GifDevice** (para convertir PDF a GIF)
3. Llama al método **ImageDevice.Process()** para realizar la conversión de PDF a imagen.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Crear objeto Resolution            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // Convertir una página en particular y guardar la imagen en el stream
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Cerrar stream
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como un ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF utilizando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Gráficos Vectoriales Escalables">SVG</abbr> usando C# y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**
{{% /alert %}}
Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a SVG con aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
[![Conversión de Aspose.PDF de PDF a SVG con aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha sido desarrollado por el Consorcio World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, scriptados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, aunque a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

Aspose.PDF para .NET soporta la característica de convertir imágenes SVG a formato PDF y también ofrece la capacidad de convertir archivos PDF a formato SVG.
Aspose.PDF para .NET soporta la funcionalidad de convertir imágenes SVG a formato PDF y también ofrece la capacidad de convertir archivos PDF a formato SVG.

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF a formato SVG con .NET.

<a name="csharp-pdf-to-svg"><strong>Pasos: Convertir PDF a SVG en C#</strong></a>

1. Crear un objeto de la clase **Document**.
2. Crear un objeto **SvgSaveOptions** con las configuraciones necesarias.
3. Llamar al método **Document.Save()** y pasarle el objeto **SvgSaveOptions** para convertir el documento PDF a SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // Cargar documento PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // Instanciar un objeto de SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // No comprimir la imagen SVG en archivo Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Guardar la salida en archivos SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

