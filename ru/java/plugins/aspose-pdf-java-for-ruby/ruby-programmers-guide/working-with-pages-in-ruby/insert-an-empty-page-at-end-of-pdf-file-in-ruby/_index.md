---
title: Вставьте пустую страницу в конец PDF-файла в Ruby
linktitle: Вставьте пустую страницу в конец PDF-файла в Ruby
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Узнайте, как вставить пустую страницу в конец документа PDF с помощью Ruby с Aspose.PDF, что повышает гибкость ваших задач по обработке PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — вставка пустой страницы в конец PDF-файла

Чтобы вставить пустую страницу в конец PDF-документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **InsertEmptyPageAtEndOfFile**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Загрузите рабочий код

Загрузите **Вставьте пустую страницу в конец PDF-файла (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
