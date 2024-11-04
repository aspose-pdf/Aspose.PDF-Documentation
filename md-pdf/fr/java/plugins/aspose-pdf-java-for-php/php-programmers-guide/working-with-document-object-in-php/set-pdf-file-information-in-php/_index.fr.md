---
title: Définir les Informations d'un Fichier PDF en PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Définir les Informations d'un Fichier PDF

Pour mettre à jour les informations d'un document Pdf en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **SetPdfFileInfo**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtenir les informations du document
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF pour java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("Informations sur le PDF");
$doc_info->setTitle("Définition des Informations du Document PDF");

# enregistrer le document mis à jour avec les nouvelles informations
$doc->save($dataDir . "Updated_Information.pdf");

print "Mettre à jour les informations du document, veuillez vérifier le fichier de sortie.";

```

**Télécharger le Code en Cours d'Exécution**

Téléchargez **Définir les Informations d'un Fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)