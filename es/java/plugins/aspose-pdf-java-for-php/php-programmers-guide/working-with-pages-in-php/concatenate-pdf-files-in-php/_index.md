---
title: Concatenar archivos PDF en PHP
linktitle: Concatenar archivos PDF en PHP
type: docs
weight: 10
url: /es/java/concatenate-pdf-files-in-php/
description: Aprenda cómo concatenar varios archivos PDF en un solo documento en PHP usando Aspose.PDF para una gestión de documentos más fácil.
lastmod: "2026-09-29"
---
## Aspose.PDF - concatenar archivos PDF

Para concatenar archivos PDF usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **ConcatenatePdfFiles**.

Código PHP

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargar **Concatenate PDF Files (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
