---
title: Insérer une page vide à la fin du fichier PDF en PHP
linktitle: Insérer une page vide à la fin du fichier PDF en PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Découvrez comment insérer une page vide à la fin d'un document PDF en PHP en utilisant Aspose.PDF pour l'expansion du document.
lastmod: "2026-09-21"
---
## Aspose.PDF - Insérer une page vide à la fin du fichier PDF

Pour insérer une page vide à la fin d'un document PDF à l'aide de **Aspose.PDF Java pour PHP**, utilisez la classe **InsertEmptyPageAtEndOfFile**.

Code PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## Télécharger l’exemple de code

Téléchargez **Insérer une page vide à la fin du fichier PDF (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
