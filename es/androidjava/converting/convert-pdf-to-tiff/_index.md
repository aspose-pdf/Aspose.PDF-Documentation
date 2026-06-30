---
title: Convertir PDF a TIFF
linktitle: Convertir PDF a TIFF
type: docs
weight: 30
url: /es/androidjava/convert-pdf-to-tiff/
lastmod: "2026-06-30"
description: Este artículo describe cómo convertir páginas de un documento PDF en una imagen TIFF. Aprenderá cómo convertir todas o una sola página a imágenes TIFF con Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** hace posible convertir páginas PDF a imágenes TIFF  .

El [Clase TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) le permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado Process que le permite convertir todas las páginas de un archivo PDF en una sola imagen TIFF.

{{% alert color="primary" %}}

Pruebe en línea. Puede comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convertir páginas PDF a una sola imagen TIFF

Aspose.PDF for Android vía Java explica cómo convertir todas las páginas de un archivo PDF en una sola imagen TIFF:

1. Cree un objeto de la clase Document.
1. Llame al método Process para convertir el documento.
1. Para establecer las propiedades del archivo de salida, use la clase TiffSettings.

El siguiente fragmento de código muestra cómo convertir todas las páginas de PDF a una sola imagen TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convertir página única a imagen TIFF

Aspose.PDF for Android via Java permite convertir una página concreta de un archivo PDF a una imagen TIFF, use una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF al formato TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Usar algoritmo Bradley durante la conversión

Aspose.PDF for Android via Java ha estado soportando la función de convertir PDF a TIFF usando compresión LZW y luego, con el uso de AForge, se puede aplicar la binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesiten obtener el umbral usando Otsu, por lo que también les gustaría usar Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

