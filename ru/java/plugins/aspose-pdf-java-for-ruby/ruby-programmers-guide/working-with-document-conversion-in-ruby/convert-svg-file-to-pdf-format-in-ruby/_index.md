---
title: Преобразование файла SVG в формат PDF на Ruby
type: docs
weight: 60
url: ru/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование SVG в PDF

Чтобы преобразовать файл SVG в формат PDF с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **SvgToPdf**.

Код на Ruby

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Создать объект LoadOption, используя опцию загрузки SVG

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Создать объект документа

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Сохранить вывод в формате XLS

pdf.save(data_dir + "SVG.pdf")

puts "Документ был успешно преобразован"
```

## Скачать выполняемый код

Скачайте **Convert SVG to PDF (Aspose.PDF)** с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)