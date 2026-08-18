---
title: Вставьте пустую страницу в PDF-файл в Ruby
linktitle: Вставьте пустую страницу в PDF-файл в Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Узнайте, как вставить пустую страницу в определенное место PDF-документа с помощью Ruby и Aspose.PDF для точного управления документами.
lastmod: "2026-06-09"
---
## Aspose.PDF – Вставка пустой страницы

Чтобы вставить пустую страницу в документ PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **InsertEmptyPage**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Загрузите рабочий код

Загрузите **Вставьте пустую страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
