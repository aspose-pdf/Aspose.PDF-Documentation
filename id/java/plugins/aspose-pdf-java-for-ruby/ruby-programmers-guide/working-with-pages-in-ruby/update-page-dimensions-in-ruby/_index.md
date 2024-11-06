---
title: Memperbarui Dimensi Halaman dalam Ruby
type: docs
weight: 90
url: id/java/update-page-dimensions-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Memperbarui Dimensi Halaman

Untuk memperbarui Dimensi halaman menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **UpdatePageDimensions**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# dapatkan koleksi halaman

page_collection = pdf.getPages()

# dapatkan halaman tertentu

pdf_page = page_collection.get_Item(1)

# atur ukuran halaman sebagai A4 (11,7 x 8,3 in) dan dalam Aspose.PDF, 1 inci = 72 poin

# sehingga dimensi A4 dalam poin akan menjadi (842,4, 597,6)

pdf_page.setPageSize(597.6,842.4)

# simpan file PDF yang baru dihasilkan

pdf.save(data_dir + "output.pdf")

puts "Dimensi diperbarui dengan sukses!"
```

## Unduh Kode Berjalan

Unduh **Update Page Dimensions (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)