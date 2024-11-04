---
title: إضافة نص إلى ملف PDF موجود في روبي
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إضافة نص

لإضافة سلسلة نصية في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **AddText**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# إنشاء كائن المستند

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# الحصول على صفحة معينة

pdf_page = doc.getPages().get_Item(1)

# إنشاء جزء النص

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# ضبط خصائص النص

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# إنشاء كائن TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# إلحاق جزء النص بصفحة PDF

text_builder.appendText(text_fragment)

# حفظ ملف PDF

doc.save(data_dir + "Text_Added.pdf")

puts "تمت إضافة النص بنجاح"
```


## تنزيل الكود الجاري

قم بتنزيل **إضافة نص (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)