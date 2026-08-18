---
title: Получить количество страниц PDF в Ruby
linktitle: Получить количество страниц PDF в Ruby
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: Получите общее количество страниц в PDF-документе программно, используя Ruby с Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение количества страниц

Чтобы получить количество страниц PDF-документа с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetNumberOfPages**.

Рубиновый код

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Загрузите рабочий код

Загрузите **Получить количество страниц (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
