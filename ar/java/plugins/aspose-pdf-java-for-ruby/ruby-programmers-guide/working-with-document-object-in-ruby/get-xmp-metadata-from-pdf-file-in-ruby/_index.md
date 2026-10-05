---
title: الحصول على بيانات XMP الوصفية من ملف PDF في Ruby
linktitle: الحصول على بيانات XMP الوصفية من ملف PDF في Ruby
type: docs
weight: 60
url: /ar/java/get-xmp-metadata-from-pdf-file-in-ruby/
description: الوصول إلى بيانات XMP الوصفية ومعالجتها في مستندات PDF باستخدام Ruby مع Aspose.PDF.
lastmod: "2026-10-05"
---
## Aspose.PDF - الحصول على بيانات XMP الوصفية

للحصول على بيانات XMP الوصفية من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetXMPMetadata**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## تنزيل الكود الجاري

تنزيلВ **Get XMP Metadata (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
