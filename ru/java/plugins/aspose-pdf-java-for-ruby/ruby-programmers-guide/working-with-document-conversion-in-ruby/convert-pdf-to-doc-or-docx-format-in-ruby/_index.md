---
title: Конвертируйте PDF в формат DOC или DOCX в Ruby.
linktitle: Конвертируйте PDF в формат DOC или DOCX в Ruby.
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Узнайте, как конвертировать PDF-документы в форматы DOC или DOCX в Ruby с помощью Aspose.PDF, что упрощает редактирование и обработку.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF в DOC или DOCX

Чтобы преобразовать PDF-документ в формат DOC или DOCX с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToDoc**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Загрузите рабочий код

Загрузите **Конвертируйте PDF в DOC или DOCX (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
