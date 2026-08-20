---
title: Удалить метаданные из PDF на Ruby
linktitle: Удалить метаданные из PDF на Ruby
type: docs
weight: 90
url: /ru/java/remove-metadata-from-pdf-in-ruby/
description: Программно удаляйте чувствительные или нежелательные метаданные из PDF‑файлов с помощью Aspose.PDF for Ruby.
lastmod: "2026-08-19"
---
## Aspose.PDF — удаление метаданных

Чтобы удалить метаданные из PDF‑документа, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **RemoveMetadata**.

Код Ruby

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

## Скачать работающий код

СкачатьВ **Remove Metadata (Aspose.PDF)**В изВ любого из указанных ниже социальных сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)


