---
title: Concaténer des fichiers PDF en PHP
linktitle: Concaténer des fichiers PDF en PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
description: Apprenez à concaténer plusieurs fichiers PDF en un seul document en PHP à l'aide d'Aspose.PDF pour faciliter la gestion des documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Concaténer des fichiers PDF



Pour concaténer des fichiers PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **ConcatenatePdfFiles**.

Code PHP


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


**Télécharger le code d'exécution**



Téléchargez** Concaténer des fichiers PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
