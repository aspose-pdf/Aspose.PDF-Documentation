---
title: Convertir un fichier SVG au format PDF en PHP
linktitle: Convertir un fichier SVG au format PDF en PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: Découvrez comment convertir des fichiers SVG au format PDF en PHP à l'aide d'Aspose.PDF pour une gestion efficace des documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir SVG en PDF



Pour convertir un fichier SVG au format PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **SvgToPdf**.

Code PHP


```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```


**Télécharger le code d'exécution**



Téléchargez** Convertir SVG en PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
