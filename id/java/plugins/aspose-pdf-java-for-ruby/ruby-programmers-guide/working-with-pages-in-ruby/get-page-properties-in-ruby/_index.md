---
title: Dapatkan Properti Halaman dalam Ruby
type: docs
weight: 50
url: /id/java/get-page-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Properti Halaman

Untuk mendapatkan properti halaman dari dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **GetPageProperties**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buat dokumen PDF

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# dapatkan koleksi halaman

page_collection = pdf_document.getPages()

# dapatkan halaman tertentu

pdf_page = page_collection.get_Item(1)

#dapatkan properti halaman

puts "ArtBox : Tinggi = " + pdf_page.getArtBox().getHeight().to_s + ", Lebar = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Tinggi = " + pdf_page.getBleedBox().getHeight().to_s + ", Lebar = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Tinggi = " + pdf_page.getCropBox().getHeight().to_s + ", Lebar = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Tinggi = " + pdf_page.getMediaBox().getHeight().to_s + ", Lebar = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Tinggi = " + pdf_page.getTrimBox().getHeight().to_s + ", Lebar = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Tinggi = " + pdf_page.getRect().getHeight().to_s + ", Lebar = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Nomor Halaman :- " + pdf_page.getNumber().to_s

puts "Rotasi :-" + pdf_page.getRotate().to_s
```


## Unduh Kode Berjalan

Unduh **Dapatkan Properti Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)