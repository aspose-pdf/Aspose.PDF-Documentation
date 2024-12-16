---
title: Convertir PDF a BMP 
linktitle: Convertir PDF a BMP
type: docs
weight: 40
url: /es/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: Este artículo describe cómo convertir páginas de PDF a imágenes BMP, convertir todas las páginas a imágenes BMP y convertir una sola página de PDF a imagen BMP con Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

La clase [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) te permite convertir páginas de PDF a imágenes <abbr title="Archivo de Imagen Bitmap">BMP</abbr>. Esta clase proporciona un método llamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que te permite convertir una página particular del archivo PDF al formato de imagen Bmp.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

La clase BmpDevice te permite convertir páginas de PDF a imágenes BMP.
 Esta clase proporciona un método llamado process(..) que te permite convertir una página específica del archivo PDF a imagen BMP.

## Convertir una Página de PDF a Imagen BMP

Para convertir una página de PDF a una imagen BMP:

1. Crea un objeto de la clase Document, para obtener la página específica que deseas convertir.
2. Llama al método process(..) para convertir la página a BMP.

El siguiente fragmento de código te muestra cómo convertir una página específica a imagen BMP.

```java
//Convertir PDF a BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Crear objeto de flujo para guardar la imagen de salida
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Crear objeto Resolution
            Resolution resolution = new Resolution(300);

            // Crear objeto BmpDevice con resolución específica
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convertir una página específica y guardar la imagen en el flujo
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Cerrar el flujo
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Convertir Todas las Páginas de PDF a Imágenes BMP

Para convertir todas las páginas de un archivo PDF a formato BMP, necesitas iterar para obtener cada página individual y convertirla a formato BMP. El siguiente fragmento de código te muestra cómo recorrer todas las páginas de un archivo PDF y convertirlas a BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Recorre todas las páginas del archivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crea un objeto de flujo para guardar la imagen de salida
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crea un objeto Resolution
            Resolution resolution = new Resolution(300);
            // Crea un objeto BmpDevice con una resolución particular
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convierte una página particular y guarda la imagen en el flujo
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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


## Convertir una región particular de la página a Imagen (DOM)

Podemos convertir documentos PDF a diferentes formatos de imagen utilizando objetos de dispositivos de imagen de Aspose.PDF. Sin embargo, a veces hay un requisito para convertir una región particular de la página en formato de imagen. Podemos cumplir con este requisito en dos pasos. Inicialmente recortar la página PDF a la región deseada y luego convertirla en imagen utilizando el objeto de dispositivo de imagen deseado.

El siguiente fragmento de código te muestra cómo convertir páginas PDF a imágenes.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // guardar el documento recortado en un flujo
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir el documento PDF recortado desde el flujo y convertirlo a imagen
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Crear objeto de Resolución
        Resolution resolution = new Resolution(300);
        // Crear dispositivo BMP con atributos especificados
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convertir una página particular y guardar la imagen en un flujo
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```