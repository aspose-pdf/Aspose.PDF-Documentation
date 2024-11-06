---
title: إدراج صفحة فارغة في ملف PDF باستخدام روبي
type: docs
weight: 70
url: ar/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إدراج صفحة فارغة

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **InsertEmptyPage**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# إدراج صفحة فارغة في ملف PDF

pdf.getPages().insert(1)

# حفظ الملف الناتج المدمج (المستند الهدف)

pdf.save(data_dir+ "output.pdf")

puts "تمت إضافة الصفحة الفارغة بنجاح!"
```

## تنزيل الكود الجاري

قم بتنزيل **إدراج صفحة فارغة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)