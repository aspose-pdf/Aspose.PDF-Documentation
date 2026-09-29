---
title: Dapatkan Properti Jendela Dokumen dan Tampilan Halaman di PHP
linktitle: Dapatkan Properti Jendela Dokumen dan Tampilan Halaman di PHP
type: docs
weight: 30
url: /id/java/get-document-window-and-page-display-properties-in-php/
description: Pelajari cara mengakses properti jendela dokumen dan tampilan halaman dari file PDF di PHP menggunakan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Properti Jendela Dokumen dan Tampilan Halaman

Untuk mendapatkan Properti Jendela Dokumen dan Tampilan Halaman dari dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **GetDocumentWindow**.

Kode PHP

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

**Unduh Kode yang Berjalan**

Unduh\u0412\u00A0**Dapatkan Properti Jendela Dokumen dan Tampilan Halaman (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
