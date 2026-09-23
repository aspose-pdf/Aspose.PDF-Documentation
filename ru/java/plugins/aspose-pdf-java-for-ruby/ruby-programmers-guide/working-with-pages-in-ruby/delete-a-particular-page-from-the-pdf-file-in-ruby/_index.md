---
title: Удаление конкретной страницы из PDF‑файла в Ruby
linktitle: Удаление конкретной страницы из PDF‑файла в Ruby
type: docs
weight: 20
url: /ru/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Программно удалять определённые страницы из PDF‑файлов с помощью Aspose.PDF for Ruby.
lastmod: "2026-09-17"
---
## Aspose.PDF - Удаление страницы

Чтобы удалить конкретную страницу из PDF‑документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **DeletePage**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## Загрузка исполняемого кода

Скачайте **Delete Page (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)


