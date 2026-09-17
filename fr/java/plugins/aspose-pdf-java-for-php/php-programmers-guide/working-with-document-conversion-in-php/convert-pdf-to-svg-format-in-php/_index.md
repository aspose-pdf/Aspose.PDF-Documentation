---
title: Convertir un PDF au format SVG en PHP
linktitle: Convertir un PDF au format SVG en PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: Découvrez comment convertir des documents PDF au format SVG en PHP avec Aspose.PDF pour une transformation de graphiques vectoriels de haute qualité.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir un PDF en SVG



Pour convertir un PDF au format SVG à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **PdfToSvg**.

Code PHP


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


**Télécharger le code d'exécution**



Téléchargez** Convertir un PDF au format SVG (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
