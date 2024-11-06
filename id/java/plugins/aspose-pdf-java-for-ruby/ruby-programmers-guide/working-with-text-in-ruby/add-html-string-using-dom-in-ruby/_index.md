---
title: Tambahkan String HTML menggunakan DOM di Ruby
type: docs
weight: 10
url: id/java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tambahkan HTML

Untuk menambahkan string HTML dalam dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **AddHtml**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instansiasi objek Document

doc = Rjb::import('com.aspose.pdf.Document').new

# Tambahkan halaman ke koleksi halaman file PDF

page = doc.getPages().add()

# Instansiasi HtmlFragment dengan konten HTML

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo untuk detail margin

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set informasi margin

title.setMargin(margin)

# Tambahkan Fragmen HTML ke koleksi paragraf halaman

page.getParagraphs().add(title)

# Simpan file PDF

doc.save(data_dir + "html.output.pdf")

puts "HTML ditambahkan dengan sukses"
```


## Download Running Code

Unduh **Add HTML (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)