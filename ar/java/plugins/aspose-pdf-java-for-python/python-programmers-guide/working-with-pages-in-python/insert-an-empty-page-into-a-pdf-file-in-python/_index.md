---
title: إدراج صفحة فارغة في ملف PDF باستخدام بايثون
type: docs
weight: 70
url: ar/java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# إدراج صفحة فارغة في ملف PDF
pdf_document.getPages().insert(1)

# احفظ الملف الناتج المدمج (المستند الهدف)
pdf_document.save(self.dataDir + "output.pdf")

print "تمت إضافة الصفحة الفارغة بنجاح!"

```

**تحميل الكود القابل للتشغيل**

قم بتحميل **إدراج صفحة فارغة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)