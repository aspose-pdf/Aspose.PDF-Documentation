---
title: Dapatkan Metadata XMP dari File PDF di Ruby
linktitle: Dapatkan Metadata XMP dari File PDF di Ruby
type: docs
weight: 60
url: /id/java/get-xmp-metadata-from-pdf-file-in-ruby/
description: Mengakses dan memanipulasi metadata XMP dalam dokumen PDF menggunakan Ruby dengan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Metadata XMP

Untuk mendapatkan Metadata XMP dari Pdf document menggunakan **Aspose.PDF Java for Ruby**, cukup panggil **GetXMPMetadata** module.

Kode Ruby

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

## Unduh Kode yang Berjalan

Unduh **Get XMP Metadata (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
