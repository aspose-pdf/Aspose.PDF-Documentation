---
title: تحويل صفحات PDF إلى صور في Ruby
linktitle: تحويل صفحات PDF إلى صور في Ruby
type: docs
weight: 20
url: /ar/java/convert-pdf-pages-to-images-in-ruby/
description: اكتشف كيفية تحويل صفحات PDF إلى صور باستخدام Ruby مع Aspose.PDF، مما يجعل من السهل استخراج المحتوى المرئي من ملفات PDF.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل صفحات PDF إلى صور

لتحويل جميع الصفحات إلى صور من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **ConvertPagesToImages**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## تنزيل الكود الجاري

تنزيل **تحويل صفحات PDF إلى صور (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
