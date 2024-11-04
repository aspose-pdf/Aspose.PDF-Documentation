---
title: Extraer Imágenes de PDF 
linktitle: Extraer Imágenes
type: docs
weight: 20
url: /php-java/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Cada página en un documento PDF contiene recursos (imágenes, formularios y fuentes). Podemos acceder a estos recursos llamando al método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La clase [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contiene [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) y podemos obtener una lista de imágenes llamando al método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Así que para extraer una imagen de una página, necesitamos obtener referencia a la página, luego a los recursos de la página y finalmente a la colección de imágenes. Podemos extraer una imagen particular, por ejemplo, por índice.

El índice de la imagen retorna un objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
This object provides a [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

```php

    // Cargar el documento PDF
    $document = new Document($inputFile);

    // Obtener la primera página del documento
    $page = $document->getPages()->get_Item(1);

    // Obtener la colección de imágenes en la página
    $xImageCollection = $page->getResources()->getImages();

    // Obtener la primera imagen de la colección
    $xImage = $xImageCollection->get_Item(1);

    // Crear un nuevo objeto FileOutputStream para guardar la imagen
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Guardar la imagen en el archivo de salida
    $xImage->save($outputImage);

    // Cerrar el archivo de imagen de salida
    $outputImage->close();
```