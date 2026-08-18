---
title: احصل على معلومات ملف PDF في بايثون
linktitle: احصل على معلومات ملف PDF في بايثون
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: اكتشف كيفية استرداد معلومات ملف PDF التفصيلية مثل البيانات التعريفية والخصائص في Python باستخدام Aspose.PDF لإدارة المستندات.
lastmod: "2026-06-09"
---
للحصول على معلومات ملف مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **GetPdfFileInfo**.

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

** تنزيل كود التشغيل **

تنزيلВ **احصل على معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
