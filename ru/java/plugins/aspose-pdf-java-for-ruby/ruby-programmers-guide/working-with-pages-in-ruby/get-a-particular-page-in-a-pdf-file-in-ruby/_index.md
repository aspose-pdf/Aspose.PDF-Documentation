---
title: Получить определенную страницу в PDF-файле в Ruby
linktitle: Получить определенную страницу в PDF-файле в Ruby
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Доступ к отдельным страницам PDF-документов и управление ими с помощью Ruby и Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — Получить страницу

Чтобы получить конкретную страницу в PDF-документе с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetPage**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Get Page (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
