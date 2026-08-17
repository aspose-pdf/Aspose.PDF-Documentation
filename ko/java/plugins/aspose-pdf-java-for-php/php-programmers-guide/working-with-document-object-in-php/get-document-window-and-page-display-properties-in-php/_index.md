---
title: PHP에서 문서 창 및 페이지 표시 속성 가져오기
linktitle: PHP에서 문서 창 및 페이지 표시 속성 가져오기
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
description: Aspose.PDF를 사용하여 PHP에서 PDF 파일의 문서 창 및 페이지 표시 속성에 액세스하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 문서 창 및 페이지 표시 속성 가져오기



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서의 문서 창 및 페이지 표시 속성을 가져오려면 간단히 **GetDocumentWindow** 클래스를 호출하면 됩니다.



PHP 코드


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


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트 중 하나에서 **문서 창 및 페이지 표시 속성(Aspose.PDF)**을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
