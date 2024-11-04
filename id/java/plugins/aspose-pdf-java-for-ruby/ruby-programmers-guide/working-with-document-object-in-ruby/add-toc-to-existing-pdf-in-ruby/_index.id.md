---
title: Tambahkan Daftar Isi ke PDF yang Ada di Ruby
type: docs
weight: 30
url: /java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan Daftar Isi

<ins>Untuk menambahkan Daftar Isi dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **AddToc**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Dapatkan akses ke halaman pertama file PDF

toc_page = doc.getPages().insert(1)

# Buat objek untuk merepresentasikan informasi Daftar Isi

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Daftar Isi")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Tetapkan judul untuk Daftar Isi

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Buat objek string yang akan digunakan sebagai elemen Daftar Isi

titles = Array["Halaman pertama", "Halaman kedua"]

i = 0

while i < 2

    # Buat objek Heading

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Tentukan halaman tujuan untuk objek heading

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # Halaman tujuan

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # Koordinat tujuan

    segment2.setText(titles[i])

    # Tambahkan heading ke halaman yang berisi Daftar Isi

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# Simpan Dokumen PDF

doc.save(data_dir + "TOC.pdf")

puts "Berhasil menambahkan Daftar Isi, silakan periksa file keluaran."
```


## <ins> **Unduh Kode Berjalan

Unduh **Tambah TOC (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)