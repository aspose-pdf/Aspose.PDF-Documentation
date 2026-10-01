---
title: إضافة JavaScript في Python
linktitle: إضافة JavaScript في Python
type: docs
weight: 10
url: /ar/java/adding-javascript-in-python/
description: اكتشف كيفية دمج شفرة JavaScript داخل مستند PDF باستخدام Python و Aspose.PDF لتعزيز التفاعلية.
lastmod: "2026-10-01"
---
لإضافة JavaScript باستخدام Aspose.PDF Java في Python، ما عليك سوى استدعاء طريقة AddJavascript() من فئة Document.

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

**تنزيل الكود الجاري**

قم بتنزيل **Add Javascript (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
