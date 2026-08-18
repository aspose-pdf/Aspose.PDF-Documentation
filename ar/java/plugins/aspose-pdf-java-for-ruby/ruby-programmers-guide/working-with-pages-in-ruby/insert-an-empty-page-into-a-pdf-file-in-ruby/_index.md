---
title: أدخل صفحة فارغة في ملف PDF في روبي
linktitle: أدخل صفحة فارغة في ملف PDF في روبي
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: تعرف على كيفية إدراج صفحة فارغة في موقع محدد داخل مستند PDF باستخدام Ruby وAspose.PDF لإدارة المستندات بدقة.
lastmod: "2026-06-09"
---
## Aspose.PDF - أدخل صفحة فارغة

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **InsertEmptyPage**.

كود روبي

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

## تحميل كود التشغيل

تنزيلВ **أدخل صفحة فارغة (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
