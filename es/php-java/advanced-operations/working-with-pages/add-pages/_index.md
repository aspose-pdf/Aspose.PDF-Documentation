---
title: Añadir Páginas en PDF 
linktitle: Añadir Páginas
type: docs
weight: 10
url: /es/php-java/add-pages/
description: Este artículo enseña cómo insertar (añadir) una página en la ubicación deseada de un archivo PDF. Aprenda cómo mover, eliminar (borrar) páginas de un archivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir o Insertar Página en un Archivo PDF

Aspose.PDF para PHP a través de Java te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF. Necesitas pasar la ubicación donde deseas insertar la página en blanco al método de inserción. Esta sección muestra cómo añadir páginas a un PDF con Aspose.PDF para PHP a través de Java.

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

El siguiente fragmento de código muestra cómo insertar una página vacía en un archivo PDF:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de entrada.
1. Añadir página e insertarla en un PDF.

1. Guarda el PDF de salida utilizando el método Save.

El siguiente fragmento de código te muestra cómo insertar una página en un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Añadir página
    $document->getPages()->add();

    // Insertar una página vacía en un PDF
    $document->getPages()->insert(2);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

En el ejemplo anterior, añadimos una página vacía con parámetros predeterminados. Si necesitas que el tamaño de la página sea el mismo que el de otra página en el documento, debes añadir
unas pocas líneas de código:

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Añadir página
    $page1 = $document->getPages()->add();

    // Insertar una página vacía en un PDF
    $page2 = $document->getPages()->insert(2);

    // copiar parámetros de la página desde la página 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```


### Agregar una Página Vacía al Final de un Archivo PDF

A veces, deseas asegurarte de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) con el archivo PDF de entrada.
1. Agrega una página e insértala en un PDF.
1. Guarda el PDF de salida usando el método save.

El siguiente fragmento de código te muestra cómo insertar una página vacía al final de un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Agregar página
    $document->getPages()->add();

    // Insertar una página vacía en un PDF
    $document->getPages()->insert(2);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```