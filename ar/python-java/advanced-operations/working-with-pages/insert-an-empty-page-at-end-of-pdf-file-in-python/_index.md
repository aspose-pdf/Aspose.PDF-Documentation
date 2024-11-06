---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام بايثون
type: docs
weight: 60
url: ar/python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة استدعاء فئة **InsertEmptyPageAtEndOfFile**.

**كود بايثون**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# إدراج صفحة فارغة في ملف PDF
pdf_document.getPages().add();

# حفظ الملف الناتج (المستند المستهدف)
pdf_document.save(self.dataDir + "output.pdf")

print "تمت إضافة الصفحة الفارغة بنجاح!"

```

**تحميل الكود القابل للتشغيل**

قم بتحميل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)