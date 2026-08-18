---
title: Установка информации о PDF-файле в Ruby
linktitle: Установка информации о PDF-файле в Ruby
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: Программно определяйте и обновляйте метаданные PDF, такие как заголовок, автор и ключевые слова, с помощью Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF — установка информации о PDF-файле

Чтобы обновить информацию о PDF-документе с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **SetPdfFileInfo**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## Загрузите рабочий код

Загрузите **Установите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
