---
title: Optimizar documento PDF para la web en PHP
linktitle: Optimizar documento PDF para la web en PHP
type: docs
weight: 60
url: /es/java/optimize-pdf-document-for-the-web-in-php/
description: Aprenda cómo optimizar un documento PDF para un rendimiento web más rápido y un tamaño de archivo reducido en PHP con Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Optimizar PDF para la web

Para optimizar el documento PDF para la web usando **Aspose.PDF Java for PHP**, simplemente invoque el método **optimize_web** deВ  **Optimize** class.

Código PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**Descargar código en ejecución**

DescargarВ **Optimizar PDF para Web (Aspose.PDF)**В deВ cualquiera de los sitios de código social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
