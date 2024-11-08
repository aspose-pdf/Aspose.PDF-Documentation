---
title: Menambahkan JavaScript dalam Ruby
type: docs
weight: 10
url: /id/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Menambahkan JavaScript

Untuk menambahkan JavaScript dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **AddJavaScript**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Menambahkan JavaScript di Tingkat Dokumen

# Instansiasi JavascriptAction dengan pernyataan JavaScript yang diinginkan

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Menetapkan objek JavascriptAction ke aksi yang diinginkan dari Dokumen

doc.setOpenAction(javaScript)

# Menambahkan JavaScript di Tingkat Halaman

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Simpan Dokumen PDF

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Berhasil Menambahkan JavaScript, silakan periksa file keluaran."
```


## Download Running Code

Unduh **Menambahkan JavaScript (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)