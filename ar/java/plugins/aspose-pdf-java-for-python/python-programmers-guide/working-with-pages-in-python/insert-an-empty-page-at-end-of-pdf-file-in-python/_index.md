---
title: إدراج صفحة فارغة في نهاية ملف PDF في بايثون
linktitle: إدراج صفحة فارغة في نهاية ملف PDF في بايثون
type: docs
weight: 60
url: /ar/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: اكتشف كيف يمكنك إدراج صفحة فارغة في نهاية مستند PDF باستخدام بايثون مع Aspose.PDF لتوسيع المستند بسهولة.
lastmod: "2026-10-01"
---
لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة استدعِ الفئة **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**تحميل الكود التشغيلي**

تحميل **Insert an Empty Page at End of PDF File (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
