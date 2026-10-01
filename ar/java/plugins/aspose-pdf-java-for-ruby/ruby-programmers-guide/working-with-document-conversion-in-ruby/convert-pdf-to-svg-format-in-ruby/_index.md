---
title: تحويل PDF إلى تنسيق SVG في Ruby
linktitle: تحويل PDF إلى تنسيق SVG في Ruby
type: docs
weight: 50
url: /ar/java/convert-pdf-to-svg-format-in-ruby/
description: اكتشف كيفية تحويل ملفات PDF إلى تنسيق SVG باستخدام Ruby و Aspose.PDF، مما يتيح رسومات متجهة قابلة للتوسع والتحرير.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل PDF إلى SVG

لتحويل PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## تنزيل الكود قيد التشغيل

تحميلВ **تحويل PDF إلى تنسيق SVG (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
