---
title: إدراج صفحة فارغة في ملف PDF باستخدام Python
linktitle: إدراج صفحة فارغة في ملف PDF باستخدام Python
type: docs
weight: 70
url: /ar/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: تعرّف على كيفية إدراج صفحة فارغة في أي موضع داخل ملف PDF باستخدام Python و Aspose.PDF لتكويد المستندات بمرونة.
lastmod: "2026-10-05"
---
لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **InsertEmptyPage**.

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

**تنزيل الشفرة القابلة للتشغيل**

Download **إدراج صفحة فارغة (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
