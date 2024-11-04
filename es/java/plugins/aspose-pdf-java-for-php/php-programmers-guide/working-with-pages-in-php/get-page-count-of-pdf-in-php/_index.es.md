---
title: Obtener Conteo de Páginas de PDF en PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Conteo de Páginas

Para obtener el conteo de páginas de un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **GetNumberOfPages**.

Código PHP

```php

# Crear documento PDF

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Conteo de Páginas:" . $page_count . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargar **Obtener Conteo de Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)