---
title: Dapatkan Metadata XMP dari File PDF di Ruby
type: docs
weight: 60
url: /id/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Metadata XMP

Untuk mendapatkan Metadata XMP dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **GetXMPMetadata**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Dapatkan properti

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## Unduh Kode Berjalan

Unduh **Get XMP Metadata (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)