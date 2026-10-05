---
title: إدراج صفحة فارغة في ملف PDF باستخدام Ruby
linktitle: إدراج صفحة فارغة في ملف PDF باستخدام Ruby
type: docs
weight: 70
url: /ar/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: تعرف على كيفية إدراج صفحة فارغة في موقع محدد داخل مستند PDF باستخدام Ruby وAspose.PDF لإدارة مستندات دقيقة.
lastmod: "2026-10-01"
---
## Aspose.PDF - إدراج صفحة فارغة

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الوحدة **InsertEmptyPage**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## تنزيل الكود الجاري

تنزيل\u0412\u00A0**إدراج صفحة فارغة (Aspose.PDF)**\u0412\u00A0من\u0412\u00A0أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
