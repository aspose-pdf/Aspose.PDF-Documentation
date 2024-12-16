---
title: حذف صفحة معينة من ملف PDF في بايثون
type: docs
weight: 20
url: /ar/python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة استدع فئة **DeletePage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# حذف صفحة معينة
pdf.getPages().delete(2)

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
doc.save(self.dataDir + "output.pdf")

print "تم حذف الصفحة بنجاح!"

```

**تحميل الكود التشغيلي**

قم بتحميل **حذف الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)