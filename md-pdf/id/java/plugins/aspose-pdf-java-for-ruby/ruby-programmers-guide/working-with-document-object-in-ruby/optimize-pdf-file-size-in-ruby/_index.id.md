---
title: Optimalkan Ukuran File PDF di Ruby
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimalkan Ukuran File PDF

Untuk mengoptimalkan ukuran file dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, panggil metode **optimize_filesize** dari modul **Optimize**.

Kode Ruby

```java

 def optimize_filesize()

    # Jalur ke direktori dokumen.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Buka dokumen pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimalkan ukuran file dengan menghapus objek yang tidak digunakan

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # Simpan dokumen keluaran

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "Ukuran File PDF Dioptimalkan, silakan periksa file keluaran."

end 
```


## Unduh Kode Berjalan

Download **Optimize PDF File Size (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)