---
title: Obtener una página en particular de un archivo PDF en PHP
linktitle: Obtener una página en particular de un archivo PDF en PHP
type: docs
weight: 30
url: /es/java/get-a-particular-page-in-a-pdf-file-in-php/
description: Aprenda cómo recuperar una página en particular de un archivo PDF en PHP usando Aspose.PDF para el procesamiento dirigido de páginas.
lastmod: "2026-09-29"
---
## Aspose.PDF - obtener página

Para obtener una página en particular en un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoque la clase **GetPage**.

Código Ruby

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## Descargar código en ejecución

Descargar **Get Page (Aspose.PDF)** de cualquiera de los sitios de codificación social que se mencionan a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
