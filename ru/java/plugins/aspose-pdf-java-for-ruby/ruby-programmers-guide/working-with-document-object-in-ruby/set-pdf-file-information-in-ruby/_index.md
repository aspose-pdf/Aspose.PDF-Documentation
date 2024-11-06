---
title: Установить информацию о PDF файле на Ruby
type: docs
weight: 120
url: ru/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Установить информацию о PDF файле

Чтобы обновить информацию о PDF-документе с использованием **Aspose.PDF Java for Ruby**, просто вызовите модуль **SetPdfFileInfo**.

Код на Ruby

```java

# Путь к директории с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть PDF документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Получить информацию о документе

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF для java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("Информация о PDF")

doc_info.setTitle("Установка информации о PDF документе")

# сохранить обновленный документ с новой информацией

doc.save(data_dir + "Updated_Information.pdf")

puts "Информация о документе обновлена, пожалуйста, проверьте выходной файл."
```


## Скачать Исполняемый Код

Скачайте **Установить информацию о PDF-файле (Aspose.PDF)** с любого из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)