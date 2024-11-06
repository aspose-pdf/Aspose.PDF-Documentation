---
title: Obtenir une Page Particulière dans un Fichier PDF en PHP
type: docs
weight: 30
url: fr/java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir une Page

Pour obtenir une page particulière dans un document PDF en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer la classe **GetPage**.

Code Ruby

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# obtenir la page à un index particulier de la collection de pages
$pdf_page = $pdf->getPages()->get_Item(1);

# créer un nouvel objet Document
$new_document = new Document();

# ajouter la page à la collection de pages du nouvel objet document
$new_document->getPages()->add($pdf_page);

# enregistrer le fichier PDF nouvellement généré
$new_document->save($dataDir . "output.pdf");

print "Processus terminé avec succès!";

```

## Télécharger le Code Exécuté

Téléchargez **Obtenir la Page (Aspose.PDF)** depuis n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)