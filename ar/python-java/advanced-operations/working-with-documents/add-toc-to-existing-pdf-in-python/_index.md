---
title: إضافة جدول محتويات إلى PDF موجود باستخدام بايثون
type: docs
weight: 20
url: /ar/python-java/add-toc-to-existing-pdf-in-python/
---

لإضافة جدول محتويات في مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **AddToc**.

```python

# فتح مستند pdf.
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

# إنشاء كائنات نصية سيتم استخدامها كعناصر في جدول المحتويات
titles = ["الصفحة الأولى", "الصفحة الثانية"]

i = 0;
while (i < 2):

# إنشاء كائن العنوان
heading2 = self.Heading(1)

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# تحديد الصفحة الهدف لكائن العنوان
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# الصفحة الهدف
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# تحديد الإحداثي الهدف
segment2.setText(titles[i])

# إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
toc_page.getParagraphs().add(heading2)

i +=1

# حفظ مستند PDF
doc.save(self.dataDir + "TOC.pdf")

print "تمت إضافة جدول المحتويات بنجاح، يرجى التحقق من ملف الإخراج."
```


**تحميل الكود الجاري**

قم بتنزيل **إضافة جدول محتويات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)