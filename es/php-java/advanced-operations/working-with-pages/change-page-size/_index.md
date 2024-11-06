---
title: Cambiar Tamaño de Página de PDF Programáticamente
linktitle: Cambiar Tamaño de Página de PDF
type: docs
weight: 50
url: es/php-java/change-page-size/
description: Cambiar el tamaño de página de su archivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cambiar Tamaño de Página de PDF

Aspose.PDF para PHP a través de Java le permite cambiar el tamaño de la página de PDF con simples líneas de código en sus aplicaciones Java. Este tema explica cómo actualizar/cambiar las dimensiones (tamaño) de la página de un archivo PDF existente.

La clase [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contiene el método SetPageSize(...) que le permite establecer el tamaño de la página. El fragmento de código a continuación actualiza las dimensiones de la página en unos pocos pasos sencillos:

1. Cargue el archivo PDF de origen.
1. Obtenga las páginas en el objeto [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtenga una página dada.
1. Llame al método setPageSize(..) para actualizar sus dimensiones.

1. Llame al método save(..) de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para generar el archivo PDF con dimensiones de página actualizadas.

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4.

```php

    // Abrir documento
    $document = new Document($inputFile);
      
    // Obtener colección de páginas
    $pageCollection = $document->getPages();

    // Obtener página particular
    $page = $pageCollection->get_Item(1);

    // Establecer el tamaño de la página como A4 (11.7 x 8.3 pulgadas) y en Aspose.Pdf, 1 pulgada = 72 puntos
    // Por lo tanto, las dimensiones A4 en puntos serán (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

## Obtener Tamaño de Página PDF

Puede leer el tamaño de página PDF de un archivo PDF existente usando Aspose.PDF para PHP a través de Java. El siguiente ejemplo de código muestra cómo leer las dimensiones de la página PDF usando PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);
      
    // Agrega una página en blanco al documento PDF
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Obtener información de altura y ancho de página
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Rotar página a un ángulo de 90 grados
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Obtener información de altura y ancho de página
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```