---
title: حذف صفحة معينة من ملف PDF في روبي
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - حذف الصفحة

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **DeletePage**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند المستهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# حذف صفحة معينة

pdf.getPages().delete(2)

# احفظ ملف PDF الذي تم إنشاؤه حديثًا

pdf.save(data_dir + "output.pdf")

puts "تم حذف الصفحة بنجاح!"
```

## تحميل الكود الجاري

قم بتحميل **حذف الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)