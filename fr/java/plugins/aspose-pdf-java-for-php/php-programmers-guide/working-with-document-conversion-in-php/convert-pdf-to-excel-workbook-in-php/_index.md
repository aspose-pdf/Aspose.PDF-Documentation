---
title: Convertir un PDF en classeur Excel en PHP
linktitle: Convertir un PDF en classeur Excel en PHP
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: Apprenez à convertir des fichiers PDF en classeurs Excel en PHP à l'aide d'Aspose.PDF, permettant une extraction et une manipulation transparentes des données.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir un PDF en classeur Excel



Pour convertir un document PDF en classeur Excel à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **PdfToExcel**.

Code PHP


```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Convertir un PDF en classeur Excel (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
