---
title: Définir les informations du fichier PDF en PHP
linktitle: Définir les informations du fichier PDF en PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: Découvrez comment définir diverses propriétés de fichier, telles que les métadonnées, pour un document PDF en PHP à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Définir les informations du fichier PDF



Pour mettre à jour les informations du document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **SetPdfFileInfo**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```


**Télécharger le code d'exécution**



Téléchargez** Définir les informations du fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
