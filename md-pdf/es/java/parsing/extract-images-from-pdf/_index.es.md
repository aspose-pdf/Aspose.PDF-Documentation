---
title: Extraer Imágenes de PDF 
linktitle: Extraer Imágenes
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen del PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página en un documento PDF contiene recursos (imágenes, formularios y fuentes). Podemos acceder a estos recursos llamando al método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La clase [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contiene [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) y podemos obtener una lista de imágenes llamando al método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Por lo tanto, para extraer una imagen de la página, necesitamos obtener una referencia a la página, luego a los recursos de la página y finalmente a la colección de imágenes.
Podemos extraer una imagen en particular, por ejemplo, por índice.

El índice de la imagen devuelve un objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Este objeto proporciona un método [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) que se puede usar para guardar la imagen extraída. El siguiente fragmento de código muestra cómo extraer imágenes de un archivo PDF.

```java
public static void Extract_Images(){
       // La ruta al directorio de documentos.
       String _dataDir = "/home/admin1/pdf-examples/Samples/";
       String filePath = _dataDir + "ExtractImages.pdf";

       // Cargar documento PDF
       com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

       com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
       // Extraer una imagen en particular
       com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

       try {
           java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
           // Guardar imagen de salida
           xImage.save(outputImage);
           outputImage.close();
       } catch (java.io.FileNotFoundException e) {
           // TODO: manejar excepción
           e.printStackTrace();
       } catch (java.io.IOException e) {
           // TODO: manejar excepción
           e.printStackTrace();
       }
   }
```