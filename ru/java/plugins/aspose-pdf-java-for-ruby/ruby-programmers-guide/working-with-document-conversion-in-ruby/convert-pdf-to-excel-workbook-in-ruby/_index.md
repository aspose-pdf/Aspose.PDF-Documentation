---
title: Конвертировать PDF в книгу Excel на Ruby
linktitle: Конвертировать PDF в книгу Excel на Ruby
type: docs
weight: 40
url: /ru/java/convert-pdf-to-excel-workbook-in-ruby/
description: Поймите, как преобразовать данные PDF в книги Excel с использованием Ruby и Aspose.PDF, упрощая извлечение и анализ данных.
lastmod: "2026-08-19"
---
## Aspose.PDF - Преобразовать PDF в книгу Excel

Чтобы преобразовать документ PDF в книгу Excel с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToExcel**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instantiate ExcelSave Option object

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Save the output to XLS format

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Document has been converted successfully"
```

## Скачать исполняемый код

СкачатьВ **Convert PDF to DOC or DOCX (Aspose.PDF)**В изВ любого из нижеупомянутых сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)

