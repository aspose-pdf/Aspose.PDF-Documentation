---
title: Convertir PDF a BMP
linktitle: Convertir PDF a BMP
type: docs
weight: 40
url: /es/androidjava/convert-pdf-to-bmp/
lastmod: "2026-06-30"
description: Este artículo describe cómo convertir páginas de PDF a imagen BMP, convertir todas las páginas a imágenes BMP y convertir una sola página de PDF a imagen BMP con Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) la clase le permite convertir páginas PDF a <abbr title="Bitmap Image File">BMP</abbr> imágenes. Esta clase proporciona un método llamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que permite convertir una página concreta del archivo PDF al formato de imagen Bmp.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

La clase BmpDevice te permite convertir páginas PDF a imágenes BMP. Esta clase proporciona un método llamado process(..) que permite convertir una página concreta del archivo PDF a una imagen BMP.

## Convertir una página PDF a imagen BMP

Para convertir una página PDF a una imagen BMP:

1. Cree un objeto de la clase Document, para obtener la página específica que desea convertir.
1. Llame al método process(..) para convertir la página a BMP.

El siguiente fragmento de código le muestra cómo convertir una página concreta a imagen BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Convertir todas las páginas PDF a imágenes BMP

Para convertir todas las páginas de un archivo PDF a formato BMP, necesita iterar para obtener cada página individual y convertirla a formato BMP. El siguiente fragmento de código le muestra cómo recorrer todas las páginas de un archivo PDF y convertirlas a BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## Convertir una región particular de la página a Imagen (DOM)

Podemos convertir documentos PDF a diferentes formatos de Imagen utilizando objetos de dispositivos de imagen de Aspose.PDF. Sin embargo, a veces hay un requisito de convertir una región particular de la página a formato de Imagen. Podemos cumplir con este requisito en dos pasos. Inicialmente recortamos la página PDF a la región deseada y luego la convertimos a imagen utilizando el objeto de dispositivo de Imagen deseado.

El siguiente fragmento de código le muestra cómo convertir páginas PDF a imágenes.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
