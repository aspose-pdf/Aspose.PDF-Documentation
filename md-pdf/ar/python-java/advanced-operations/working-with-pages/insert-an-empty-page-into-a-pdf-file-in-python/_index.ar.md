---
title: إدراج صفحة فارغة في ملف PDF باستخدام بايثون
type: docs
weight: 70
url: /python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء فئة **InsertEmptyPage**.

**كود بايثون**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# إدراج صفحة فارغة في PDF
pdf_document.getPages().insert(1)

# حفظ الملف الناتج المدمج (المستند الهدف)
pdf_document.save(self.dataDir + "output.pdf")

print "تم إضافة الصفحة الفارغة بنجاح!"

```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **إدراج صفحة فارغة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)