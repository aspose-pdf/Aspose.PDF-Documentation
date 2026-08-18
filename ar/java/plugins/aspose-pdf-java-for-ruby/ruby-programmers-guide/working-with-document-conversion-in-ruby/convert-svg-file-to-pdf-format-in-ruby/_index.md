---
title: تحويل ملف SVG إلى تنسيق PDF في روبي
linktitle: تحويل ملف SVG إلى تنسيق PDF في روبي
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: تعرف على كيفية تحويل ملفات SVG إلى تنسيق PDF في Ruby باستخدام Aspose.PDF لتحويل المستندات بشكل دقيق وقابل للتطوير.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل SVG إلى PDF

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **SvgToPdf**.

كود روبي

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

## تحميل كود التشغيل

تنزيل В **تحويل SVG إلى PDF (Aspose.PDF)** В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
