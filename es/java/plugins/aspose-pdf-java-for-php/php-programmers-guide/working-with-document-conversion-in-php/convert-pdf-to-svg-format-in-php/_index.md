---
title: Convertir PDF a formato SVG en PHP
linktitle: Convertir PDF a formato SVG en PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: Descubra cómo convertir documentos PDF a formato SVG en PHP con Aspose.PDF para una transformación de gráficos vectoriales de alta calidad.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir PDF a SVG



Para convertir PDF a formato SVG usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **PdfToSvg**.

Código PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```


**Descargar código de ejecución**



Descargue **Convierta PDF a formato SVG (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
