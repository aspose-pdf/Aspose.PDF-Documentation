---
title: تعيين انتهاء صلاحية PDF في Python
linktitle: تعيين انتهاء صلاحية PDF في Python
type: docs
weight: 80
url: /ar/java/set-pdf-expiration-in-python/
description: تعلم كيفية تعيين تاريخ انتهاء صلاحية لملف PDF في Python باستخدام Aspose.PDF للوصول إلى المستندات الحساسة للوقت.
lastmod: "2026-10-05"
---
لتعيين انتهاء صلاحية of  Pdf document باستخدام **Aspose.PDF Java for Python**، ببساطة استدعِ الفئة **SetExpiration**.

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

**تنزيل الشفرة القابلة للتشغيل**

تحميل **تعيين انتهاء صلاحية PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
