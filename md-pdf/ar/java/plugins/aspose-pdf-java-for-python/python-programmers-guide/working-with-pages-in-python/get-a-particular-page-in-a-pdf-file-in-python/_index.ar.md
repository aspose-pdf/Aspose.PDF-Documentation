---
title: الحصول على صفحة معينة في ملف PDF باستخدام لغة بايثون
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة استدع **GetPage** class.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على الصفحة في فهرس معين من مجموعة الصفحات
pdf_page = pdf.getPages().get_Item(1)

# إنشاء كائن مستند جديد
new_document = self.Document()

# إضافة الصفحة إلى مجموعة الصفحات في كائن المستند الجديد
new_document.getPages().add(pdf_page)

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
new_document.save(self.dataDir + "output.pdf")

print "تمت العملية بنجاح!

```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **Get Page (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)