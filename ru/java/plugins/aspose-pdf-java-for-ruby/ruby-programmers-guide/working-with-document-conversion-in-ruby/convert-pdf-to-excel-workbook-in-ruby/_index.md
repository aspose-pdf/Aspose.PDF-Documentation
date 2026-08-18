---
title: Конвертировать PDF в книгу Excel в Ruby
linktitle: Конвертировать PDF в книгу Excel в Ruby
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
description: Узнайте, как конвертировать данные PDF в книги Excel с помощью Ruby с Aspose.PDF, что упрощает извлечение и анализ данных.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF в книгу Excel

Чтобы преобразовать PDF-документ в книгу Excel с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToExcel**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Конвертируйте PDF в DOC или DOCX (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
