---
title: Ubah Ukuran Halaman PDF Secara Programatis
linktitle: Ubah Ukuran Halaman
type: docs
weight: 50
url: /java/change-page-size/
description: Ubah Ukuran Halaman dari file PDF Anda menggunakan pustaka Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ubah Ukuran Halaman PDF

Aspose.PDF untuk Java memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana dalam aplikasi Java Anda. Topik ini menjelaskan cara memperbarui/mengubah dimensi halaman (ukuran) dari file PDF yang ada.

Kelas [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) berisi metode SetPageSize(...) yang memungkinkan Anda mengatur ukuran halaman. Cuplikan kode di bawah ini memperbarui dimensi halaman dalam beberapa langkah mudah:

1. Muat file PDF sumber.
1. Dapatkan halaman ke dalam objek [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Dapatkan halaman tertentu.
1. Panggil metode SetPageSize(..) untuk memperbarui dimensinya.

1. Panggil metode Save(..) dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) untuk menghasilkan file PDF dengan dimensi halaman yang diperbarui.

{{% alert color="primary" %}}

Harap diperhatikan bahwa properti tinggi dan lebar menggunakan poin sebagai unit dasar, di mana 1 inci = 72 poin dan 1 cm = 1/2.54 inci = 0.3937 inci = 28.3 poin.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara mengubah dimensi halaman PDF ke ukuran A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Buka dokumen pertama
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Dapatkan koleksi halaman
        PageCollection pageCollection = pdfDocument.getPages();

        // Dapatkan halaman tertentu
        Page pdfPage = pageCollection.get_Item(1);

        // Set ukuran halaman sebagai A4 (11.7 x 8.3 in) dan di Aspose.Pdf, 1 inci = 72 poin
        // Jadi dimensi A4 dalam poin akan menjadi (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```


## Dapatkan Ukuran Halaman PDF

Anda dapat membaca ukuran halaman PDF dari file PDF yang ada menggunakan Aspose.PDF untuk Java. Contoh kode berikut menunjukkan cara membaca dimensi halaman PDF menggunakan Java.

```java
    public static void GetPDFPageSize() {
        
        // Buka dokumen pertama
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Menambahkan halaman kosong ke dokumen pdf
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Dapatkan informasi tinggi dan lebar halaman
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Putar halaman pada sudut 90 derajat
        page.setRotate (Rotation.on90);

        // Dapatkan informasi tinggi dan lebar halaman
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Simpan dokumen yang diperbarui
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```