---
title: Получить определённую страницу в PDF‑файле на Ruby
linktitle: Получить определённую страницу в PDF‑файле на Ruby
type: docs
weight: 30
url: /ru/java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Получайте доступ и управляйте отдельными страницами PDF‑документов с помощью Ruby и Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF - Получить страницу

Чтобы получить определённую страницу в PDF‑документе с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetPage**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## Скачать исполняемый код

Скачать **Get Page (Aspose.PDF)** из любого из перечисленных ниже сайтов для совместного кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)


