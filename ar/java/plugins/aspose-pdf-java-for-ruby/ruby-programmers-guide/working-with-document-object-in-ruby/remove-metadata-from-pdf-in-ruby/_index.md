---
title: إزالة البيانات الوصفية من PDF في Ruby
type: docs
weight: 90
url: ar/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إزالة البيانات الوصفية

لإزالة البيانات الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **RemoveMetadata**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# احفظ المستند المحدث بالمعلومات الجديدة

doc.save(data_dir + "Remove_Metadata.pdf")

puts "تمت إزالة البيانات الوصفية بنجاح، يرجى التحقق من ملف الإخراج."
```

## تنزيل الكود القابل للتشغيل

قم بتنزيل **إزالة البيانات الوصفية (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)