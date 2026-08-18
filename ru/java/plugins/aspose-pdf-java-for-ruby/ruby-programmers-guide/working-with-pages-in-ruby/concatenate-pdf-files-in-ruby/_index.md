---
title: Объединение PDF-файлов в Ruby
linktitle: Объединение PDF-файлов в Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: Эффективно объединяйте несколько PDF-файлов в один документ, используя Ruby и Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — объединение PDF-файлов

Чтобы объединить PDF-файлы с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **ConcatenatePdfFiles**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Объединить PDF-файлы (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
