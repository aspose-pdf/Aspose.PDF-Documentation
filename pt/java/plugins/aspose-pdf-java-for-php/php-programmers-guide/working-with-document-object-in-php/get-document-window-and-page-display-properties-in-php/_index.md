---
title: Obter Propriedades da Janela de Documento e Exibição de Página em PHP
linktitle: Obter Propriedades da Janela de Documento e Exibição de Página em PHP
type: docs
weight: 30
url: /pt/java/get-document-window-and-page-display-properties-in-php/
description: Aprenda como acessar as propriedades da janela de documento e de exibição de página de um arquivo PDF em PHP usando Aspose.PDF.
lastmod: "2026-10-06"
---
## Aspose.PDF - Obter Propriedades da Janela de Documento e Exibição de Página

Para obter as propriedades da janela de documento e de exibição de página de um documento Pdf usando **Aspose.PDF Java for PHP**, basta invocar a classe **GetDocumentWindow**.

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

**Baixar Código em Execução**

DownloadВ **Obter Propriedades da Janela do Documento e Exibição de Página (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
