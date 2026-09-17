---
title: Преобразование страниц PDF в изображения на Ruby
linktitle: Преобразование страниц PDF в изображения на Ruby
type: docs
weight: 20
url: /ru/java/convert-pdf-pages-to-images-in-ruby/
description: Узнайте, как конвертировать страницы PDF в изображения с помощью Ruby и Aspose.PDF, что упрощает извлечение визуального содержимого из PDF.
lastmod: "2026-09-17"
---
## Aspose.PDF — Конвертация страниц PDF в изображения

Чтобы конвертировать все страницы PDF‑документа в изображения, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **ConvertPagesToImages**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## Загрузка работающего кода

Скачайте **Convert PDF pages to Images (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)


