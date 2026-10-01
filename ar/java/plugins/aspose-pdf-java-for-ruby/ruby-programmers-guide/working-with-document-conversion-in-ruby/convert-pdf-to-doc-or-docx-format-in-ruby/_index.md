---
title: تحويل PDF إلى تنسيق DOC أو DOCX في Ruby
linktitle: تحويل PDF إلى تنسيق DOC أو DOCX في Ruby
type: docs
weight: 30
url: /ar/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: تعلم كيفية تحويل مستندات PDF إلى تنسيقات DOC أو DOCX في Ruby باستخدام Aspose.PDF، مما يتيح تحريرًا ومعالجة أسهل.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل PDF إلى DOC أو DOCX

لتحويل مستند PDF إلى تنسيق DOC أو DOCX باستخدام **Aspose.PDF Java for Ruby**، يكفي استدعاء وحدة **PdfToDoc**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## تحميل الكود الجاري

تحميل **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
