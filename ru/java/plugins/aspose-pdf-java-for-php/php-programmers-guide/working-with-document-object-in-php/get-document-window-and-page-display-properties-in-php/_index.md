---
title: Получить свойства окна документа и отображения страниц в PHP
linktitle: Получить свойства окна документа и отображения страниц в PHP
type: docs
weight: 30
url: /ru/java/get-document-window-and-page-display-properties-in-php/
description: Узнайте, как получить доступ к свойствам окна документа и отображения страниц PDF‑файла в PHP с помощью Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF - Получить свойства окна документа и отображения страниц

Чтобы получить свойства окна документа и отображения страниц PDF‑документа, используя **Aspose.PDF Java for PHP**, просто вызовите класс **GetDocumentWindow**.

PHP‑код

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

**Скачать исполняемый код**

Скачать **Получить свойства окна документа и отображения страниц (Aspose.PDF)** из любого из указанных ниже сайтов с открытым кодом:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)

