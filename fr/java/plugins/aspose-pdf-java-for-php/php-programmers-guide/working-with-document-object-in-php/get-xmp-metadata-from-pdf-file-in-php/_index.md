---
title: Obtenez des métadonnées XMP à partir d'un fichier PDF en PHP
linktitle: Obtenez des métadonnées XMP à partir d'un fichier PDF en PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: Découvrez comment extraire les métadonnées XMP de documents PDF en PHP à l'aide d'Aspose.PDF pour une analyse avancée du contenu.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir les métadonnées XMP



Pour obtenir les métadonnées XMP d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetXMPMetadata**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Obtenez des métadonnées XMP (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
