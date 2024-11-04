---
title: Dapatkan Informasi File PDF di Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Informasi File PDF

Untuk Mendapatkan Informasi File dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **GetPdfFileInfo**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Dapatkan informasi dokumen

doc_info = doc.getInfo()

# Tampilkan informasi dokumen

puts "Penulis:-" + doc_info.getAuthor().to_s

puts "Tanggal Pembuatan:-" + doc_info.getCreationDate().to_string

puts "Kata Kunci:-" + doc_info.getKeywords().to_s

puts "Tanggal Modifikasi:-" + doc_info.getModDate().to_string

puts "Subjek:-" + doc_info.getSubject().to_s

puts "Judul:-" + doc_info.getTitle().to_s
```

## Unduh Kode Berjalan

Unduh **Dapatkan Informasi File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)

```ruby
# Muat pustaka yang diperlukan
require 'java'
require_relative '../lib/asposepdfjava'

include Asposepdfjava

module GetPdfFileInfo
  def self.run()
    # Dapatkan informasi file PDF
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    pdf_file = data_dir + 'input.pdf'

    # Buka dokumen PDF yang ada
    pdf_document = Document.new(pdf_file)

    # Dapatkan informasi dari dokumen PDF
    puts "Jumlah Halaman: " + pdf_document.pages.size.to_s
    puts "Judul: " + pdf_document.info.title.to_s
    puts "Pengarang: " + pdf_document.info.author.to_s
    puts "Subjek: " + pdf_document.info.subject.to_s
    puts "Kata Kunci: " + pdf_document.info.keywords.to_s
  end
end