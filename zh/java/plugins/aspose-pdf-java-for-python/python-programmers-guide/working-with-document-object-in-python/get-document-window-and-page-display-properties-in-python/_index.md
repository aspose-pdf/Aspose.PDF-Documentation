---
title: 在Python中获取文档窗口和页面显示属性
linktitle: 在Python中获取文档窗口和页面显示属性
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-python/
description: 了解如何使用 Aspose.PDF 从 Python 中的 PDF 中检索文档窗口和页面显示属性，以实现准确的演示。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 获取 Pdf 文档的文档窗口和页面显示属性，只需调用 **GetDocumentWindow** 类即可。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get different document properties
# Position of document's window - Default: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Predominant reading order; determine the position of page
# when displayed side by side - Default: L2R
print "Direction :- " + str(doc.getDirection())

# Whether window's title bar should display document title.
# If false, title bar displays PDF file name - Default: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

#Whether to resize the document's window to fit the size of
#first displayed page - Default: false
print "FitWindow :- " + str(doc.getFitWindow())

# Whether to hide menu bar of the viewer application - Default: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Whether to hide tool bar of the viewer application - Default: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Whether to hide UI elements like scroll bars
# and leaving only the page contents displayed - Default: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# The document's page mode. How to display document on exiting full-screen mode.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# The page layout i.e. single page, one column
print "PageLayout :-" + str(doc.getPageLayout())

#How the document should display when opened.
print "pageMode :-" + str(doc.getPageMode())
```

**下载运行代码**

从以下任何一个社交编码网站下载**获取文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)
