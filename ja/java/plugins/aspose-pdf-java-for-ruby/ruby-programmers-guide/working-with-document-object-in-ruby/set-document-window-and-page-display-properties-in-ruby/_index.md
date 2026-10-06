---
title: "Ruby での文書ウィンドウとページ表示プロパティの設定"
linktitle: "Ruby での文書ウィンドウとページ表示プロパティの設定"
type: docs
weight: 100
url: /ja/java/set-document-window-and-page-display-properties-in-ruby/
description: "Ruby と Aspose.PDF を使用して、PDF の文書およびページ表示設定をカスタマイズします。"
lastmod: "2026-10-06"
---
## Aspose.PDF - 文書ウィンドウおよびページ表示プロパティの設定

Pdf文書の文書ウィンドウとページ表示プロパティを設定するには、**Aspose.PDF Java for Ruby** を使用して、単に\u0412\u00A0**SetDocumentWindow** モジュールを呼び出します。

Ruby コード

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

## 実行コードのダウンロード

以下に記載されたソーシャルコーディングサイトのいずれかから **Set Document Window and Page Display Properties (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
