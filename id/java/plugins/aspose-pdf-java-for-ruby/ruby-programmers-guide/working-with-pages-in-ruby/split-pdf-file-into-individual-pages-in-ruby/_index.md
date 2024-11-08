---
title: Memisahkan File PDF Menjadi Halaman Individual dalam Ruby
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Memisahkan Halaman

Untuk memisahkan dokumen PDF menjadi halaman individual menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **SplitAllPages**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop melalui semua halaman

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# buat objek Document baru

new_document = Rjb::import('com.aspose.pdf.Document').new

# dapatkan halaman pada indeks tertentu dari Koleksi Halaman

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# simpan file PDF yang baru dihasilkan

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Proses pemisahan selesai dengan sukses!"
```


## Download Running Code

Unduh **Split Pages (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)