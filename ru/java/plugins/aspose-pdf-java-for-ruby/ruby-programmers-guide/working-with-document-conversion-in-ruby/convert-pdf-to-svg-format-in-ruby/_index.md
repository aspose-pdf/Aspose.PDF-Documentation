---
title: Конвертировать PDF в формат SVG на Ruby
type: docs
weight: 50
url: ru/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Конвертация PDF в SVG

Чтобы конвертировать PDF в формат SVG, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **PdfToSvg**.

Код на Ruby

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# создать объект SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# не сжимать изображение SVG в архив Zip

save_options.CompressOutputToZipArchive = false

# Сохранить вывод в формате XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "Документ был успешно преобразован"
```

## Скачать исполняемый код

Скачайте **Конвертировать PDF в формат SVG (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)