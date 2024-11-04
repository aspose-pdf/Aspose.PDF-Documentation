---
title: Mengatur Informasi File PDF di Ruby
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Mengatur Informasi File PDF

Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **SetPdfFileInfo**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Dapatkan informasi dokumen

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF untuk java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("Informasi PDF")

doc_info.setTitle("Mengatur Informasi Dokumen PDF")

# simpan dokumen yang diperbarui dengan informasi baru

doc.save(data_dir + "Updated_Information.pdf")

puts "Perbarui informasi dokumen, silakan periksa file keluaran."
```


## Download Running Code

Unduh **Set PDF File Information (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)