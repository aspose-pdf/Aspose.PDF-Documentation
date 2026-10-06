---
title: "Python でのドキュメントウィンドウとページ表示プロパティの取得"
linktitle: "Python でのドキュメントウィンドウとページ表示プロパティの取得"
type: docs
weight: 30
url: /ja/java/get-document-window-and-page-display-properties-in-python/
description: Aspose.PDF を使用して Python で PDF からドキュメントウィンドウとページ表示プロパティを取得する方法を理解し、正確な表示を実現します。
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントのドキュメントウィンドウとページ表示プロパティを取得するには、単に **GetDocumentWindow** クラスを呼び出してください。

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

**実行コードをダウンロード**

以下に記載されたソーシャルコーディングサイトのいずれかから **ドキュメントウィンドウとページ表示プロパティ (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)
