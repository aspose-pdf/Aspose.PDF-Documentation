---
title: Удалить определенную страницу из PDF-файла в Ruby
linktitle: Удалить определенную страницу из PDF-файла в Ruby
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Удалите определенные страницы из PDF-файлов программно с помощью Aspose.PDF для Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - Удалить страницу

Чтобы удалить определенную страницу из документа PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **DeletePage**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Удалить страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
