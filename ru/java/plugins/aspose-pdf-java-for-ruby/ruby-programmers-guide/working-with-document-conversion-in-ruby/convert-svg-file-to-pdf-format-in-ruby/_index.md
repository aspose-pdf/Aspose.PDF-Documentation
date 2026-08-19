---
title: Конвертировать файл SVG в формат PDF на Ruby
linktitle: Конвертировать файл SVG в формат PDF на Ruby
type: docs
weight: 60
url: /ru/java/convert-svg-file-to-pdf-format-in-ruby/
description: Узнайте, как конвертировать файлы SVG в формат PDF на Ruby с помощью Aspose.PDF для точного и масштабируемого преобразования документов.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать SVG в PDF

Чтобы конвертировать файл SVG в формат PDF с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **SvgToPdf**.

Код Ruby

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

## Скачать исполняемый код

СкачатьВ **Convert SVG to PDF (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)

