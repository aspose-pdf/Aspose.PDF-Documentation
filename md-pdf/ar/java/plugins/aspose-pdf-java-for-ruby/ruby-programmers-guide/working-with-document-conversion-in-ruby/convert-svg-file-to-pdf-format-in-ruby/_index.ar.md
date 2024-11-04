---
title: تحويل ملف SVG إلى تنسيق PDF في روبي
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل SVG إلى PDF

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for Ruby**، قم فقط باستدعاء وحدة **SvgToPdf**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# إنشاء كائن LoadOption باستخدام خيار تحميل SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# إنشاء كائن المستند

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# حفظ الناتج بتنسيق XLS

pdf.save(data_dir + "SVG.pdf")

puts "تم تحويل المستند بنجاح"
```

## تنزيل الكود العامل

قم بتنزيل **تحويل SVG إلى PDF (Aspose.PDF)** من أي من مواقع التشفير الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)