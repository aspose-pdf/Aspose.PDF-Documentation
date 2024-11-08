---
title: Supprimer une Page Particulière du Fichier PDF En PHP
type: docs
weight: 20
url: /fr/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Supprimer une Page

Pour supprimer une page particulière du document PDF en utilisant **Aspose.PDF Java pour PHP**, invoquez simplement la classe **DeletePage**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# supprimer une page particulière
$pdf->getPages()->delete(2);

# enregistrer le fichier PDF nouvellement généré
$pdf->save($dataDir . "output.pdf");

print "Page supprimée avec succès!";

```

**Télécharger l'Exécution**

Téléchargez **Supprimer la Page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)