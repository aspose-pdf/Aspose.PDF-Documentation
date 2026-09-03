---
title: Actualizar dimensiones de página en PHP
linktitle: Actualizar dimensiones de página en PHP
type: docs
weight: 90
url: /es/java/update-page-dimensions-in-php/
description: Aprenda cómo modificar las dimensiones de la página dentro de un documento PDF en PHP usando Aspose.PDF para un mejor control del diseño.
lastmod: "2026-09-03"
---
## Aspose.PDF - Actualizar dimensiones de página

Para actualizar las dimensiones de la página usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **UpdatePageDimensions**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**Descargar código en ejecución**

DescargarВ **Actualizar dimensiones de página (Aspose.PDF)**В deV cualquier sitio de codificación social mencionado a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)
