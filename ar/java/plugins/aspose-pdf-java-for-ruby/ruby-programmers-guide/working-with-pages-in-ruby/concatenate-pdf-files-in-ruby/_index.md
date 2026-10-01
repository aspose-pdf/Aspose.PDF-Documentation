---
title: دمج ملفات PDF في روبي
linktitle: دمج ملفات PDF في روبي
type: docs
weight: 10
url: /ar/java/concatenate-pdf-files-in-ruby/
description: الجمع بين ملفات PDF متعددة في مستند واحد باستخدام روبي و Aspose.PDF بكفاءة.
lastmod: "2026-10-01"
---
## Aspose.PDF - دمج ملفات PDF

لتجميع ملفات PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **ConcatenatePdfFiles**.

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

## تنزيل الكود الجاري

تحميلВ **Concatenate PDF Files (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
