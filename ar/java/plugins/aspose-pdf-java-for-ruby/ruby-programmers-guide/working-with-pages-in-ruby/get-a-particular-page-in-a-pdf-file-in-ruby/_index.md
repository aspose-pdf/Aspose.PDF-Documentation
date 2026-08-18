---
title: احصل على صفحة معينة في ملف PDF في روبي
linktitle: احصل على صفحة معينة في ملف PDF في روبي
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: يمكنك الوصول إلى الصفحات الفردية في مستندات PDF ومعالجتها باستخدام Ruby وAspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على الصفحة

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **GetPage**.

كود روبي

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

## تحميل كود التشغيل

قم بتنزيل **الحصول على الصفحة (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
