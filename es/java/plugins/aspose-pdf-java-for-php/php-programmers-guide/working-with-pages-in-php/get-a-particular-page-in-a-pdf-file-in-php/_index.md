---
title: Obtener una página particular en un archivo PDF en PHP
linktitle: Obtener una página particular en un archivo PDF en PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: Aprenda cómo recuperar una página particular de un archivo PDF en PHP usando Aspose.PDF para el procesamiento de páginas específicas.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtener página



Para obtener una página particular en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque la clase **GetPage**.

Código Rubí


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

## 
Descargar código de ejecución



Descargue **Obtener página (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
