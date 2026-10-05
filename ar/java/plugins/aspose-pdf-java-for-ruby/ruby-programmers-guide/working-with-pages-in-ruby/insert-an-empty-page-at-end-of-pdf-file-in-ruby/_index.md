---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام Ruby
linktitle: إدراج صفحة فارغة في نهاية ملف PDF باستخدام Ruby
type: docs
weight: 60
url: /ar/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: اكتشف كيفية إدراج صفحة فارغة في نهاية مستند PDF باستخدام Ruby و Aspose.PDF، مما يضيف مرونة إلى مهام معالجة ملفات PDF الخاصة بك.
lastmod: "2026-10-05"
---
## Aspose.PDF - إدراج صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **InsertEmptyPageAtEndOfFile**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## تحميل الكود المشغَّل

تحميل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
