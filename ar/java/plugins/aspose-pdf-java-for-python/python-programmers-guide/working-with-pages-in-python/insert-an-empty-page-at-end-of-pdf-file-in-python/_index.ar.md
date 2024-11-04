---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام بايثون
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# إدراج صفحة فارغة في ملف PDF
pdf_document.getPages().add();

# حفظ ملف الإخراج المدمج (المستند الهدف)
pdf_document.save(self.dataDir + "output.pdf")

print "تمت إضافة الصفحة الفارغة بنجاح!"

```

**تحميل كود التشغيل**

قم بتحميل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)