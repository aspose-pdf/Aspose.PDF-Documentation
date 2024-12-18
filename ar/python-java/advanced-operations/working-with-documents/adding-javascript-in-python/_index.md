---
title: إضافة JavaScript في Python
type: docs
weight: 10
url: /ar/python-java/adding-javascript-in-python/
---

لإضافة JavaScript باستخدام Aspose.PDF Java في Python، ببساطة قم باستدعاء طريقة AddJavascript() من فئة Document.

**كود Python**

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# إضافة JavaScript على مستوى الصفحة
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# حفظ مستند PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "تمت إضافة JavaScript بنجاح، يرجى التحقق من ملف المخرجات."

```

**تنزيل الكود التشغيلي**

قم بتنزيل **إضافة JavaScript (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)