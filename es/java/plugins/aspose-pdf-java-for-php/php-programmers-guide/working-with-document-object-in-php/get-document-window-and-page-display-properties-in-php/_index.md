---
title: Obtener las propiedades de la ventana del documento y de visualización de página en PHP
linktitle: Obtener las propiedades de la ventana del documento y de visualización de página en PHP
type: docs
weight: 30
url: /es/java/get-document-window-and-page-display-properties-in-php/
description: Aprenda cómo acceder a las propiedades de la ventana del documento y de visualización de página de un archivo PDF en PHP usando Aspose.PDF.
lastmod: "2026-09-03"
---
## Aspose.PDF - Obtener las propiedades de la ventana del documento y de visualización de página

Para obtener las propiedades de la ventana del documento y de visualización de página del documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **GetDocumentWindow**.

Código PHP

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

**Descargar código en ejecución**

Download\u0412\u00A0**Obtener propiedades de la ventana del documento y de la visualización de página (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
