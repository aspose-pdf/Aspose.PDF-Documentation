---
title: الحصول على بيانات XMP الوصفية من ملف PDF باستخدام Python
type: docs
weight: 50
url: ar/python-java/get-xmp-metadata-from-pdf-file-in-python/
---

<ins>للحصول على بيانات XMP الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **GetXMPMetadata**.

**كود بايثون**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على الخصائص
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**تنزيل الكود التشغيلي**

قم بتنزيل **الحصول على بيانات XMP الوصفية (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)