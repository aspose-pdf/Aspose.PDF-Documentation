---
title: Ekstrak Teks Dari Semua Halaman Dokumen PDF di Ruby
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ekstrak Teks Dari Semua Halaman

Untuk mengekstrak teks dari semua halaman dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **ExtractTextFromAllPages**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# buat objek TextAbsorber untuk mengekstrak teks

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# terima absorber untuk semua halaman

pdf.getPages().accept(text_absorber)

# Untuk mengekstrak teks dari halaman tertentu dokumen, kita perlu menentukan halaman tertentu menggunakan indeksnya terhadap metode accept(..).

# terima absorber untuk halaman PDF tertentu

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#dapatkan teks yang diekstraksi

extracted_text = text_absorber.getText()

# buat penulis dan buka file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# tulis satu baris teks ke file

# tw.WriteLine(extractedText);

# tutup stream

writer.close()

puts "Teks berhasil diekstraksi. Periksa file keluaran."
```


## Download Running Code

Unduh **Extract Text From All the Pages (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)