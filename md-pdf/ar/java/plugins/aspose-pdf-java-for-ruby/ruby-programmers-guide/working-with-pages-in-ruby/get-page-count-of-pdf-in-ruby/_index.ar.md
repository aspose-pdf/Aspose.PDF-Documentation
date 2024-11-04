---
title: الحصول على عدد صفحات PDF في روبي
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على عدد الصفحات

للحصول على عدد صفحات مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **GetNumberOfPages**.

كود روبي

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# إنشاء مستند PDF

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "عدد الصفحات:" + page_count.to_s
```

## تحميل الكود التشغيلي

قم بتحميل **الحصول على عدد الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)