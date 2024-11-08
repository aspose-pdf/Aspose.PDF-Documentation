---
title: Optimalkan Dokumen PDF untuk Web di Ruby
type: docs
weight: 70
url: /id/java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimalkan PDF untuk Web

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil metode **optimize_web** dari modul **Optimize**.

Kode Ruby

```java

 def optimize_web()

    # Jalur ke direktori dokumen.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Buka dokumen pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimalkan untuk web

    doc.optimize()

    #Simpan dokumen keluaran

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "PDF dioptimalkan untuk Web, silakan periksa file keluaran."

end
``` 

## Unduh Kode Berjalan

Unduh **Optimalkan PDF untuk Web (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)