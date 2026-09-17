---
title: Optimiser un document PDF pour le Web en PHP
linktitle: Optimiser un document PDF pour le Web en PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Apprenez à optimiser un document PDF pour des performances Web plus rapides et une taille de fichier réduite en PHP avec Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Optimiser le PDF pour le Web



Pour optimiser un document PDF pour le Web à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la méthode **optimize_web** de la classe **Optimize**.

Code PHP


```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```


**Télécharger le code d'exécution**



Téléchargez** Optimiser le PDF pour le Web (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
