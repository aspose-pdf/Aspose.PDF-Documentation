---
title: Extraer Imágenes de PDF 
linktitle: Extraer Imágenes
type: docs
weight: 20
url: /es/androidjava/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para Android a través de Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página en un documento PDF contiene recursos (imágenes, formularios y fuentes). Podemos acceder a estos recursos llamando al método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La clase [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contiene [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) y podemos obtener la lista de imágenes llamando al método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Por lo tanto, para extraer una imagen de la página, necesitamos obtener una referencia a la página, luego a los recursos de la página y finalmente a la colección de imágenes.

Podemos extraer una imagen en particular, por ejemplo, por índice.

El índice de la imagen devuelve un objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage). Este objeto proporciona un método [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) que se puede usar para guardar la imagen extraída. El siguiente fragmento de código muestra cómo extraer imágenes de un archivo PDF.

```java
public void extractImage () {
       // Abrir documento
       try {
           document=new Document(inputStream);
       } catch (Exception e) {
           resultMessage.setText(e.getMessage());
           return;
       }

       com.aspose.pdf.Page page=document.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
       // Extraer una imagen en particular
       com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
       File file=new File(fileStorage, "extracted-image.jpeg");
       try {
           java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
           // Guardar imagen de salida
           xImage.save(outputImage, ImageType.getJpeg());
           outputImage.close();
       } catch (java.io.IOException e) {
           resultMessage.setText(e.getMessage());
           return;
       }
       resultMessage.
         }
```