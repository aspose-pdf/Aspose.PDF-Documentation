---
title: Преобразование HTML в PDF-формат на Ruby
linktitle: Преобразование HTML в PDF-формат на Ruby
type: docs
weight: 10
url: /ru/java/convert-html-to-pdf-format-in-ruby/
description: Узнайте, как конвертировать HTML-контент в формат PDF на Ruby с помощью Aspose.PDF для надёжного и точного создания документов.
lastmod: "2026-09-17"
---
## Aspose.PDF - Конвертация HTML в PDF-формат

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

## Загрузка работающего кода

Скачайте **Convert HTML to PDF Format (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)


