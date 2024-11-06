---
title: Вставка пустой страницы в конец PDF файла на Ruby
type: docs
weight: 60
url: ru/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Вставка пустой страницы в конец PDF файла

Чтобы вставить пустую страницу в конец PDF документа с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **InsertEmptyPageAtEndOfFile**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# вставить пустую страницу в PDF

pdf.getPages().add()

# Сохранить объединенный выходной файл (целевой документ)

pdf.save(data_dir+ "output.pdf")

puts "Пустая страница добавлена успешно!"
```

## Скачать работающий код

Скачайте **Вставка пустой страницы в конец PDF файла (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)