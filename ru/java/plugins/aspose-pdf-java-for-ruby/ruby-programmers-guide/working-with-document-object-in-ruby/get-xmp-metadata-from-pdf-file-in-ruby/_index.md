---
title: Получить метаданные XMP из PDF-файла в Ruby
linktitle: Получить метаданные XMP из PDF-файла в Ruby
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Доступ к метаданным XMP в PDF-документах и ​​манипулирование ими с помощью Ruby с Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF — получение метаданных XMP

Чтобы получить метаданные XMP из документа PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **GetXMPMetadata**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Получите метаданные XMP (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
