---
title: احصل على معلومات ملف PDF في روبي
linktitle: احصل على معلومات ملف PDF في روبي
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: قم باستخراج البيانات التعريفية والتفاصيل من ملفات PDF برمجياً باستخدام Aspose.PDF في Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على معلومات ملف PDF

للحصول على معلومات ملف مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetPdfFileInfo**.

كود روبي

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

## تحميل كود التشغيل

تنزيلВ **احصل على معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
