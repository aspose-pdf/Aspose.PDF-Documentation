---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام روبي
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - إدراج صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **InsertEmptyPageAtEndOfFile**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند المستهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# إدراج صفحة فارغة في ملف PDF

pdf.getPages().add()

# حفظ الملف الناتج المتكامل (المستند المستهدف)

pdf.save(data_dir+ "output.pdf")

puts "تمت إضافة الصفحة الفارغة بنجاح!"
```

## تحميل الكود الجاري

حمل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)