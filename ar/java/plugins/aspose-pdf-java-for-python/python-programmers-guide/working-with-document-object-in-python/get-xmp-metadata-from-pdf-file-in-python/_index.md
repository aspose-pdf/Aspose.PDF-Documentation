---
title: احصل على بيانات تعريف XMP من ملف PDF في Python
linktitle: احصل على بيانات تعريف XMP من ملف PDF في Python
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: اكتشف كيفية استرداد بيانات تعريف XMP من ملف PDF في Python باستخدام Aspose.PDF، مما يتيح تحليل المحتوى التفصيلي.
lastmod: "2026-06-09"
---
للحصول على بيانات تعريف XMP من مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

** تنزيل كود التشغيل **

تنزيل ** احصل على بيانات تعريف XMP (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
