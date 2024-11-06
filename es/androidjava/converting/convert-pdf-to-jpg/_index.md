---
title: Convertir PDF a JPG 
linktitle: Convertir PDF a JPG
type: docs
weight: 10
url: es/androidjava/convert-pdf-to-jpg/
description: Esta página describe cómo convertir Páginas PDF a imagen JPEG, convertir todas y únicas páginas a imágenes JPEG con Aspose.PDF para Android a través de Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir Páginas PDF a Imágenes JPG

La clase JpegDevice te permite convertir páginas PDF a imágenes JPEG. Esta clase proporciona un método llamado process(..) que te permite convertir una página particular del archivo PDF a imagen JPEG.

{{% alert color="primary" %}}

Prueba en línea. Puedes verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Convertir una sola página PDF a imagen JPG

Aspose.PDF para Android a través de Java te permite convertir una sola página a formato Jpeg.

Para convertir solo una página a una imagen JPEG:

1. Cree un objeto de la clase Document para obtener la página que desea convertir.
1. Llame al método process(..) para convertir la página a una imagen JPEG.

El siguiente fragmento de código muestra los pasos para convertir la primera página de PDF a formato Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Crear objeto de flujo para guardar la imagen de salida
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Crear objeto Resolution
            Resolution resolution = new Resolution(300);

            // Crear objeto JpegDevice con una resolución particular
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convertir una página particular y guardar la imagen en el flujo
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Cerrar el flujo
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir todas las páginas PDF a imagen JPG

Aspose.PDF para Android a través de Java te permite convertir todas las páginas de un archivo PDF a imágenes:

1. Recorre todas las páginas del archivo.
1. Convierte cada página individualmente:
    - Crea un objeto de la clase Document para cargar el documento PDF.
    - Obtén la página que deseas convertir.
    - Llama al método Process para convertir la página a Jpeg.

El siguiente fragmento de código te muestra cómo convertir todas las páginas de un PDF a imágenes Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Recorre todas las páginas del archivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crea un objeto de flujo para guardar la imagen de salida
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crea un objeto de Resolución
            Resolution resolution = new Resolution(300);
            // Crea un objeto JpegDevice con una resolución particular
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convierte una página particular y guarda la imagen en el flujo
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Cierra el flujo
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


## Convertir una página particular de PDF a imagen JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtener el rectángulo de una región particular de la página
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // establecer el valor de CropBox según el rectángulo de la región deseada de la página
        document.getPages().get_Item(1).setCropBox(pageRect);
        // guardar el documento recortado en el flujo
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir el documento PDF recortado desde el flujo y convertirlo a imagen
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Crear objeto de Resolución
        Resolution resolution = new Resolution(300);
        // Crear dispositivo Jpeg con atributos especificados
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convertir una página particular y guardar la imagen en el flujo
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```