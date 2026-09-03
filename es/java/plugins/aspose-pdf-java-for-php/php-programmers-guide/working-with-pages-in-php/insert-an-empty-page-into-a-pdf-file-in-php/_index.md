---
title: Insertar una página vacía en un archivo PDF en PHP
linktitle: Insertar una página vacía en un archivo PDF en PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Aprenda a insertar una página vacía en cualquier posición dentro de un archivo PDF en PHP usando Aspose.PDF para una estructuración flexible de documentos.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Insertar una página vacía



Para insertar una página vacía en un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque la clase **InsertEmptyPage**.

Código PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```


**Descargar código de ejecución**



Descargue **Inserte una página vacía (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
