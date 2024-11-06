---
title: تحديث أبعاد الصفحة في بايثون
type: docs
weight: 90
url: ar/java/update-page-dimensions-in-python/
lastmod: "2021-06-05"
---

لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على مجموعة الصفحات
page_collection = pdf.getPages()

# الحصول على صفحة معينة
pdf_page = page_collection.get_Item(1)

# تعيين حجم الصفحة إلى A4 (11.7 x 8.3 بوصة) وفي Aspose.PDF، 1 بوصة = 72 نقطة
# لذلك ستكون أبعاد A4 بالنقاط (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
pdf.save(self.dataDir + "output.pdf")

print "تم تحديث الأبعاد بنجاح!"

```

**تحميل الكود التنفيذي**

قم بتحميل **تحديث أبعاد الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)