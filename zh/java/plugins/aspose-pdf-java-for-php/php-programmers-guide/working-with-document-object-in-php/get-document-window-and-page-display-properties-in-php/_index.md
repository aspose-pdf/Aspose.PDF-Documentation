---
title: 在 PHP 中获取文档窗口和页面显示属性
linktitle: 在 PHP 中获取文档窗口和页面显示属性
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中访问 PDF 文件的文档窗口和页面显示属性。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取文档窗口和页面显示属性

要使用 **Aspose.PDF Java for PHP** 获取 Pdf 文档的文档窗口和页面显示属性，只需调用 **GetDocumentWindow** 类即可。

PHP代码

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

**下载运行代码**

从以下任何一个社交编码网站下载**获取文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
