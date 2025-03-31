---
title: Convertir PDF a Diferentes Formatos de Imagen en C#
linktitle: Convertir PDF a Imágenes
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Este tema te muestra cómo usar Aspose.PDF para convertir PDF a varios formatos de imagen, por ejemplo, TIFF, BMP, EMF, JPEG, PNG, GIF, SVG con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Different Image Formats in C#",
    "alternativeHeadline": "Convert PDF Files to Multiple Image Formats in C#",
    "abstract": "La función en Aspose.PDF for .NET permite a los usuarios convertir sin problemas archivos PDF en múltiples formatos de imagen como TIFF, BMP, EMF, JPEG, PNG, GIF y SVG. Esta funcionalidad simplifica el manejo de documentos al permitir la conversión con solo unas pocas líneas de código C#, lo que la convierte en una herramienta esencial para los desarrolladores que buscan mejorar sus aplicaciones con capacidades versátiles de procesamiento de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2012",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-images-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-images-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Resumen

Este artículo explica cómo convertir PDF a diferentes formatos de imagen usando C#. Cubre los siguientes temas.

_Formato de Imagen_: **TIFF**
- [C# PDF a TIFF](#csharp-pdf-to-tiff)
- [C# Convertir PDF a TIFF](#csharp-pdf-to-tiff)
- [C# Convertir Páginas Únicas o Particulares de PDF a TIFF](#csharp-pdf-to-tiff-pages)

_Formato de Imagen_: **BMP**
- [C# PDF a BMP](#csharp-pdf-to-bmp)
- [C# Convertir PDF a BMP](#csharp-pdf-to-bmp)
- [C# Convertidor de PDF a BMP](#csharp-pdf-to-bmp)

_Formato de Imagen_: **EMF**
- [C# PDF a EMF](#csharp-pdf-to-emf)
- [C# Convertir PDF a EMF](#csharp-pdf-to-emf)
- [C# Convertidor de PDF a EMF](#csharp-pdf-to-emf)

_Formato de Imagen_: **JPG**
- [C# PDF a JPG](#csharp-pdf-to-jpg)
- [C# Convertir PDF a JPG](#csharp-pdf-to-jpg)
- [C# Convertidor de PDF a JPG](#csharp-pdf-to-jpg)

_Formato de Imagen_: **PNG**
- [C# PDF a PNG](#csharp-pdf-to-png)
- [C# Convertir PDF a PNG](#csharp-pdf-to-png)
- [C# Convertidor de PDF a PNG](#csharp-pdf-to-png)

_Formato de Imagen_: **GIF**
- [C# PDF a GIF](#csharp-pdf-to-gif)
- [C# Convertir PDF a GIF](#csharp-pdf-to-gif)
- [C# Convertidor de PDF a GIF](#csharp-pdf-to-gif)

_Formato de Imagen_: **SVG**
- [C# PDF a SVG](#csharp-pdf-to-svg)
- [C# Convertir PDF a SVG](#csharp-pdf-to-svg)
- [C# Convertidor de PDF a SVG](#csharp-pdf-to-svg)

## C# Convertir PDF a Imagen

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

**Aspose.PDF for .NET** utiliza varios enfoques para convertir PDF a imagen. En términos generales, utilizamos dos enfoques: conversión utilizando el enfoque de Dispositivo y conversión utilizando SaveOption. Esta sección te mostrará cómo convertir documentos PDF a formatos de imagen como BMP, JPEG, GIF, PNG, EMF, TIFF y SVG utilizando uno de esos enfoques.

Hay varias clases en la biblioteca que te permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado a la conversión de todo el documento, pero ImageDevice - para una página particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF for .NET** hace posible convertir páginas PDF a imágenes TIFF.

La clase TiffDevice (basada en DocumentDevice) permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado `Process` que te permite convertir todas las páginas de un archivo PDF a una sola imagen TIFF.

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a TIFF con Aplicación Gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir Páginas PDF a Una Imagen TIFF

Aspose.PDF for .NET explica cómo convertir todas las páginas en un archivo PDF a una sola imagen TIFF:

<a name="csharp-pdf-to-tiff"><strong>Pasos: Convertir PDF a TIFF en C#</strong></a>

1. Crea un objeto de la clase **Document**.
2. Crea objetos **TiffSettings** y **TiffDevice**.
3. Llama al método **TiffDevice.Process()** para convertir el documento PDF a TIFF.
4. Para establecer las propiedades del archivo de salida, utiliza la clase **TiffSettings**.

El siguiente fragmento de código muestra cómo convertir todas las páginas PDF a una sola imagen TIFF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTIFF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTIFF.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
            SkipBlankPages = false
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, dataDir + "PDFtoTIFF_out.tif");
    }
}
```

### Convertir Una Página a Imagen TIFF

Aspose.PDF for .NET permite convertir una página particular en un archivo PDF a una imagen TIFF, utiliza una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF a formato TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Pasos: Convertir Páginas Únicas o Particulares de PDF a TIFF en C#</strong></a>

1. Crea un objeto de la clase **Document**.
2. Crea objetos **TiffSettings** y **TiffDevice**.
3. Llama al método sobrecargado **TiffDevice.Process()** con los parámetros **fromPage** y **toPage** para convertir las páginas del documento PDF a TIFF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffSinglePage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffSinglePage.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, 1, 1, dataDir + "PDFtoTiffSinglePage_out.tif");
    }
}
```

### Usar el algoritmo de Bradley durante la conversión

Aspose.PDF for .NET ha estado apoyando la función de convertir PDF a TIF utilizando compresión LZW y luego, con el uso de AForge, se puede aplicar la Binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral utilizando Otsu, por lo que también les gustaría usar Bradley.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffBradleyBinarization()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffBradleyBinarization.pdf"))
    {
        string outputImageFile = dataDir + "PDFtoTiffBradleyBinarization_out.tif";
        string outputBinImageFile = dataDir + "PDFtoTiffBradleyBinarization-bin_out.tif";

        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.LZW,
            Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, outputImageFile);

        // Binarize the image using Bradley method
        using (var inStream = new FileStream(outputImageFile, FileMode.Open))
        {
            using (var outStream = new FileStream(outputBinImageFile, FileMode.Create))
            {
                tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
            }
        }
    }
}
```

## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/bmpdevice) permite convertir páginas PDF a imágenes <abbr title="Bitmap Image File">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/emfdevice) permite convertir páginas PDF a imágenes <abbr title="Enhanced Meta File">EMF</abbr>.
- La clase [JpegDevice](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/jpegdevice) permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/pngdevice) permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.
- La clase [GifDevice](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/gifdevice) permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Veamos cómo convertir una página PDF a una imagen.

La clase `BmpDevice` proporciona un método llamado [Process](https://reference.aspose.com/pdf/es/net/aspose.pdf.devices/bmpdevice/methods/process) que permite convertir una página particular del archivo PDF a formato de imagen BMP. Las otras clases tienen el mismo método. Así que, si necesitamos convertir una página PDF a una imagen, simplemente instanciamos la clase requerida.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Los siguientes pasos y el fragmento de código en C# muestran esta posibilidad
 
 - [Convertir PDF a BMP en C#](#csharp-pdf-to-image)
 - [Convertir PDF a EMF en C#](#csharp-pdf-to-image)
 - [Convertir PDF a JPG en C#](#csharp-pdf-to-image)
 - [Convertir PDF a PNG en C#](#csharp-pdf-to-image)
 - [Convertir PDF a GIF en C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Pasos: PDF a Imagen (BMP, EMF, JPG, PNG, GIF) en C#</strong></a>

1. Carga el archivo PDF utilizando la clase **Document**.
2. Crea una instancia de la subclase de **ImageDevice**, es decir,
   * **BmpDevice** (para convertir PDF a BMP).
   * **EmfDevice** (para convertir PDF a Emf).
   * **JpegDevice** (para convertir PDF a JPG).
   * **PngDevice** (para convertir PDF a PNG).
   * **GifDevice** (para convertir PDF a GIF).
3. Llama al método **ImageDevice.Process()** para realizar la conversión de PDF a Imagen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFusingImageDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create Resolution object            
    var resolution = new Aspose.Pdf.Devices.Resolution(300);
    var bmpDevice = new Aspose.Pdf.Devices.BmpDevice(resolution);
    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(resolution);
    var gifDevice = new Aspose.Pdf.Devices.GifDevice(resolution);
    var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);
    var emfDevice = new Aspose.Pdf.Devices.EmfDevice(resolution);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        ConvertPDFtoImage(bmpDevice, "bmp", document, dataDir);
        ConvertPDFtoImage(jpegDevice, "jpeg", document, dataDir);
        ConvertPDFtoImage(gifDevice, "gif", document, dataDir);
        ConvertPDFtoImage(pngDevice, "png", document, dataDir);
        ConvertPDFtoImage(emfDevice, "emf", document, dataDir);
    }
}

private static void ConvertPDFtoImage(ImageDevice imageDevice,
        string ext, Document document, var dataDir)
{
    for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
    {
        using (FileStream imageStream =
            new FileStream($"{dataDir}image{pageCount}_out.{ext}",
            FileMode.Create))
        {
            // Convert a particular page and save the image to stream
            imageDevice.Process(document.Pages[pageCount], imageStream);
        }
    }
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como un ejemplo de cómo funcionan nuestras aplicaciones gratuitas, consulta la siguiente función.

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando Aplicación Gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Scalable Vector Graphics">SVG</abbr> usando C# y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PDF a SVG con Aplicación Gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscadas, indexadas, guionizadas y, si es necesario, comprimidas. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

Aspose.PDF for .NET admite la función de convertir imágenes SVG a formato PDF y también ofrece la capacidad de convertir archivos PDF a formato SVG. Para lograr este requisito, se ha introducido la clase [`SvgSaveOptions`](https://reference.aspose.com/pdf/es/net/aspose.pdf/svgsaveoptions/methods/index) en el espacio de nombres Aspose.PDF. Instancia un objeto de SvgSaveOptions y pásalo como segundo argumento al método [`Document.Save(..)`](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/methods/save/index) para convertir el documento PDF a SVG.

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF a formato SVG con .NET.

<a name="csharp-pdf-to-svg"><strong>Pasos: Convertir PDF a SVG en C#</strong></a>

1. Crea un objeto de la clase **Document**.
2. Crea un objeto **SvgSaveOptions** con la configuración necesaria.
3. Llama al método **Document.Save()** y pásale el objeto **SvgSaveOptions** para convertir el documento PDF a SVG.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoSVG.pdf"))
    {
        // Instantiate an object of SvgSaveOptions
        var saveOptions = new Aspose.Pdf.SvgSaveOptions
        {
            // Do not compress SVG image to Zip archive
            CompressOutputToZipArchive = false,
            TreatTargetFileNameAsDirectory = true                
        };

        // Save SVG file
        document.Save(dataDir + "PDFToSVG_out.svg", saveOptions);
    }
}
```