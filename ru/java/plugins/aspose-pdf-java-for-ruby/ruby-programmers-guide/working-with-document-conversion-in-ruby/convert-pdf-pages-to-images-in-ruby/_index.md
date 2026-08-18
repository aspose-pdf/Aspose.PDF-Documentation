---
title: Преобразование PDF-страниц в изображения в Ruby
linktitle: Преобразование PDF-страниц в изображения в Ruby
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
description: Узнайте, как конвертировать PDF-страницы в изображения с помощью Ruby с Aspose.PDF, что упрощает извлечение визуального контента из PDF-файлов.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF-страниц в изображения

Чтобы преобразовать все страницы в изображения PDF-документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **ConvertPagesToImages**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Конвертируйте PDF-страницы в изображения (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
