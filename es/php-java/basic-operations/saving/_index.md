---
title: Guardar Documento PDF 
linktitle: Guardar
type: docs
weight: 30
url: /es/php-java/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF con la biblioteca Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos utilizando el método save de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```