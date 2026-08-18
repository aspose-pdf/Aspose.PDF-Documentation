---
title: Конвертировать файл SVG в формат PDF в Ruby
linktitle: Конвертировать файл SVG в формат PDF в Ruby
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: Узнайте, как конвертировать файлы SVG в формат PDF в Ruby с помощью Aspose.PDF для точного и масштабируемого преобразования документов.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование SVG в PDF

Чтобы преобразовать файл SVG в формат PDF с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **SvgToPdf**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## Загрузите рабочий код

Загрузите **Конвертируйте SVG в PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
