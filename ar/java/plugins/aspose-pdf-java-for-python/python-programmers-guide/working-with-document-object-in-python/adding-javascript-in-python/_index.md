---
title: إضافة جافا سكريبت في بايثون
linktitle: إضافة جافا سكريبت في بايثون
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: تعرف على كيفية تضمين كود JavaScript في مستند PDF باستخدام Python وAspose.PDF لتعزيز التفاعل.
lastmod: "2026-06-09"
---
لإلحاق إضافة Javascript باستخدام Aspose.PDF Java في Python، ما عليك سوى استدعاء طريقة AddJavascript() لفئة المستند.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```

** تنزيل كود التشغيل **

قم بتنزيل **إضافة Javascript (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
