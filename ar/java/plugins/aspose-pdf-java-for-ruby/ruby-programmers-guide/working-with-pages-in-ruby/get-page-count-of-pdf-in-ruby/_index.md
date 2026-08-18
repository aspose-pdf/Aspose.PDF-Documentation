---
title: احصل على عدد صفحات ملف PDF في روبي
linktitle: احصل على عدد صفحات ملف PDF في روبي
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: يمكنك استرداد العدد الإجمالي للصفحات في مستند PDF برمجيًا باستخدام Ruby مع Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على عدد الصفحات

للحصول على عدد صفحات مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetNumberOfPages**.

كود روبي

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## تحميل كود التشغيل

تنزيلВ **احصل على عدد الصفحات (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
