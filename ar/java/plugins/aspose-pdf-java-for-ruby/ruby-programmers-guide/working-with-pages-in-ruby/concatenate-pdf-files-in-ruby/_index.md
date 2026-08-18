---
title: تسلسل ملفات PDF في روبي
linktitle: تسلسل ملفات PDF في روبي
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: قم بدمج ملفات PDF متعددة في مستند واحد باستخدام Ruby وAspose.PDF بكفاءة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تسلسل ملفات PDF

لتسلسل ملفات PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **ConcatenatePdfFiles**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## تحميل كود التشغيل

تنزيل В ** تسلسل ملفات PDF (Aspose.PDF)** В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
