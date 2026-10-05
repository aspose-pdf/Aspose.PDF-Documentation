---
title: الحصول على صفحة محددة في ملف PDF باستخدام Ruby
linktitle: الحصول على صفحة محددة في ملف PDF باستخدام Ruby
type: docs
weight: 30
url: /ar/java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: الوصول إلى الصفحات الفردية وتعديلها في مستندات PDF باستخدام Ruby و Aspose.PDF.
lastmod: "2026-10-01"
---
## Aspose.PDF - الحصول على صفحة

للحصول على صفحة محددة في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetPage**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## تحميل الكود الجاري

تحميل **Get Page (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
