---
title: إضافة جدول محتويات إلى ملف PDF موجود في روبي
type: docs
weight: 30
url: ar/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة جدول محتويات

<ins>لإضافة جدول محتويات في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **AddToc**.

كود روبي

```java
# مسار دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# الوصول إلى الصفحة الأولى من ملف PDF

toc_page = doc.getPages().insert(1)

# إنشاء كائن لتمثيل معلومات جدول المحتويات

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("جدول المحتويات")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# تعيين العنوان لجدول المحتويات

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# إنشاء كائنات سلسلة ستستخدم كعناصر جدول المحتويات

titles = Array["الصفحة الأولى", "الصفحة الثانية"]

i = 0

while i < 2

    # إنشاء كائن عنوان

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # تحديد الصفحة الوجهة لكائن العنوان

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # صفحة الوجهة

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # إحداثيات الوجهة

    segment2.setText(titles[i])

    # إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# حفظ مستند PDF

doc.save(data_dir + "TOC.pdf")

puts "تمت إضافة جدول المحتويات بنجاح، يرجى التحقق من ملف الإخراج."
```


## <ins> **تحميل كود التشغيل

قم بتنزيل **إضافة جدول المحتويات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)