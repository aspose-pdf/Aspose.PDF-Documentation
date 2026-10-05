---
title: "PHP での ドキュメントウィンドウとページ表示プロパティの取得"
linktitle: "PHP での ドキュメントウィンドウとページ表示プロパティの取得"
type: docs
weight: 30
url: /ja/java/get-document-window-and-page-display-properties-in-php/
description: Aspose.PDF を使用して PHP で PDF ファイルのドキュメントウィンドウとページ表示プロパティにアクセスする方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - ドキュメントウィンドウとページ表示プロパティの取得

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントのドキュメントウィンドウとページ表示プロパティを取得するには、単に **GetDocumentWindow** クラスを呼び出します。

PHP コード

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

**実行コードをダウンロード**

DownloadВ **ドキュメントウィンドウとページ表示プロパティ (Aspose.PDF)**В から以下に記載されたソーシャルコーディングサイトのいずれかで取得:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
