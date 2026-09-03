---
title: Получить XMP Metadata из PDF‑файла в Ruby
linktitle: Получить XMP Metadata из PDF‑файла в Ruby
type: docs
weight: 60
url: /ru/java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Доступ и манипулирование XMP metadata в PDF‑документах с использованием Ruby и Aspose.PDF.
lastmod: "2026-08-19"
---
## Aspose.PDF – Получить XMP Metadata

Чтобы получить XMP Metadata из PDF‑документа с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetXMPMetadata**.

Код Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Скачайте запущенный код

Скачать **Получить XMP Metadata (Aspose.PDF)** из любого из перечисленных ниже социальных площадок для разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)


