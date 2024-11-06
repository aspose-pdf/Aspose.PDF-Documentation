---
title: الحصول على معلومات ملف PDF في بايثون
type: docs
weight: 40
url: ar/java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

للحصول على معلومات ملف مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على معلومات المستند
doc_info = doc.getInfo();

# عرض معلومات المستند
print "المؤلف:-" + str(doc_info.getAuthor())
print "تاريخ الإنشاء:-" + str(doc_info.getCreationDate())
print "الكلمات المفتاحية:-" + str(doc_info.getKeywords())
print "تاريخ التعديل:-" + str(doc_info.getModDate())
print "الموضوع:-" + str(doc_info.getSubject())
print "العنوان:-" + str(doc_info.getTitle())
```

**تنزيل الكود الجاري**

قم بتنزيل **الحصول على معلومات ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)