---
title: تحويل HTML إلى تنسيق PDF في روبي
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل HTML إلى تنسيق PDF

لتحويل HTML إلى تنسيق PDF باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **HtmlToPdf**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# تحميل ملف HTML

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# حفظ الملف الناتج المدمج (المستند الهدف)

pdf.save(data_dir + "html.pdf")

puts "تم تحويل المستند بنجاح"
```

## تحميل كود التشغيل

قم بتحميل **تحويل HTML إلى تنسيق PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)