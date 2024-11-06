---
title: Преобразование страниц PDF в изображения на Ruby
type: docs
weight: 20
url: ru/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование страниц PDF в изображения

Чтобы преобразовать все страницы PDF-документа в изображения с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **ConvertPagesToImages**.

Код на Ruby

```java

# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "Страницы PDF успешно преобразованы в отдельные изображения!"
```

## Скачать работающий код

Скачайте **Преобразование страниц PDF в изображения (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)