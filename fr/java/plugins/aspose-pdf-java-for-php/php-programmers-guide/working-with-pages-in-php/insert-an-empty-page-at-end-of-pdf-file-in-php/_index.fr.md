---
title: Insérer une Page Vide à la Fin d'un Fichier PDF en PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insérer une Page Vide à la Fin d'un Fichier PDF

Pour insérer une page vide à la fin d'un document PDF en utilisant **Aspose.PDF Java pour PHP**, invoquez simplement la classe **InsertEmptyPageAtEndOfFile**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# insérer une page vide dans un PDF
$pdf->getPages()->add();

# Enregistrer le fichier de sortie concaténé (le document cible)
$pdf->save($dataDir . "output.pdf");

print "Page vide ajoutée avec succès!" . PHP_EOL;

```

## Télécharger le Code Exécutable

Téléchargez **Insérer une Page Vide à la Fin d'un Fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)