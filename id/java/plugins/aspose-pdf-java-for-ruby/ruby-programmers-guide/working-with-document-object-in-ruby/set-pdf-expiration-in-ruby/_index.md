---
title: Tetapkan Kedaluwarsa PDF di Ruby
type: docs
weight: 110
url: id/java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Tetapkan Kedaluwarsa PDF

Untuk menetapkan kedaluwarsa dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **SetExpiration**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('File ini telah kedaluwarsa. Anda memerlukan yang baru.');")

doc.setOpenAction(javascript)

# simpan dokumen yang diperbarui dengan informasi baru

doc.save(data_dir + "set_expiration.pdf")

puts "Perbarui informasi dokumen, silakan periksa file keluaran."
```


## Unduh Kode yang Berjalan

Unduh **Setel Kedaluwarsa PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)