---
title: أدخل صفحة فارغة في ملف PDF في بايثون
linktitle: أدخل صفحة فارغة في ملف PDF في بايثون
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
description: تعرف على كيفية إدراج صفحة فارغة في أي موضع داخل ملف PDF باستخدام Python وAspose.PDF لتنظيم مرن للمستندات.
lastmod: "2026-06-09"
---
لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

** تنزيل كود التشغيل **

تنزيلВ **أدخل صفحة فارغة (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
