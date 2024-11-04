---
title: Convertir PDF a formatos de Imágenes
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir PDF a varios formatos de imágenes. Convierte páginas PDF a imágenes PNG, JPEG, BMP con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** te permite convertir documentos PDF a formatos de imagen como BMP, JPEG, GIF, PNG, EMF, TIFF y SVG utilizando dos enfoques. La conversión se realiza usando Device y usando SaveOption.

Hay varias clases en la biblioteca que te permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado para la conversión de todo el documento, pero ImageDevice - para una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF for Java** hace posible convertir páginas PDF a imágenes TIFF.

La [clase TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) te permite convertir páginas PDF a imágenes TIFF.
 Esta clase proporciona un método llamado Process que te permite convertir todas las páginas de un archivo PDF a una sola imagen TIFF.

### Convertir Páginas de PDF a Una Imagen TIFF

Aspose.PDF para Java explica cómo convertir todas las páginas de un archivo PDF a una sola imagen TIFF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Llama al método [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) para convertir el documento.
1. Para establecer las propiedades del archivo de salida, usa la clase [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

El siguiente fragmento de código muestra cómo convertir todas las páginas de PDF a una sola imagen TIFF.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Crear objeto Resolution
Resolution resolution = new Resolution(300);

// Crear objeto TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// Crear dispositivo TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Convertir una página en particular y guardar la imagen en el stream
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### Convertir una Sola Página a Imagen TIFF

Aspose.PDF para Java permite convertir una página particular en un archivo PDF a una imagen TIFF, utilizando una versión sobrecargada del método Process(..) que toma como argumento un número de página para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF al formato TIFF.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// Crear objeto Resolution
Resolution resolution = new Resolution(300);

// Crear objeto TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// Crear dispositivo TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Convertir una página particular y guardar la imagen en el flujo
tiffDevice.process(document, 1, 1, tiffFileName);
```


### Usar el algoritmo de Bradley durante la conversión

Aspose.PDF para Java ha estado soportando la función de convertir PDF a TIFF usando la compresión LZW y luego, con el uso de AForge, se puede aplicar la Binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral usando Otsu, por lo que también les gustaría usar Bradley.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Crear objeto Resolution
Resolution resolution = new Resolution(300);
// Crear objeto TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// Crear dispositivo TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// Convertir una página particular y guardar la imagen en el flujo
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// Crear objeto de flujo para guardar la imagen de salida
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### Convertir Páginas PDF a Imágenes TIFF Pixeladas

Para convertir todas las páginas de un archivo PDF al formato TIFF Pixelado, use la opción Pixelated de IndexedConversionType

```java
// Convertir Páginas PDF a Imágenes TIFF Pixeladas
// Para convertir todas las páginas de un archivo PDF al formato TIFF Pixelado, use la opción Pixelated
// de IndexedConversionType.

// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Crear objeto de flujo para guardar la imagen de salida
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// Crear objeto Resolution
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// instanciar objeto TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// establecer la compresión de la imagen TIFF resultante
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// establecer la profundidad de color para la imagen resultante
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// omitir páginas en blanco al renderizar PDF a TIFF
tiffSettings.setSkipBlankPages(true);
// establecer el brillo de la imagen
tiffSettings.setBrightness(.5f);

// establecer el Tipo de Conversión Indexada, el valor predeterminado es simple
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// Crear objeto TiffDevice con una resolución particular
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// Convertir una página en particular (Página 1) y guardar la imagen en el flujo
tiffDevice.process(document, 1, 1, imageStream);

// Cerrar el flujo
imageStream.close();
```


{{% alert color="success" %}}
**Intente convertir PDF a TIFF en línea**

Aspose.PDF para Java le presenta la aplicación gratuita en línea ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puede intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a TIFF con aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) le permite convertir páginas PDF a imágenes <abbr title="Archivo de Imagen Bitmap">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) le permite convertir páginas PDF a imágenes <abbr title="Archivo Meta Mejorado">EMF</abbr>.

- La clase [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) le permite convertir páginas PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) te permite convertir páginas PDF a imágenes <abbr title="Portable Network Graphics">PNG</abbr>.
- La clase [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) te permite convertir páginas PDF a imágenes <abbr title="Graphics Interchange Format">GIF</abbr>.

Veamos cómo convertir una página PDF a una imagen.

La clase [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) proporciona un método llamado [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) que te permite convertir una página particular del archivo PDF al formato de imagen BMP. Las otras clases tienen el mismo método. Así que, si necesitamos convertir una página PDF a una imagen, simplemente instanciamos la clase requerida.

El siguiente fragmento de código muestra esta posibilidad:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF a Imagen.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Crear objeto Resolution
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // Convertir una página particular y guardar la imagen en el stream
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Cerrar el stream
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Cómo convertir PDF a PNG usando la App Gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Gráficos Vectoriales Escalables">SVG</abbr> usando Java y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a SVG con la App Gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio de la World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, programados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG se pueden crear y editar con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

### Convertir páginas PDF a imágenes SVG

Aspose.PDF para Java soporta la función de convertir archivos PDF al formato SVG.
 Para cumplir con este requisito, la clase [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) ha sido introducida en el paquete com.aspose.pdf. Instancie un objeto de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) y páselo como segundo argumento al método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF al formato SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF a SVG.
 */
public class ConvertPDFtoSVG {
    // La ruta al directorio de documentos.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // Cargar documento PDF
        Document document = new Document(pdfFileName);

        // Instanciar un objeto de SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // No comprimir la imagen SVG en un archivo Zip
        saveOptions.setCompressOutputToZipArchive(false);

        // Guardar la salida en archivos SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```