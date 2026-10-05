---
title: تحويل HTML إلى تنسيق PDF في Ruby
linktitle: تحويل HTML إلى تنسيق PDF في Ruby
type: docs
weight: 10
url: /ar/java/convert-html-to-pdf-format-in-ruby/
description: تعرف على كيفية تحويل محتوى HTML إلى تنسيق PDF في Ruby باستخدام Aspose.PDF لتوليد مستندات موثوقة ودقيقة.
lastmod: "2026-10-05"
---
## Aspose.PDF - تحويل HTML إلى تنسيق PDF

لتحويل HTML إلى تنسيق PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **HtmlToPdf**.

كود Ruby

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

## تحميل الكود الجاري

تحميل **تحويل HTML إلى تنسيق PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
