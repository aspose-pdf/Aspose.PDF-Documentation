---
title: Получение количества страниц PDF в Ruby
linktitle: Получение количества страниц PDF в Ruby
type: docs
weight: 40
url: /ru/java/get-page-count-of-pdf-in-ruby/
description: Программно получить общее число страниц в PDF‑документе с помощью Ruby и Aspose.PDF.
lastmod: "2026-09-17"
---
## Aspose.PDF — Получение количества страниц

Чтобы получить количество страниц PDF‑документа, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetNumberOfPages**.

Код Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## Загрузка работающего кода

Скачайте **Получить количество страниц (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)


