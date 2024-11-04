---
title: Ajouter une table des matières à un PDF existant en PHP
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter une table des matières

Pour ajouter une table des matières dans un document Pdf en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **AddToc**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Accéder à la première page du fichier PDF
$toc_page = $doc->getPages()->insert(1);

# Créer un objet pour représenter les informations de la table des matières
$toc_info = new TocInfo();
$title = new TextFragment("Table des matières");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Définir le titre pour la table des matières
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Créer des objets de chaîne qui seront utilisés comme éléments de la table des matières
$titles = array("Première page", "Deuxième page");

$i = 0;
while ($i < 2){

    # Créer un objet Heading
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Spécifier la page de destination pour l'objet Heading
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Page de destination
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Coordonnée de destination
    $segment2->setText($titles[$i]);

    # Ajouter le heading à la page contenant la table des matières
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Enregistrer le document PDF
$doc->save($dataDir . "TOC.pdf");

print "Table des matières ajoutée avec succès, veuillez vérifier le fichier de sortie.";

```


**Télécharger le Code Exécutable**

Téléchargez **Ajouter TOC (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)