---
title: الحصول على معلومات ملف PDF في روبي
type: docs
weight: 50
url: ar/java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على معلومات ملف PDF

للحصول على معلومات ملف المستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **GetPdfFileInfo**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# احصل على معلومات المستند

doc_info = doc.getInfo()

# عرض معلومات المستند

puts "المؤلف:-" + doc_info.getAuthor().to_s

puts "تاريخ الإنشاء:-" + doc_info.getCreationDate().to_string

puts "الكلمات المفتاحية:-" + doc_info.getKeywords().to_s

puts "تاريخ التعديل:-" + doc_info.getModDate().to_string

puts "الموضوع:-" + doc_info.getSubject().to_s

puts "العنوان:-" + doc_info.getTitle().to_s
```

## تحميل الكود التشغيلي

قم بتحميل **الحصول على معلومات ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)

```ruby
# تحميل مستند PDF
pdf_document = Asposepdfjava::Document.new("input.pdf")

# الحصول على معلومات المستند
page_count = pdf_document.getPages().size()
creation_date = pdf_document.getInfo().getCreationDate()
author = pdf_document.getInfo().getAuthor()

# طباعة المعلومات
puts "عدد الصفحات: #{page_count}"
puts "تاريخ الإنشاء: #{creation_date}"
puts "المؤلف: #{author}"
`