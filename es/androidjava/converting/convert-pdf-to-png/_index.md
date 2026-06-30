---
title: Convertir PDF a PNG
linktitle: Convertir PDF a PNG
type: docs
weight: 20
url: /es/androidjava/convert-pdf-to-png/
lastmod: "2026-06-30"
description: Esta página describe cómo convertir páginas PDF a imágenes PNG, convertir todas y páginas individuales a imágenes PNG con Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Utilice la biblioteca **Aspose.PDF for Android via Java** para convertir páginas PDF a <abbr title="Portable Network Graphics">PNG</abbr> Imágenes de forma accesible y conveniente.

La clase PngDevice le permite convertir páginas PDF a imágenes PNG. Esta clase proporciona un método llamado Process que le permite convertir una página en particular del archivo PDF al formato de imagen PNG.

## Convertir páginas PDF a imágenes PNG

Para convertir todas las páginas de un archivo PDF a archivos PNG, recorra las páginas individuales y convierta cada una al formato PNG. El siguiente fragmento de código muestra cómo recorrer todas las páginas de un archivo PDF y convertir cada una en una imagen PNG.

{{% alert color="primary" %}} 

Pruébelo en línea. Puede comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Convertir una única página PDF a imagen PNG

Pasar el índice de la página como argumento al método Process(..).
El siguiente fragmento de código muestra los pasos para convertir la primera página del PDF a formato PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convertir todas las páginas PDF a imagen PNG

Aspose.PDF for Android via Java le muestra cómo convertir todas las páginas de un archivo PDF a imágenes:

1. Recorre todas las páginas del archivo.
1. Convierte cada página individualmente:
    1. Crea un objeto de la clase Document para cargar el documento PDF.
    1. Obtén la página que deseas convertir.
    1. Llame al método Process para convertir la página a Png.

El siguiente fragmento de código le muestra cómo convertir todas las páginas PDF a imágenes PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir una página PDF específica a imagen PNG

Aspose.PDF for Android via Java le muestra cómo convertir una página específica a formato PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
