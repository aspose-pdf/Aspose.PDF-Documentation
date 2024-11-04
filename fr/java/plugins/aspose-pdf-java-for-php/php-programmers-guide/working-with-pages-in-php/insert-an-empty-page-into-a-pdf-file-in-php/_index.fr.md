---
title: Insérer une Page Vide dans un Fichier PDF en PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insérer une Page Vide

Pour insérer une page vide dans un document PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **InsertEmptyPage**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# insérer une page vide dans un PDF
$pdf->getPages()->insert(1);

# Enregistrer le fichier de sortie concaténé (le document cible)
$pdf->save($dataDir . "output.pdf");

print "Page vide ajoutée avec succès!";

```

**Télécharger le Code Exécutable**

Téléchargez **Insérer une Page Vide (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)