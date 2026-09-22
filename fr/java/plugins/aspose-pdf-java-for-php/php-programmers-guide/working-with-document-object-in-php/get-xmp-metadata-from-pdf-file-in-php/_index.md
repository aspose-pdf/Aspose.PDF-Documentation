---
title: Obtenir des métadonnées XMP à partir d'un fichier PDF en PHP
linktitle: Obtenir des métadonnées XMP à partir d'un fichier PDF en PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: Découvrez comment extraire les métadonnées XMP de documents PDF en PHP à l'aide d'Aspose.PDF pour une analyse avancée du contenu.
lastmod: "2026-09-21"
---
## Aspose.PDF - Obtenir les métadonnées XMP

Pour obtenir les métadonnées XMP d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, utilisez la classe **GetXMPMetadata**.

Code PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Télécharger l’exemple de code**

Téléchargez **Obtenez des métadonnées XMP (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
