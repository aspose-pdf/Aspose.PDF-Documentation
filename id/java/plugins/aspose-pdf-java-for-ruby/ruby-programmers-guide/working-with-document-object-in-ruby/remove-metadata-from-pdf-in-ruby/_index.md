---
title: "Menghapus metadata dari PDF di Ruby"
linktitle: "Menghapus metadata dari PDF di Ruby"
type: docs
weight: 90
url: /id/java/remove-metadata-from-pdf-in-ruby/
description: Hapus metadata sensitif atau tidak diinginkan dari file PDF secara programatis dengan Aspose.PDF for Ruby.
lastmod: "2026-09-30"
---
## Aspose.PDF - hapus metadata

Untuk menghapus Metadata dari dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **RemoveMetadata**.

Kode Ruby

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

## Mengunduh kode yang dapat dijalankan

Unduh **Remove Metadata (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
