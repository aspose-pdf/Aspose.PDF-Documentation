---
title: "Mengatur kedaluwarsa PDF di Ruby"
linktitle: "Mengatur kedaluwarsa PDF di Ruby"
type: docs
weight: 110
url: /id/java/set-pdf-expiration-in-ruby/
description: Terapkan tanggal kedaluwarsa pada PDF menggunakan Aspose.PDF untuk Ruby untuk dokumen yang sensitif waktu.
lastmod: "2026-09-30"
---
## Aspose.PDF - atur kedaluwarsa PDF

Untuk mengatur kedaluwarsa dari  dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **SetExpiration**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## Mengunduh kode yang dapat dijalankan

Unduh **Set PDF Expiration (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
