---
title: Supprimer les Métadonnées d'un PDF en PHP
type: docs
weight: 70
url: /fr/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Supprimer les Métadonnées

Pour supprimer les métadonnées d'un document PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'appeler la classe **RemoveMetadata**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# enregistrer le document mis à jour avec de nouvelles informations
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Métadonnées supprimées avec succès, veuillez vérifier le fichier de sortie." . PHP_EOL;

```

**Télécharger le Code Fonctionnel**

Téléchargez **Remove Metadata (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)