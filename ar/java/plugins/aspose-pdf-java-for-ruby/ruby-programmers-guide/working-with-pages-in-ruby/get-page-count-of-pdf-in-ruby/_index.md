---
title: احصل على عدد صفحات PDF في روبي
linktitle: احصل على عدد صفحات PDF في روبي
type: docs
weight: 40
url: /ar/java/get-page-count-of-pdf-in-ruby/
description: استرجع العدد الإجمالي للصفحات في مستند PDF برمجيًا باستخدام روبي مع Aspose.PDF.
lastmod: "2026-10-01"
---
## Aspose.PDF - احصل على عدد الصفحات

للحصول على عدد صفحات مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الوحدة **GetNumberOfPages**.

كود روبي

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## تحميل الكود الجاري

تحميلВ **Get Page Count (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
