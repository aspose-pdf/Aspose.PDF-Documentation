---
title: الحصول على بيانات XMP الوصفية من ملف PDF في بايثون
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

للحصول على بيانات XMP الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# احصل على الخصائص
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**تحميل الكود الجاري**

قم بتحميل **الحصول على بيانات XMP (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)