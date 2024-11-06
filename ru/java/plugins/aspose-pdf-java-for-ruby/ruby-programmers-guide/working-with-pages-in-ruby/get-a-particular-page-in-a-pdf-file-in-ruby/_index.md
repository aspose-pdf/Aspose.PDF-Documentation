---
title: Получение Определенной Страницы в PDF Файле на Ruby
type: docs
weight: 30
url: ru/java/get-a-particular-page-in-a-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получение Страницы

Чтобы получить определенную страницу в PDF документе, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetPage**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# получить страницу по определенному индексу в коллекции страниц

pdf_page = pdf.getPages().get_Item(1)

# создать новый объект Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# добавить страницу в коллекцию страниц нового объекта документа

new_document.getPages().add(pdf_page)

# сохранить вновь созданный PDF файл

new_document.save(data_dir + "output.pdf")

puts "Процесс успешно завершен!"
```

## Загрузка Исполняемого Кода

Скачайте **Получение Страницы (Aspose.PDF)** с любого из нижеуказанных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)