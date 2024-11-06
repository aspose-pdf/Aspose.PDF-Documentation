---
title: Optimizar Documento PDF para la Web en PHP
type: docs
weight: 60
url: es/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimizar PDF para la Web

Para optimizar un documento PDF para la web usando **Aspose.PDF Java para PHP**, simplemente invoque el método **optimize_web** de la clase **Optimize**.

Código PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Abrir un documento pdf.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimizar para la web

    $doc->optimize();

    #Guardar documento de salida

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "PDF optimizado para la Web, por favor revise el archivo de salida." . PHP_EOL;

}    
```

**Descargar Código en Ejecución**

Descargue **Optimizar PDF para Web (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)