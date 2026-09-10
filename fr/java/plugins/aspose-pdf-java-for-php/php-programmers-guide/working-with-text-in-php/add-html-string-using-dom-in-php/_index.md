---
title: Ajouter une chaîne HTML en utilisant DOM en PHP
linktitle: Ajouter une chaîne HTML en utilisant DOM en PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: Découvrez comment ajouter du contenu HTML à un document PDF à l'aide du DOM en PHP avec Aspose.PDF pour la création de documents riches.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter du HTML



Pour ajouter une chaîne HTML dans un document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **AddHtml**.

Code PHP


```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Ajouter du HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
