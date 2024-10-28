---
title: إزالة البيانات الوصفية من PDF في بايثون
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
lastmod: "2021-06-05"
---

لإزالة البيانات الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# حفظ المستند المحدث بالمعلومات الجديدة
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "تمت إزالة البيانات الوصفية بنجاح، يرجى التحقق من ملف الإخراج."

```

**تنزيل الكود التشغيلي**

قم بتنزيل **Remove Metadata (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)