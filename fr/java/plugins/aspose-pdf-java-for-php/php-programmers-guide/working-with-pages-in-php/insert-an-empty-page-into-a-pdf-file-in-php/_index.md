---
title: Insérer une page vide dans un fichier PDF en PHP
linktitle: Insérer une page vide dans un fichier PDF en PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: Apprenez à insérer une page vide à n'importe quel endroit dans un fichier PDF en PHP en utilisant Aspose.PDF pour une structuration flexible des documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Insérer une page vide



Pour insérer une page vide dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **InsertEmptyPage**.

Code PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```


**Télécharger le code d'exécution**



Téléchargez** Insérer une page vide (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
