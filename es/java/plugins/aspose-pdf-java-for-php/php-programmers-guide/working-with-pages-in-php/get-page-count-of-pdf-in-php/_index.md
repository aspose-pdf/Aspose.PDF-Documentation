---
title: Obtener recuento de páginas de PDF en PHP
linktitle: Obtener recuento de páginas de PDF en PHP
type: docs
weight: 40
url: /es/java/get-page-count-of-pdf-in-php/
description: Descubra cómo recuperar el recuento total de páginas de un documento PDF en PHP usando Aspose.PDF para el análisis de documentos.
lastmod: "2026-09-29"
---
## Aspose.PDF - obtener recuento de páginas

Para obtener el recuento de páginas de un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **GetNumberOfPages**.

Código PHP

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**Descargar código en ejecución**

Descargar **Obtener recuento de páginas (Aspose.PDF)** de cualquier sitio de código social mencionado a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
