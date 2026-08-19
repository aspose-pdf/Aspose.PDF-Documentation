---
title: Преобразовать HTML в PDF-формат на Ruby
linktitle: Преобразовать HTML в PDF-формат на Ruby
type: docs
weight: 10
url: /ru/java/convert-html-to-pdf-format-in-ruby/
description: Узнайте, как конвертировать HTML-контент в формат PDF на Ruby с помощью Aspose.PDF для надёжного и точного создания документов.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать HTML в PDF-формат

Чтобы конвертировать HTML в PDF-формат, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **HtmlToPdf**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## Скачать работающий код

Скачать **Convert HTML to PDF Format (Aspose.PDF)** из любых из перечисленных ниже сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)

