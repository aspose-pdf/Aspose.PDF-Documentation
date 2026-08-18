---
title: احصل على خصائص نافذة الوثيقة وعرض الصفحة في بايثون
linktitle: احصل على خصائص نافذة الوثيقة وعرض الصفحة في بايثون
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-python/
description: افهم كيفية استرداد خصائص نافذة المستند وعرض الصفحة من ملف PDF في Python باستخدام Aspose.PDF للحصول على عرض تقديمي دقيق.
lastmod: "2026-06-09"
---
للحصول على خصائص نافذة المستند وعرض الصفحة لمستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **GetDocumentWindow**.

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

** تنزيل كود التشغيل **

تنزيل**الحصول على خصائص نافذة المستند وعرض الصفحة (Aspose.PDF)**Вمنأي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)
