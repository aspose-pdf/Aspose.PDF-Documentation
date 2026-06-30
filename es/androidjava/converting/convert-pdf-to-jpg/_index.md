---
title: Convertir PDF a JPG
linktitle: Convertir PDF a JPG
type: docs
weight: 10
url: /es/androidjava/convert-pdf-to-jpg/
description:  Esta página describe cómo convertir páginas PDF a imagen JPEG, convertir todas y una sola página a imágenes JPEG con Aspose.PDF for Android via Java.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir páginas PDF a imágenes JPG

La clase JpegDevice le permite convertir páginas PDF a imágenes JPEG. Esta clase proporciona un método llamado process(..) que le permite convertir una página específica del archivo PDF a una imagen JPEG.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Convertir una sola página de PDF a imagen JPG

Aspose.PDF for Android via Java le permite convertir una sola página al formato Jpeg.

Para convertir solo una página a una imagen JPEG:

1. Cree un objeto de la clase Document para obtener la página que desea convertir.
1. Llame al método process(..) para convertir la página a una imagen JPEG.

El siguiente fragmento de código muestra los pasos para convertir la primera página del PDF al formato Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convertir todas las páginas PDF a imagen JPG

Aspose.PDF for Android via Java le permite convertir todas las páginas de un archivo PDF en imágenes:

1. Recorra todas las páginas del archivo.
1. Convierta cada página individualmente:
    - Cree un objeto de la clase Document para cargar el documento PDF.
    - Obtenga la página que desea convertir.
    - Llame al método Process para convertir la página a Jpeg.

El siguiente fragmento de código le muestra cómo convertir todas las páginas PDF a imágenes Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
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
            JpegDevice JpegDevice = new JpegDevice(resolution);

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

## Convertir página PDF particular a imagen JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
