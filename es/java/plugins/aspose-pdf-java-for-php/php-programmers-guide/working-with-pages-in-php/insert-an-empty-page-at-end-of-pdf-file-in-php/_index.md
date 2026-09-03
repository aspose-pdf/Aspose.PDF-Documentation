---
title: Insertar una página vacía al final del archivo PDF en PHP
linktitle: Insertar una página vacía al final del archivo PDF en PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Aprenda a insertar una página vacía al final de un documento PDF en PHP usando Aspose.PDF para expandir el documento.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Insertar una página vacía al final del archivo PDF



Para insertar una página vacía al final de un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **InsertEmptyPageAtEndOfFile**.

Código PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## 
Descargar código de ejecución



Descargue **Inserte una página vacía al final del archivo PDF (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
