---
title: Ajouter une table des matières au PDF existant en PHP
linktitle: Ajouter une table des matières au PDF existant en PHP
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-php/
description: Découvrez comment ajouter une table des matières (TOC) à un document PDF existant en PHP avec Aspose.PDF pour une navigation améliorée.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter une table des matières



Pour ajouter une table des matières dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **AddToc**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get access to first page of PDF file
$toc_page = $doc->getPages()->insert(1);

# Create object to represent TOC information
$toc_info = new TocInfo();
$title = new TextFragment("Table Of Contents");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Set the title for TOC
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Create string objects which will be used as TOC elements
$titles = array("First page", "Second page");

$i = 0;
while ($i < 2){

    # Create Heading object
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Specify the destination page for heading object
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Destination page
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Destination coordinate
    $segment2->setText($titles[$i]);

    # Add heading to page containing TOC
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Save PDF Document
$doc->save($dataDir . "TOC.pdf");

print "Added TOC Successfully, please check the output file.";

```


**Télécharger le code d'exécution**



Téléchargez** Ajouter une table des matières (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)
