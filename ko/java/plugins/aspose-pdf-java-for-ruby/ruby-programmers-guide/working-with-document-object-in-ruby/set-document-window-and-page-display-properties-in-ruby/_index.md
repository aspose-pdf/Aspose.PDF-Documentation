---
title: Ruby에서 문서 창 및 페이지 표시 속성 설정
linktitle: Ruby에서 문서 창 및 페이지 표시 속성 설정
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
description: Ruby 및 Aspose.PDF를 사용하여 PDF의 문서 및 페이지 표시 설정을 사용자 정의하세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 문서 창 및 페이지 표시 속성 설정



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 문서 창 및 페이지 표시 속성을 설정하려면 **SetDocumentWindow** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Set different document properties

# Position of document's window - Default: false

doc.setCenterWindow(true)

# Predominant reading order; determine the position of page

# when displayed side by side - Default: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Whether window's title bar should display document title.

# If false, title bar displays PDF file name - Default: false

doc.setDisplayDocTitle(true)

# Whether to resize the document's window to fit the size of

# first displayed page - Default: false

doc.setFitWindow(true)

# Whether to hide menu bar of the viewer application - Default: false

doc.setHideMenubar(true)

# Whether to hide tool bar of the viewer application - Default: false

doc.setHideToolBar(true)

# Whether to hide UI elements like scroll bars

# and leaving only the page contents displayed - Default: false

doc.setHideWindowUI(true)

# The document's page mode. How to display document on exiting full-screen mode.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# The page layout i.e. single page, one column

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# How the document should display when opened.

doc.setPageMode()

# Save updated PDF file

doc.save(data_dir + "Set Document Window.pdf")
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트에서 **문서 창 및 페이지 표시 속성 설정(Aspose.PDF)**을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
