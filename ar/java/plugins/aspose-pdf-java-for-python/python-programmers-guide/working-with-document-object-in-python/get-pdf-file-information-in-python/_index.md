---
title: احصل على معلومات ملف PDF في Python
linktitle: احصل على معلومات ملف PDF في Python
type: docs
weight: 40
url: /ar/java/get-pdf-file-information-in-python/
description: استكشف كيفية استرداد معلومات ملف PDF التفصيلية مثل البيانات الوصفية والخصائص في Python باستخدام Aspose.PDF لإدارة المستندات.
lastmod: "2026-10-01"
---
للحصول على معلومات ملف Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة استدعِ الفئة **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**تحميل الشيفرة قيد التشغيل**

تحميلВ **احصل على معلومات ملف PDF (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
