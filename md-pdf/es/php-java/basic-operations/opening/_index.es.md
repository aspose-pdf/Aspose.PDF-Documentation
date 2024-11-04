---
title: Abrir Documento PDF
linktitle: Abrir
type: docs
weight: 20
url: /php-java/open-pdf-document/
description: Aprende cómo abrir un archivo PDF con Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir un documento PDF existente

Los archivos PDF o archivos de formato de documento portátil se han convertido en el estándar universal para el intercambio de documentos. Se utilizan ampliamente para conservar el formato de un documento. Sin embargo, trabajar con archivos PDF usando lenguajes de programación como PHP a través de Java puede ser un poco difícil. Este artículo presenta la biblioteca Aspose.PDF para PHP a través de Java, que te permite abrir tu PDF de manera rápida y sencilla.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "El documento ha sido abierto con éxito. Tamaño del archivo: " . filesize($inputFile);
```