---
title: الحصول على صفحة معينة في ملف PDF باستخدام روبي
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على صفحة

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetPage**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند المستهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# احصل على الصفحة عند فهرس معين من مجموعة الصفحات

pdf_page = pdf.getPages().get_Item(1)

# أنشئ كائن مستند جديد

new_document = Rjb::import('com.aspose.pdf.Document').new

# إضافة الصفحة إلى مجموعة الصفحات في كائن المستند الجديد

new_document.getPages().add(pdf_page)

# احفظ ملف PDF الذي تم إنشاؤه حديثًا

new_document.save(data_dir + "output.pdf")

puts "تمت العملية بنجاح!"
```

## تنزيل الكود الجاري

قم بتنزيل **Get Page (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)