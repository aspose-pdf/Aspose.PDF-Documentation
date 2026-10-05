---
title: تحديث أبعاد الصفحة في Ruby
linktitle: تحديث أبعاد الصفحة في Ruby
type: docs
weight: 90
url: /ar/java/update-page-dimensions-in-ruby/
description: اكتشف كيفية تحديث أبعاد صفحة مستند PDF باستخدام Ruby مع Aspose.PDF لتنسيق الصفحة بدقة.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحديث أبعاد الصفحة

لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for Ruby**، ببساطة استدعِ وحدة **UpdatePageDimensions**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## تنزيل الشيفرة الجارية

تنزيل **تحديث أبعاد الصفحة (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
