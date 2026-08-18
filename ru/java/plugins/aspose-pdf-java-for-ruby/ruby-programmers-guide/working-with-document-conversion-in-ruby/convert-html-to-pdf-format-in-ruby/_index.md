---
title: Преобразование HTML в формат PDF в Ruby
linktitle: Преобразование HTML в формат PDF в Ruby
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: Узнайте, как конвертировать содержимое HTML в формат PDF в Ruby с помощью Aspose.PDF для надежного и точного создания документов.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование HTML в формат PDF

Чтобы преобразовать HTML в формат PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **HtmlToPdf**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Конвертируйте HTML в формат PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
