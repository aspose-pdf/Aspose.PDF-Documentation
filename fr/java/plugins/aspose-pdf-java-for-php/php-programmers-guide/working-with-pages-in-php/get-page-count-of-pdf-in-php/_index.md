---
title: Obtenir le nombre de pages d'un PDF en PHP
linktitle: Obtenir le nombre de pages d'un PDF en PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: Découvrez comment récupérer le nombre total de pages d'un document PDF en PHP en utilisant Aspose.PDF pour l'analyse de documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir le nombre de pages



Pour obtenir le nombre de pages d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetNumberOfPages**.

Code PHP


```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Obtenir le nombre de pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
