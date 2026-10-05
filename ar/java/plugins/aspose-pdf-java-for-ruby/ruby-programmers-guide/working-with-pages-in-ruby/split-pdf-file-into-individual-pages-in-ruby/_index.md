---
title: تقسيم ملف PDF إلى صفحات فردية باستخدام Ruby
linktitle: تقسيم ملف PDF إلى صفحات فردية باستخدام Ruby
type: docs
weight: 80
url: /ar/java/split-pdf-file-into-individual-pages-in-ruby/
description: تعرّف على كيفية تقسيم ملف PDF إلى صفحات فردية باستخدام Ruby و Aspose.PDF، مما يجعل إدارة المحتوى واستخلاصه أسهل.
lastmod: "2026-10-05"
---
## Aspose.PDF - تقسيم الصفحات

لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **SplitAllPages**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## تنزيل الكود الجاري

تحميل **Split Pages (Aspose.PDF)** من من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
