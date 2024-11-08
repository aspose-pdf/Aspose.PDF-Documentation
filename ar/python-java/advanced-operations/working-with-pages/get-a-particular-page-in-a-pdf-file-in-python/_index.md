---
title: احصل على صفحة معينة في ملف PDF باستخدام بايثون
type: docs
weight: 30
url: /ar/python-java/get-a-particular-page-in-a-pdf-file-in-python/
---

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء فئة **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# احصل على الصفحة عند الفهرس المحدد من مجموعة الصفحات
pdf_page = pdf.getPages().get_Item(1)

# إنشاء كائن مستند جديد
new_document = self.Document()

# إضافة الصفحة إلى مجموعة الصفحات لكائن المستند الجديد
new_document.getPages().add(pdf_page)

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
new_document.save(self.dataDir + "output.pdf")

print "تمت العملية بنجاح!

```

**تحميل الكود الجاري**

قم بتحميل **Get Page (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)