---
title: Supprimer les métadonnées du PDF en PHP
linktitle: Supprimer les métadonnées du PDF en PHP
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
description: Découvrez comment supprimer les métadonnées d'un document PDF en PHP à l'aide d'Aspose.PDF pour améliorer la confidentialité et la sécurité des documents.
lastmod: "2026-09-21"
---
## Aspose.PDF - Supprimer les métadonnées

Pour supprimer les métadonnées d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, utilisez la classe **RemoveMetadata**.

Code PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**Télécharger l’exemple de code**

Téléchargez **Supprimer les métadonnées (Aspose.PDF)** de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
