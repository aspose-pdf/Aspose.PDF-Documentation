---
title: حذف صفحة معينة من ملف PDF باستخدام لغة بايثون
type: docs
weight: 20
url: ar/java/delete-a-particular-page-from-the-pdf-file-in-python/
lastmod: "2021-06-05"
---

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# حذف صفحة معينة
pdf.getPages().delete(2)

# حفظ ملف PDF الجديد
doc.save(self.dataDir + "output.pdf")

print "تم حذف الصفحة بنجاح!"

```

**تحميل الكود المشغل**

قم بتنزيل **Delete Page (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)