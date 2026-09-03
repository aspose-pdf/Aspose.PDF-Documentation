---
title: Obtener recuento de páginas de PDF en PHP
linktitle: Obtener recuento de páginas de PDF en PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: Descubra cómo recuperar el recuento total de páginas de un documento PDF en PHP utilizando Aspose.PDF para el análisis de documentos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener recuento de páginas



Para obtener el recuento de páginas de un documento PDF utilizando **Aspose.PDF Java para PHP**, simplemente invoque la clase **GetNumberOfPages**.

Código PHP


```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```


**Descargar código de ejecución**



Descargue **Obtenga recuento de páginas (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
