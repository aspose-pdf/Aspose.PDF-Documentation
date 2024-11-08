---
title: Обновление размеров страницы в Ruby
type: docs
weight: 90
url: /ru/java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Обновление размеров страницы

Чтобы обновить размеры страницы с использованием **Aspose.PDF Java для Ruby**, просто вызовите модуль **UpdatePageDimensions**.

Код на Ruby

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# получить коллекцию страниц

page_collection = pdf.getPages()

# получить определенную страницу

pdf_page = page_collection.get_Item(1)

# установить размер страницы как A4 (11.7 x 8.3 дюйма) и в Aspose.PDF, 1 дюйм = 72 пункта

# поэтому размеры A4 в пунктах будут (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# сохранить вновь созданный PDF файл

pdf.save(data_dir + "output.pdf")

puts "Размеры обновлены успешно!"
```

## Скачать исполняемый код

Скачать **Обновление размеров страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)