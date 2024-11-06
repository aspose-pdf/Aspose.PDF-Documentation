---
title: Ajouter du texte à un fichier PDF existant en PHP
type: docs
weight: 20
url: fr/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter du texte

Pour ajouter une chaîne de texte dans un document PDF en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer le module **AddText**.

Code PHP

```php

# Instancier l'objet Document
$doc = new Document($dataDir . 'input1.pdf');

# obtenir une page particulière
$pdf_page = $doc->getPages()->get_Item(1);

# créer un fragment de texte
$text_fragment = new TextFragment("texte principal");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# définir les propriétés du texte
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# créer un objet TextBuilder
$text_builder = new TextBuilder($pdf_page);

# ajouter le fragment de texte à la page PDF
$text_builder->appendText($text_fragment);

# Enregistrer le fichier PDF
$doc->save($dataDir . "Text_Added.pdf");

print "Texte ajouté avec succès" . PHP_EOL;

```


**Télécharger le Code Exécutable**

Téléchargez **Ajouter du Texte (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)