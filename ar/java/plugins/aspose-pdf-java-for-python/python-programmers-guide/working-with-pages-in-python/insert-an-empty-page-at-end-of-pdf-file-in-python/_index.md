---
title: أدخل صفحة فارغة في نهاية ملف PDF في بايثون
linktitle: أدخل صفحة فارغة في نهاية ملف PDF في بايثون
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: اكتشف كيفية إدراج صفحة فارغة في نهاية مستند PDF في Python باستخدام Aspose.PDF لتوسيع المستند بسهولة.
lastmod: "2026-06-09"
---
لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

** تنزيل كود التشغيل **

قم بتنزيل **أدخل صفحة فارغة في نهاية ملف PDF (Aspose.PDF)**В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
