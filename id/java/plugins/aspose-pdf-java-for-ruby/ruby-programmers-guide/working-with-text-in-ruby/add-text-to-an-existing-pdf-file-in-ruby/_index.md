---
title: Tambahkan Teks ke file PDF yang sudah ada di Ruby
type: docs
weight: 20
url: id/java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan Teks

Untuk menambahkan string Teks dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **AddText**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instansiasi objek Dokumen

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# dapatkan halaman tertentu

pdf_page = doc.getPages().get_Item(1)

# buat fragmen teks

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("teks utama")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# atur properti teks

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# buat objek TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# tambahkan fragmen teks ke halaman PDF

text_builder.appendText(text_fragment)

# Simpan file PDF

doc.save(data_dir + "Text_Added.pdf")

puts "Teks berhasil ditambahkan"
```


## Unduh Kode yang Berjalan

Unduh **Tambahkan Teks (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)