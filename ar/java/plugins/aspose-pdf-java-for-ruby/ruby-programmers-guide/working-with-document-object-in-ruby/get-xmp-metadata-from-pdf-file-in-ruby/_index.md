---
title: الحصول على بيانات XMP الوصفية من ملف PDF في روبي
type: docs
weight: 60
url: ar/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على بيانات XMP الوصفية

للحصول على بيانات XMP الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **GetXMPMetadata**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# الحصول على الخصائص

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## تنزيل الكود التشغيلي

قم بتنزيل **الحصول على بيانات XMP الوصفية (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)