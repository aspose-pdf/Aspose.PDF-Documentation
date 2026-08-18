---
title: Получить информацию о PDF-файле в Ruby
linktitle: Получить информацию о PDF-файле в Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: Извлекайте метаданные и детали из PDF-файлов программно с помощью Aspose.PDF в Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение информации о PDF-файле

Чтобы получить информацию о файле PDF-документа с помощью **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetPdfFileInfo**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## Загрузите рабочий код

Загрузите **Получите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
