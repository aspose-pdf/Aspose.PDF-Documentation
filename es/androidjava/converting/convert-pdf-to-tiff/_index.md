---
title: Convertir PDF a TIFF 
linktitle: Convertir PDF a TIFF  
type: docs
weight: 30
url: /es/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: Este artículo describe cómo convertir páginas en un documento PDF en una imagen TIFF. Aprenderás cómo convertir todas o una sola página a imágenes TIFF con Aspose.PDF para Android a través de Android a través de Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android a través de Java** hace posible convertir páginas PDF a imágenes TIFF.

La [clase TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) te permite convertir páginas PDF a imágenes TIFF. Esta clase proporciona un método llamado Process que te permite convertir todas las páginas en un archivo PDF a una sola imagen TIFF.

{{% alert color="primary" %}}

Prueba en línea. Puedes verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convertir Páginas de PDF a Una Imagen TIFF

Aspose.PDF para Android a través de Java explica cómo convertir todas las páginas de un archivo PDF en una única imagen TIFF:

1. Crear un objeto de la clase Document.
1. Llamar al método Process para convertir el documento.
1. Para establecer las propiedades del archivo de salida, usar la clase TiffSettings.

El siguiente fragmento de código muestra cómo convertir todas las páginas del PDF en una sola imagen TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Crear objeto Resolution
        Resolution resolution = new Resolution(300);

        // Crear objeto TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Crear dispositivo TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convertir una página particular y guardar la imagen en el stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir una Página a Imagen TIFF

Aspose.PDF para Android a través de Java permite convertir una página particular en un archivo PDF a una imagen TIFF, utilizando una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF al formato TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


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
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convertir una página particular y guardar la imagen en el flujo
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## Utilizar el algoritmo de Bradley durante la conversión

Aspose.PDF para Android a través de Java ha estado soportando la función de convertir PDF a TIFF usando compresión LZW y luego con el uso de AForge, se puede aplicar binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral usando Otsu, por lo que también les gustaría usar Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //No implementado en Aspose.PDF para Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //No implementado en Aspose.PDF para Android
        throw new NotImplementedException();
    }
```