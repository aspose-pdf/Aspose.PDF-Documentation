---
title: Обновить размеры страницы в Ruby
linktitle: Обновить размеры страницы в Ruby
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
description: Узнайте, как обновить размеры страницы PDF-документа с помощью Ruby с Aspose.PDF для точного форматирования страницы.
lastmod: "2026-06-09"
---
## Aspose.PDF — обновление размеров страницы

Чтобы обновить размеры страницы с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **UpdatePageDimensions**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Обновить размеры страницы (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
