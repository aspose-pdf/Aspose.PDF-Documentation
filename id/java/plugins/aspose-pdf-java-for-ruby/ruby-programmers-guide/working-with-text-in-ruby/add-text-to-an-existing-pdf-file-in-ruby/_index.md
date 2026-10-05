---
title: "Menambahkan teks ke file PDF yang ada di Ruby"
linktitle: "Menambahkan teks ke file PDF yang ada di Ruby"
type: docs
weight: 20
url: /id/java/add-text-to-an-existing-pdf-file-in-ruby/
description: Pelajari cara menambahkan teks ke dokumen PDF yang ada di Ruby dengan Aspose.PDF untuk meningkatkan atau memperbarui konten PDF Anda.
lastmod: "2026-09-30"
---
## Aspose.PDF - tambah teks

Untuk menambahkan string Teks dalam dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **AddText**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get particular page

pdf_page = doc.getPages().get_Item(1)

# create text fragment

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# set text properties

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# create TextBuilder object

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# append the text fragment to the PDF page

text_builder.appendText(text_fragment)

# Save PDF file

doc.save(data_dir + "Text_Added.pdf")

puts "Text added successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Tambahkan Teks (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)
