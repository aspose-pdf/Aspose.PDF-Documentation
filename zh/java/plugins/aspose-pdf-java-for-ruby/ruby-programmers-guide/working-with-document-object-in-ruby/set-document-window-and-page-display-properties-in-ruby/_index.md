---
title: 在 Ruby 中设置文档窗口和页面显示属性
linktitle: 在 Ruby 中设置文档窗口和页面显示属性
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 自定义 PDF 中的文档和页面显示设置。
lastmod: "2026-06-09"
---
## Aspose.PDF - 设置文档窗口和页面显示属性

要使用 **Aspose.PDF Java for Ruby** 设置 Pdf 文档的文档窗口和页面显示属性，只需调用 **SetDocumentWindow** 模块即可。

红宝石代码

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

## 下载运行代码

从以下任何社交编码网站下载**设置文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)
