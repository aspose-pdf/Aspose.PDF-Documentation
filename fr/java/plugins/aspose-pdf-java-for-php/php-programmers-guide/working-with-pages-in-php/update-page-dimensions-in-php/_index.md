---
title: Mettre à jour les dimensions de la page en PHP
type: docs
weight: 90
url: /fr/java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mettre à jour les dimensions de la page

Pour mettre à jour les dimensions de la page en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **UpdatePageDimensions**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# obtenir la collection de pages
$page_collection = $pdf->getPages();

# obtenir une page particulière
$pdf_page = $page_collection->get_Item(1);

# définir la taille de la page comme A4 (11.7 x 8.3 in) et dans Aspose.PDF, 1 pouce = 72 points
# donc les dimensions A4 en points seront (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# enregistrer le fichier PDF nouvellement généré
$pdf->save($dataDir . "output.pdf");

print "Dimensions mises à jour avec succès!" . PHP_EOL;

```

**Télécharger le code en cours d'exécution**

Téléchargez **Update Page Dimensions (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)