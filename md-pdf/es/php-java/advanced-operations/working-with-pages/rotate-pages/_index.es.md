---
title: Rotar Páginas de PDF programáticamente
linktitle: Rotar Páginas de PDF
type: docs
weight: 60
url: /php-java/rotate-pages/
description: Cambiar la orientación de la página y ajustar el contenido de la página a la nueva orientación de la página usando Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cambiar la Orientación de la Página

Este artículo describe cómo actualizar o cambiar la orientación de las páginas en un archivo PDF existente.

Aspose.PDF para PHP vía Java tiene la función de cambiar la orientación de la página de horizontal a vertical y viceversa.

1. Abra el documento usando el archivo de entrada especificado.
1. Obtenga todas las páginas del documento.
1. Itere a través de cada página y establezca la rotación a 90 grados.
1. Guarde el documento modificado en el archivo de salida especificado.
1. Cierre el documento.

```php

    // Abrir documento
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Recorrer todas las páginas
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```