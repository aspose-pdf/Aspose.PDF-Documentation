---
title: احصل على بيانات تعريف XMP من ملف PDF في روبي
linktitle: احصل على بيانات تعريف XMP من ملف PDF في روبي
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: يمكنك الوصول إلى بيانات تعريف XMP ومعالجتها في مستندات PDF باستخدام Ruby مع Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على بيانات تعريف XMP

للحصول على بيانات تعريف XMP من مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetXMPMetadata**.

كود روبي

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

## تحميل كود التشغيل

تنزيل ** احصل على بيانات تعريف XMP (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
