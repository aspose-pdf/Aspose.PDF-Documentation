---
title: تحويل PDF إلى تنسيق SVG في روبي
linktitle: تحويل PDF إلى تنسيق SVG في روبي
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: تعرف على كيفية تحويل ملفات PDF إلى تنسيق SVG باستخدام Ruby وAspose.PDF، مما يتيح رسومات متجهة قابلة للتحجيم والتحرير.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل PDF إلى SVG

لتحويل تنسيق PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

كود روبي

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

## تحميل كود التشغيل

تنزيل В ** تحويل PDF إلى تنسيق SVG (Aspose.PDF)** В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
