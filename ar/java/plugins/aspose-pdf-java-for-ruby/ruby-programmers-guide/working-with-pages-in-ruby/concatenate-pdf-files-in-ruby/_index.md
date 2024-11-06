---
title: دمج ملفات PDF في روبي
type: docs
weight: 10
url: ar/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - دمج ملفات PDF

لدمج ملفات PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة استدعِ وحدة **ConcatenatePdfFiles**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# افتح المستند المصدر

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# أضف صفحات المستند المصدر إلى المستند الهدف

pdf1.getPages().add(pdf2.getPages())

# احفظ الملف الناتج المدمج (المستند الهدف)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "تم حفظ المستند الجديد، يرجى التحقق من ملف الإخراج"
```

## تحميل الكود الجاري

قم بتحميل **دمج ملفات PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)

```ruby
# تحميل مستندات PDF
doc1 = Aspose::Pdf::Document.new("Document1.pdf")
doc2 = Aspose::Pdf::Document.new("Document2.pdf")

# دمج المستندات
doc1.pages.add(doc2.pages)

# حفظ المستند المدمج
doc1.save("MergedDocument.pdf")
```

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)

```ruby
# تحميل مستند PDF
pdf_document = Aspose::Pdf::Document.new("Input.pdf")

# الحصول على عدد الصفحات
page_count = pdf_document.pages.count

# طباعة عدد الصفحات
puts "عدد الصفحات: #{page_count}"