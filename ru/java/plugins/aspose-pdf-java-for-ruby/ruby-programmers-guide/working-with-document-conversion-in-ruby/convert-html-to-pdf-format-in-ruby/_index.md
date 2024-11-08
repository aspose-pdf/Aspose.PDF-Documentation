---
title: Преобразование HTML в формат PDF на Ruby
type: docs
weight: 10
url: /ru/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование HTML в формат PDF

Чтобы преобразовать HTML в формат PDF с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **HtmlToPdf**.

Код на Ruby

```java

# Путь к каталогу с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Загрузить HTML файл

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Сохранить объединенный выходной файл (целевой документ)

pdf.save(data_dir + "html.pdf")

puts "Документ успешно преобразован"
```

## Скачать выполняемый код

Скачать **Преобразование HTML в формат PDF (Aspose.PDF)** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)