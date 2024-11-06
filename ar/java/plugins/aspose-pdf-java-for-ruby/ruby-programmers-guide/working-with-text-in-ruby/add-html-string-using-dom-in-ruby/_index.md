---
title: إضافة سلسلة HTML باستخدام DOM في Ruby
type: docs
weight: 10
url: ar/java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة HTML

لإضافة سلسلة HTML في وثيقة Pdf باستخدام **Aspose.PDF Java for Ruby**، يمكنك ببساطة استدعاء وحدة **AddHtml**.

كود Ruby

```java
# المسار إلى دليل الوثائق.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# إنشاء كائن Document

doc = Rjb::import('com.aspose.pdf.Document').new

# إضافة صفحة إلى مجموعة الصفحات في ملف PDF

page = doc.getPages().add()

# إنشاء HtmlFragment مع محتويات HTML

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# تعيين MarginInfo لتفاصيل الهوامش

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# تعيين معلومات الهوامش

title.setMargin(margin)

# إضافة جزء HTML إلى مجموعة الفقرات في الصفحة

page.getParagraphs().add(title)

# حفظ ملف PDF

doc.save(data_dir + "html.output.pdf")

puts "تمت إضافة HTML بنجاح"
```


## تحميل الكود الجاري

قم بتنزيل **إضافة HTML (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)