---
title: تحويل HTML إلى تنسيق PDF في روبي
linktitle: تحويل HTML إلى تنسيق PDF في روبي
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: تعرف على كيفية تحويل محتوى HTML إلى تنسيق PDF في Ruby باستخدام Aspose.PDF لإنشاء مستندات موثوقة ودقيقة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل HTML إلى تنسيق PDF

لتحويل تنسيق HTML إلى PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **HtmlToPdf**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## تحميل كود التشغيل

تنزيل ** تحويل HTML إلى تنسيق PDF (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
