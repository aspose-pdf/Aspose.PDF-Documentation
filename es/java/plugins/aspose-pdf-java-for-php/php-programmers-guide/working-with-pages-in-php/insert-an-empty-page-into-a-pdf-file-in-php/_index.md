---
title: Insertar una página vacía en un archivo PDF en PHP
linktitle: Insertar una página vacía en un archivo PDF en PHP
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Aprenda cómo insertar una página vacía en cualquier posición dentro de un archivo PDF en PHP usando Aspose.PDF para una estructuración flexible del documento.
lastmod: "2026-09-29"
---
## Aspose.PDF - insertar una página vacía

Para insertar una página vacía en un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **InsertEmptyPage**.

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

**Descargar código en ejecución**

Descargar **Insertar una página vacía (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
