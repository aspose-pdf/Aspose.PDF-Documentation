---
title: Insertar una página en blanco en un archivo PDF en PHP
linktitle: Insertar una página en blanco en un archivo PDF en PHP
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Aprenda cómo insertar una página en blanco en cualquier posición dentro de un archivo PDF en PHP usando Aspose.PDF para una estructuración flexible de documentos.
lastmod: "2026-09-03"
---
## Aspose.PDF - Insertar una página en blanco

Para insertar una página en blanco en un documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **InsertEmptyPage**.

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

**Descargar Código en Ejecución**

DescargarВ **Insert an Empty Page (Aspose.PDF)**В deВ cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
