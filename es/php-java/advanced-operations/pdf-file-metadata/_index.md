---
title: Trabajando con Metadatos de Archivos PDF 
linktitle: Metadatos de Archivos PDF
type: docs
weight: 140
url: /es/php-java/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener Metadatos XMP de un archivo PDF, establecer Información de Archivos PDF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Información del Archivo PDF

Para obtener información específica de un archivo PDF, primero obtenga el objeto 'docInfo' utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Una vez que se recupera el objeto 'docInfo', puede obtener los valores de las propiedades individuales.

El siguiente fragmento de código muestra cómo establecer la información del archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Obtener información del documento
    $docInfo = $document->getInfo();

    // Mostrar información del documento
    $responseData1 = "Autor: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Fecha de Creación: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Palabras clave: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Fecha de Modificación: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Asunto: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Título: " . $docInfo->getTitle() . "";

    $document->close();
```