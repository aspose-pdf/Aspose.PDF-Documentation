---
title: Ajouter du texte à un fichier PDF existant en PHP
linktitle: Ajouter du texte à un fichier PDF existant en PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: Découvrez comment ajouter un nouveau texte à un document PDF existant en PHP en utilisant Aspose.PDF pour améliorer le contenu.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter du texte



Pour ajouter une chaîne de texte dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **AddText**.

Code PHP


```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Ajouter du texte (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
