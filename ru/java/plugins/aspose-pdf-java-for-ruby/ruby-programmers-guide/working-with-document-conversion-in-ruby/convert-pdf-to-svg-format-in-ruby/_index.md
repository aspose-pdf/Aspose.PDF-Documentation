---
title: Конвертируйте PDF в формат SVG в Ruby
linktitle: Конвертируйте PDF в формат SVG в Ruby
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: Узнайте, как конвертировать PDF-файлы в формат SVG с помощью Ruby и Aspose.PDF, обеспечивая масштабируемую и редактируемую векторную графику.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF в SVG

Чтобы преобразовать PDF в формат SVG с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToSvg**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## Загрузите рабочий код

Загрузите **Конвертируйте PDF в формат SVG (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
