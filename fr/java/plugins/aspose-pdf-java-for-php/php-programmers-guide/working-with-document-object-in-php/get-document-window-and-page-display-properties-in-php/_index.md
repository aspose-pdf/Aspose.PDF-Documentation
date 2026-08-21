---
title: Obtenir les propriétés d'affichage de la fenêtre du document et de la page en PHP
linktitle: Obtenir les propriétés d'affichage de la fenêtre du document et de la page en PHP
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
description: Découvrez comment accéder aux propriétés d'affichage de la fenêtre du document et de la page d'un fichier PDF en PHP à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir les propriétés d'affichage de la fenêtre du document et de la page



Pour obtenir les propriétés d'affichage de la fenêtre et de la page du document PDF à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement la classe **GetDocumentWindow**.

Code PHP


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get different document properties
# Position of document's window - Default: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# Predominant reading order; determine the position of page
# when displayed side by side - Default: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# Whether window's title bar should display document title.
# If false, title bar displays PDF file name - Default: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

#Whether to resize the document's window to fit the size of
#first displayed page - Default: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# Whether to hide menu bar of the viewer application - Default: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# Whether to hide tool bar of the viewer application - Default: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# Whether to hide UI elements like scroll bars
# and leaving only the page contents displayed - Default: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# The document's page mode. How to display document on exiting full-screen mode.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# The page layout i.e. single page, one column
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

#How the document should display when opened.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**Télécharger le code d'exécution**



Téléchargez** Obtenez les propriétés d'affichage de la fenêtre et de la page du document (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
