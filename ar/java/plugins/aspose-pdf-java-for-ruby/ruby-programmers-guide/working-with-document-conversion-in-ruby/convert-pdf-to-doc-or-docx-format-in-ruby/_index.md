---
title: تحويل PDF إلى تنسيق DOC أو DOCX في روبي
linktitle: تحويل PDF إلى تنسيق DOC أو DOCX في روبي
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: تعرف على كيفية تحويل مستندات PDF إلى تنسيقات DOC أو DOCX في Ruby باستخدام Aspose.PDF، مما يتيح سهولة التحرير والمعالجة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل PDF إلى DOC أو DOCX

لتحويل مستند PDF إلى تنسيق DOC أو DOCX باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **PdfToDoc**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## تحميل كود التشغيل

تنزيل ** تحويل PDF إلى DOC أو DOCX (Aspose.PDF) **В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
