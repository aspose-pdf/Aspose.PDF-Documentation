---
title: Конвертировать PDF в формат DOC или DOCX в Ruby
linktitle: Конвертировать PDF в формат DOC или DOCX в Ruby
type: docs
weight: 30
url: /ru/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Узнайте, как конвертировать PDF‑документы в форматы DOC или DOCX в Ruby с помощью Aspose.PDF, обеспечивая более простое редактирование и обработку.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать PDF в DOC или DOCX

Чтобы конвертировать PDF‑документ в формат DOC или DOCX, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **PdfToDoc**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Скачайте исполняемый код

СкачатьВ **Преобразовать PDF в DOC или DOCX (Aspose.PDF)**В сВ любого из нижеупомянутых социальных сайтов кодинга:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)


