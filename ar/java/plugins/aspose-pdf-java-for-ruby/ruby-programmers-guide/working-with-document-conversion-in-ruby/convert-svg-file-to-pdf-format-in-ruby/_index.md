---
title: تحويل ملف SVG إلى تنسيق PDF في Ruby
linktitle: تحويل ملف SVG إلى تنسيق PDF في Ruby
type: docs
weight: 60
url: /ar/java/convert-svg-file-to-pdf-format-in-ruby/
description: تعرف على كيفية تحويل ملفات SVG إلى تنسيق PDF في Ruby باستخدام Aspose.PDF للحصول على تحويل مستندات دقيق وقابل للتوسع.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل SVG إلى PDF

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **SvgToPdf**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## تنزيل الكود الجاري

تحميلВ **Convert SVG to PDF (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
