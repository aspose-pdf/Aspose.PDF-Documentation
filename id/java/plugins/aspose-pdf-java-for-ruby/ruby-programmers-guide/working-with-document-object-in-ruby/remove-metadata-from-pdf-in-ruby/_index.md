---
title: Hapus Metadata dari PDF dalam Ruby
type: docs
weight: 90
url: id/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Hapus Metadata

Untuk menghapus Metadata dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **RemoveMetadata**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# simpan dokumen pembaruan dengan informasi baru

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Metadata berhasil dihapus, silakan periksa file keluaran."
```

## Unduh Kode Berjalan

Unduh **Remove Metadata (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)