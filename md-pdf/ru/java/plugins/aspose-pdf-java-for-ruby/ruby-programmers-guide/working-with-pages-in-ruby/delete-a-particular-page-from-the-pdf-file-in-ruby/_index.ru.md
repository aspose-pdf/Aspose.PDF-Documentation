---
title: Удаление Определенной Страницы из PDF Файла в Ruby
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Удаление Страницы

Чтобы удалить определенную страницу из PDF документа, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **DeletePage**.

Код на Ruby

```java
# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# удалить определенную страницу

pdf.getPages().delete(2)

# сохранить вновь созданный PDF файл

pdf.save(data_dir + "output.pdf")

puts "Страница успешно удалена!"
```

## Скачать Исполняемый Код

Скачайте **Delete Page (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)