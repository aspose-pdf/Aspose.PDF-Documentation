---
title: Mover Páginas de PDF
linktitle: Mover Páginas de PDF
type: docs
weight: 20
url: /es/php-java/move-pages/
description: Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para PHP vía Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mover una Página de un Documento PDF a Otro

Este tema explica cómo mover una página de un documento PDF al final de otro documento usando PHP.
Para mover una página debemos:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen
1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de destino
1. Añadir la página al documento de salida. Guardar el archivo de salida
1. Eliminar la página del documento de entrada. Guardar el documento de entrada modificado
1. Cerrar los documentos
1. Guardar y cerrar el documento de salida

El siguiente fragmento de código muestra cómo mover una página.

```php

    // Abrir documento
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Guardar archivo de salida
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```


## Mover un conjunto de Páginas de un Documento PDF a Otro

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de destino.
1. Definir las páginas a copiar del documento de entrada al documento de salida.
1. Ejecutar un bucle a través del array:
    1. Obtener la página en el índice especificado del documento de entrada.
    1. Agregar la página al documento de destino.
1. Guardar el PDF de salida usando el método Save.
1. Eliminar la página en el documento de origen usando el array.
1. Guardar el PDF de origen usando el método Save.

El siguiente fragmento de código muestra cómo insertar una página vacía al final de un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Guardar archivos de salida
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## Moviendo una Página a una nueva ubicación en el Documento PDF actual

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de origen.
1. Obtenga la página de la colección [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Agregue la página a la nueva ubicación.
1. Elimine la página en el índice 2.
1. Guarde el PDF de salida utilizando el método save.

```php

    // Abrir documento
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Guardar archivo de salida
    $document->save($outputFile);
    $document->close();      
```