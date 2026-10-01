---
title: الحصول على معلومات ملف PDF في Ruby
linktitle: الحصول على معلومات ملف PDF في Ruby
type: docs
weight: 50
url: /ar/java/get-pdf-file-information-in-ruby/
description: استخراج البيانات الوصفية والتفاصيل من ملفات PDF برمجيًا باستخدام Aspose.PDF في Ruby.
lastmod: "2026-10-01"
---
## Aspose.PDF - الحصول على معلومات ملف PDF

للحصول على معلومات ملف PDF المستند باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetPdfFileInfo**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## تنزيل الكود الجاري

تنزيل **Get PDF File Information (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
