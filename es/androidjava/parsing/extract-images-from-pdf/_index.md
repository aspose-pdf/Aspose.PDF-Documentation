---
title: Extraer imágenes de PDF
linktitle: Extraer imágenes
type: docs
weight: 20
url: /es/androidjava/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de PDF usando Aspose.PDF for Android via Java
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página en el documento PDF contiene recursos (imágenes, formularios y fuentes). Podemos acceder a estos recursos llamando [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) método. Clase [Recursos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contienen [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) y podemos obtener la lista de imágenes llamando a [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) método.

Así, para extraer la imagen de la página, necesitamos obtener una referencia a la página, luego a los recursos de la página y por último a la colección de imágenes.
Imagen particular podemos extraer, por ejemplo, por índice.

El índice de la imagen devuelve un [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) objeto.
Este objeto proporciona un [Guardar](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) método que se puede usar para guardar la imagen extraída. El siguiente fragmento de código muestra cómo extraer imágenes de un archivo PDF.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

