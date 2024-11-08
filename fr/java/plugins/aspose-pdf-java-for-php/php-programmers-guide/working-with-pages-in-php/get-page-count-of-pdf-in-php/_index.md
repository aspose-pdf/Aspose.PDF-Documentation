---
title: Obtenir le Nombre de Pages d'un PDF en PHP
type: docs
weight: 40
url: /fr/java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir le Nombre de Pages

Pour obtenir le nombre de pages d'un document Pdf en utilisant **Aspose.PDF Java pour PHP**, il suffit d'appeler la classe **GetNumberOfPages**.

Code PHP

```php

# Créer un document PDF

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Nombre de Pages:" . $page_count . PHP_EOL;

```

**Télécharger le Code Exécuté**

Téléchargez **Obtenir le Nombre de Pages (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)