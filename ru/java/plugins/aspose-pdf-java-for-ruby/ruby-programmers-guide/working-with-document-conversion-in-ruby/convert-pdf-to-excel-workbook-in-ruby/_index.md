---
title: Преобразование PDF в Excel книгу в Ruby
type: docs
weight: 40
url: ru/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование PDF в Excel книгу

Чтобы преобразовать PDF документ в Excel книгу, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToExcel**.

Ruby Код

```java

# Путь к каталогу документов.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть целевой документ

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Создать объект ExcelSave Option

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Сохранить вывод в формате XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Документ был успешно преобразован"
```

## Скачать запускаемый код

Скачайте **Преобразование PDF в DOC или DOCX (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)