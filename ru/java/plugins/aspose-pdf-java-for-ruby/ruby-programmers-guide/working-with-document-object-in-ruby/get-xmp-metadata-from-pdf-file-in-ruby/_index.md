---
title: Получить XMP Метаданные из PDF Файла в Ruby
type: docs
weight: 60
url: ru/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Получить XMP Метаданные

Чтобы получить XMP метаданные из PDF документа, используя **Aspose.PDF Java для Ruby**, просто вызовите модуль **GetXMPMetadata**.

Ruby Код

```java
# Путь к каталогу с документами.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Открыть pdf документ.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Получить свойства

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Скачать Запущенный Код

Скачайте **Get XMP Metadata (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов по программированию:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)