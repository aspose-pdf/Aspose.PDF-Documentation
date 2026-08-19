---
title: Разделить PDF-файл на отдельные страницы в Ruby
linktitle: Разделить PDF-файл на отдельные страницы в Ruby
type: docs
weight: 80
url: /ru/java/split-pdf-file-into-individual-pages-in-ruby/
description: Узнайте, как разделить PDF-файл на отдельные страницы с помощью Ruby и Aspose.PDF, что упрощает управление и извлечение содержимого.
lastmod: "2026-08-19"
---
## Aspose.PDF - Разделить страницы

Чтобы разделить PDF‑документ на отдельные страницы, используя **Aspose.PDF Java for Ruby**, достаточно вызвать модуль **SplitAllPages**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## Скачать исполняющий код

Скачать **Split Pages (Aspose.PDF)**В изВ любого из указанных ниже сайтов совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)

