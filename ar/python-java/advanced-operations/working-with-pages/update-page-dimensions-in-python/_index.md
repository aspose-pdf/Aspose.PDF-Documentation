---
title: تحديث أبعاد الصفحة في Python
type: docs
weight: 90
url: ar/python-java/update-page-dimensions-in-python/
---

<ins>لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **UpdatePageDimensions**.

**كود بايثون**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على مجموعة الصفحات
page_collection = pdf.getPages()

# الحصول على صفحة معينة
pdf_page = page_collection.get_Item(1)

# تعيين حجم الصفحة كـ A4 (11.7 x 8.3 بوصة) وفي Aspose.PDF، 1 بوصة = 72 نقطة
# لذا فإن أبعاد A4 بالنقاط ستكون (842.4، 597.6)
pdf_page.setPageSize(597.6,842.4)

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
pdf.save(self.dataDir + "output.pdf")

print "تم تحديث الأبعاد بنجاح!"

```

**تحميل الكود الجاري**

قم بتحميل **تحديث أبعاد الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)