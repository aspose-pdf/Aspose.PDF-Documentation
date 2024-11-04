---
title: Вставить пустую страницу в PDF файл на Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Вставка пустой страницы

Чтобы вставить пустую страницу в PDF документ, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **InsertEmptyPage**.

Код на Ruby

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# вставить пустую страницу в PDF

pdf.getPages().insert(1)

# Сохранить объединенный выходной файл (целевой документ)

pdf.save(data_dir+ "output.pdf")

puts "Пустая страница успешно добавлена!"
```

## Скачать работающий код

Скачайте **Вставка пустой страницы (Aspose.PDF)** с любого из нижеупомянутых сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)