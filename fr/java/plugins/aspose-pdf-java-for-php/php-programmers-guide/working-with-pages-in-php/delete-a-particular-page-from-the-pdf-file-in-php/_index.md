---
title: Supprimer une page particulière du fichier PDF en PHP
linktitle: Supprimer une page particulière du fichier PDF en PHP
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Découvrez comment supprimer une page spécifique d'un document PDF en PHP avec Aspose.PDF, simplifiant ainsi l'édition de documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Supprimer la page



Pour supprimer une page particulière du document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **DeletePage**.

Code PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```


**Télécharger en cours d'exécution**



Téléchargez ** Supprimer la page (Aspose.PDF) ** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
