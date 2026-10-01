---
title: استخراج بيانات XMP الوصفية من ملف PDF في بايثون
linktitle: استخراج بيانات XMP الوصفية من ملف PDF في بايثون
type: docs
weight: 50
url: /ar/java/get-xmp-metadata-from-pdf-file-in-python/
description: اكتشف كيفية استرجاع بيانات XMP الوصفية من ملف PDF في بايثون باستخدام Aspose.PDF، مما يتيح تحليلًا مفصّلاً للمحتوى.
lastmod: "2026-10-01"
---
للحصول على بيانات XMP الوصفية من مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**تحميل الكود الجاري**

تنزيلВ **احصل على بيانات XMP الوصفية (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
