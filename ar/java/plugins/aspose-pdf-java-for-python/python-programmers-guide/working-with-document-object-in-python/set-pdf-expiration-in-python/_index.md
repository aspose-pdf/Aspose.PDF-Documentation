---
title: ضبط انتهاء صلاحية ملف PDF في بايثون
type: docs
weight: 80
url: /ar/java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

لضبط انتهاء صلاحية مستند PDF باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء فئة **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# احفظ المستند المحدث بالمعلومات الجديدة
doc.save(self.dataDir + "set_expiration.pdf");

print "تحديث معلومات المستند، يرجى التحقق من الملف الناتج."
```

**تحميل الكود قيد التشغيل**

قم بتحميل **تعيين انتهاء صلاحية PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)