---
title: إضافة جدول محتويات إلى ملف PDF موجود في بايثون
type: docs
weight: 20
url: ar/java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

لإضافة جدول محتويات في مستند PDF باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء فئة **AddToc**.

```python

# افتح مستند PDF.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الوصول إلى الصفحة الأولى من ملف PDF
toc_page = doc.getPages().insert(1)

# إنشاء كائن لتمثيل معلومات جدول المحتويات
toc_info = self.TocInfo()
title = self.TextFragment("جدول المحتويات")
title.getTextState().setFontSize(20)

# تعيين العنوان لجدول المحتويات
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# إنشاء كائنات السلسلة التي ستستخدم كعناصر جدول المحتويات
titles = ["الصفحة الأولى", "الصفحة الثانية"]

i = 0;
while (i < 2):

# إنشاء كائن عنوان
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# تحديد الصفحة الوجهة لكائن العنوان
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# الصفحة الوجهة
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# إحداثيات الوجهة
segment2.setText(titles[i])

# إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
toc_page.getParagraphs().add(heading2)

i +=1;

# حفظ مستند PDF
doc.save(self.dataDir + "TOC.pdf")

print "تمت إضافة جدول المحتويات بنجاح، يرجى التحقق من ملف الإخراج."
```


**تحميل الكود الجاري**

قم بتنزيل **إضافة جدول المحتويات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)