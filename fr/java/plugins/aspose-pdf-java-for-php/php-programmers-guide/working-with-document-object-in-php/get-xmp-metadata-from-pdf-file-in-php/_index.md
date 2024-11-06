---
title: Obtenir des métadonnées XMP à partir d'un fichier PDF en PHP
type: docs
weight: 50
url: fr/java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir des métadonnées XMP

Pour obtenir des métadonnées XMP à partir d'un document Pdf en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **GetXMPMetadata**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtenir des propriétés
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**Télécharger le code en cours d'exécution**

Téléchargez **Obtenir des métadonnées XMP (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)