---
title: Объединение PDF-файлов в Ruby
linktitle: Объединение PDF-файлов в Ruby
type: docs
weight: 10
url: /ru/java/concatenate-pdf-files-in-ruby/
description: Эффективно объединяйте несколько PDF в один документ с помощью Ruby и Aspose.PDF.
lastmod: "2026-09-17"
---
## Aspose.PDF - Объединение PDF-файлов

Чтобы объединить PDF-файлы, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **ConcatenatePdfFiles**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## Загрузка работающего кода

Скачайте **Concatenate PDF Files (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)


