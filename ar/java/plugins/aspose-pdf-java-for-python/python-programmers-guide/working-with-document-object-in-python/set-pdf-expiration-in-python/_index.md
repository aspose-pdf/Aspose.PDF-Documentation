---
title: ضبط انتهاء صلاحية PDF في بايثون
linktitle: ضبط انتهاء صلاحية PDF في بايثون
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: تعرف على كيفية تعيين تاريخ انتهاء الصلاحية لملف PDF في Python باستخدام Aspose.PDF للوصول إلى المستندات الحساسة للوقت.
lastmod: "2026-06-09"
---
لتعيين انتهاء صلاحية مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```

** تنزيل كود التشغيل **

تنزيلВ **تعيين انتهاء صلاحية ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
