---
title: Удалить метаданные из PDF в Ruby
linktitle: Удалить метаданные из PDF в Ruby
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: Удалите конфиденциальные или нежелательные метаданные из PDF-файлов программно с помощью Aspose.PDF для Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF — удаление метаданных

Чтобы удалить метаданные из документа PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **RemoveMetadata**.

Рубиновый код

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## Загрузите рабочий код

Загрузите **Удалить метаданные (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
