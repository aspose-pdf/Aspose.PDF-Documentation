---
title: Установить информацию о PDF-файле в Ruby
linktitle: Установить информацию о PDF-файле в Ruby
type: docs
weight: 120
url: /ru/java/set-pdf-file-information-in-ruby/
description: Программно определять и обновлять метаданные PDF, такие как заголовок, автор и ключевые слова, с помощью Ruby.
lastmod: "2026-08-19"
---
## Aspose.PDF - Установить информацию о PDF-файле

Чтобы обновить информацию о документе PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **SetPdfFileInfo**.

Код Ruby

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

## Скачайте исполняющий код

СкачатьВ **Set PDF File Information (Aspose.PDF)**В fromВ любой из перечисленных ниже сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)


