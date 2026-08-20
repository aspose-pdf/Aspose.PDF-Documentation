---
title: Optimice el documento PDF para la Web en PHP
linktitle: Optimice el documento PDF para la Web en PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Aprenda a optimizar un documento PDF para un rendimiento web más rápido y un tamaño de archivo reducido en PHP con Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Optimizar PDF para Web



Para optimizar un documento PDF para la web usando **Aspose.PDF Java para PHP**, simplemente invoque el método **optimize_web** de la clase **Optimize**.

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


**Descargar código de ejecución**



Descargue **Optimice PDF para Web (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
