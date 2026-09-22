---
title: Obtenir une page particulière dans un fichier PDF en PHP
linktitle: Obtenir une page particulière dans un fichier PDF en PHP
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: Découvrez comment récupérer une page particulière d'un fichier PDF en PHP en utilisant Aspose.PDF pour un traitement de page ciblé.
lastmod: "2026-09-21"
---
## Aspose.PDF - Obtenir la page

Pour obtenir une page particulière dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, utilisez la classe **GetPage**.

Code PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## Télécharger l’exemple de code

Téléchargez **Obtenir la page (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
