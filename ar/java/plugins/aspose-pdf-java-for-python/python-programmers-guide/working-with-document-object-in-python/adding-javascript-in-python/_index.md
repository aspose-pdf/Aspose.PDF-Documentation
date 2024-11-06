---
title: إضافة جافا سكريبت في بايثون
type: docs
weight: 10
url: ar/java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

لإضافة جافا سكريبت باستخدام Aspose.PDF Java في بايثون، ببساطة قم باستدعاء طريقة AddJavascript() لفئة Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# إضافة جافا سكريبت على مستوى الصفحة
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# حفظ مستند PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "تمت إضافة جافا سكريبت بنجاح، يرجى التحقق من ملف الإخراج."

```

**تحميل الكود الجاري**

قم بتنزيل **إضافة جافا سكريبت (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)