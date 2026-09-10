---
title: Définir l'expiration du PDF en PHP
linktitle: Définir l'expiration du PDF en PHP
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: Découvrez comment définir une date d'expiration pour un fichier PDF en PHP, en contrôlant l'accès avec Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Définir l'expiration du PDF



Pour définir l'expiration d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **SetExpiration**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Définir l'expiration du PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
