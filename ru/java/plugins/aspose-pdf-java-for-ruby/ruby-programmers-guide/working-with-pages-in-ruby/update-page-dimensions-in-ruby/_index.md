---
title: Обновление размеров страницы в Ruby
linktitle: Обновление размеров страницы в Ruby
type: docs
weight: 90
url: /ru/java/update-page-dimensions-in-ruby/
description: Узнайте, как обновить размеры страниц PDF‑документа с помощью Ruby и Aspose.PDF для точного форматирования страниц.
lastmod: "2026-08-19"
---
## Aspose.PDF - Обновление размеров страницы

Чтобы обновить размеры страниц, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **UpdatePageDimensions**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## Скачайте работающий код

Скачать\u0412\u00A0**Update Page Dimensions (Aspose.PDF)**\u0412\u00A0из\u0412\u00A0любого из нижеупомянутых социальных кодирующих сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)


