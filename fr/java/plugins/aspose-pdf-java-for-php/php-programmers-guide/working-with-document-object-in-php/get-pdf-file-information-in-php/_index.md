---
title: Obtenir des informations sur un fichier PDF en PHP
linktitle: Obtenir des informations sur un fichier PDF en PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: Découvrez comment récupérer des informations détaillées sur un fichier PDF, y compris les métadonnées et les propriétés, en PHP avec Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir des informations sur le fichier PDF



Pour obtenir les informations sur le fichier d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetPdfFileInfo**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```


**Télécharger le code d'exécution**



Téléchargez** Obtenez des informations sur le fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
