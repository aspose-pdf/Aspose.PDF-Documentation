---
title: Agregar Imagen a Archivo PDF Existente 
linktitle: Agregar Imagen
type: docs
weight: 10
url: /php-java/add-image-to-existing-pdf-file/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando PHP.
lastmod: "2024-06-05"
---

Cada página PDF contiene propiedades de Recursos y Contenidos. Los recursos pueden ser imágenes y formularios, por ejemplo, mientras que el contenido está representado por un conjunto de operadores PDF. Cada operador tiene su nombre y argumento. Este ejemplo utiliza operadores para agregar una imagen a un archivo PDF.

Para agregar una imagen a un archivo PDF existente:

- Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abra el documento PDF de entrada.
- Obtenga la página a la que desea agregar una imagen.
- Agregue una nueva página al documento.
- Establezca el tamaño de la página en 1190.7 x 841.995.
- Agregue una imagen a la página utilizando el archivo de imagen especificado y el cuadro de recorte de la página.
- Guarde el archivo.

El siguiente fragmento de código muestra cómo agregar la imagen en un documento PDF.

```php

    // Abra el documento utilizando el archivo de entrada especificado.
    $document = new Document($inputFile);
    
    // Agregue una nueva página al documento.
    $page = $document->getPages()->add();
    
    // Establezca el tamaño de la página en 1190.7 x 841.995.
    $page->setPageSize(1190.7, 841.995);
    
    // Agregue una imagen a la página utilizando el archivo de imagen especificado y el cuadro de recorte de la página.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // Guarde el documento modificado en el archivo de salida especificado.
    $document->save($outputFile);
    
    // Cierre el documento.
    $document->close();
```