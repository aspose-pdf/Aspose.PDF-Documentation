---
title: أدخل صفحة فارغة في نهاية ملف PDF في روبي
linktitle: أدخل صفحة فارغة في نهاية ملف PDF في روبي
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: اكتشف كيفية إدراج صفحة فارغة في نهاية مستند PDF باستخدام Ruby مع Aspose.PDF، مما يضيف المرونة إلى مهام معالجة PDF الخاصة بك.
lastmod: "2026-06-09"
---
## Aspose.PDF - أدخل صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الوحدة النمطية **InsertEmptyPageAtEndOfFile**.

كود روبي

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

## تحميل كود التشغيل

قم بتنزيل **أدخل صفحة فارغة في نهاية ملف PDF (Aspose.PDF)**В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
