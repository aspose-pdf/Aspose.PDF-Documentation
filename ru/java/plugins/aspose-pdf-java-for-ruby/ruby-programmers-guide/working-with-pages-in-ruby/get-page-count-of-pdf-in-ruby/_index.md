---
title: Получить количество страниц PDF в Ruby
type: docs
weight: 40
url: /ru/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить количество страниц

Чтобы получить количество страниц PDF-документа с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetNumberOfPages**.

Код на Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Создать PDF-документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Количество страниц:" + page_count.to_s
```

## Скачать работающий код

Скачайте **Get Page Count (Aspose.PDF)** с любого из нижеупомянутых социальных кодинг-сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)