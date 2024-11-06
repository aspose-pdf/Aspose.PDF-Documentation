---
title: Diviser un fichier PDF en pages individuelles en PHP
type: docs
weight: 80
url: fr/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Diviser les pages

Pour diviser un document PDF en pages individuelles en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **SplitAllPages**.

Code PHP

```php

# Ouvrir le document cible
$pdf = new Document($dataDir . 'input1.pdf');

# parcourir toutes les pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # créer un nouvel objet Document
    $new_document = new Document();

    # obtenir la page à un index particulier de la collection de pages
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # enregistrer le fichier PDF nouvellement généré
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Processus de division terminé avec succès!";

```

**Télécharger le code en cours d'exécution**


Téléchargez **Diviser les pages (Aspose.PDF)** à partir de l'un des sites de codage sociaux mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)

```php
<?php
// Charger le document PDF
$pdfDocument = new \Aspose\Pdf\Document("document.pdf");

// Boucle à travers toutes les pages
for ($pageNumber = 1; $pageNumber <= $pdfDocument->getPages()->size(); $pageNumber++) {
    // Créer un nouveau document
    $newDocument = new \Aspose\Pdf\Document();
    // Ajouter la page au nouveau document
    $newDocument->getPages()->add($pdfDocument->getPages()->get_Item($pageNumber));
    // Enregistrer le document
    $newDocument->save("page_" . $pageNumber . ".pdf");
}
?>
```

- [Documentation](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)


# Diviser toutes les pages d'un document PDF

Ce programme PHP illustre comment diviser chaque page d'un document PDF en un nouveau fichier PDF distinct.

## Instructions

1. Assurez-vous que vous avez installé la bibliothèque Aspose.PDF pour PHP.
2. Chargez le document PDF existant que vous souhaitez diviser.
3. Bouclez à travers chaque page du document.
4. Pour chaque page, créez un nouveau document PDF et ajoutez-y la page.
5. Enregistrez le nouveau document PDF avec un nom distinct.

## Exemple de code

Le code suivant montre comment diviser un document PDF en plusieurs fichiers PDF, un pour chaque page du document original.

```php
<?php
// Charger le document PDF
$pdfDocument = new \Aspose\Pdf\Document("document.pdf");

// Boucle à travers toutes les pages
for ($pageNumber = 1; $pageNumber <= $pdfDocument->getPages()->size(); $pageNumber++) {
    // Créer un nouveau document
    $newDocument = new \Aspose\Pdf\Document();
    // Ajouter la page au nouveau document
    $newDocument->getPages()->add($pdfDocument->getPages()->get_Item($pageNumber));
    // Enregistrer le document
    $newDocument->save("page_" . $pageNumber . ".pdf");
}
?>
```