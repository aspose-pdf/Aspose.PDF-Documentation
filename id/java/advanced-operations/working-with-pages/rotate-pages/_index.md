---
title: Putar Halaman PDF secara programatis
linktitle: Putar Halaman PDF
type: docs
weight: 60
url: id/java/rotate-pages/
description: Ubah orientasi halaman dan sesuaikan konten halaman dengan orientasi halaman baru menggunakan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ubah Orientasi Halaman

Artikel ini menjelaskan bagaimana cara memperbarui atau mengubah orientasi halaman dari halaman-halaman dalam file PDF yang sudah ada.

Aspose.PDF untuk Java memiliki fitur untuk mengubah orientasi halaman dari landscape ke portrait dan sebaliknya. Untuk mengubah orientasi halaman, atur [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) halaman menggunakan potongan kode berikut.

Anda juga dapat mengubah orientasi halaman dengan mengatur sudut rotasi menggunakan metode Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // Kita harus memindahkan halaman ke atas untuk mengkompensasi perubahan ukuran halaman
            // // (tepi bawah halaman adalah 0,0 dan informasi biasanya ditempatkan dari
            // //  bagian atas halaman. Itulah mengapa kita memindahkan tepi bawah ke atas pada perbedaan antara
            // //  tinggi lama dan baru.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // Kadang kita juga perlu mengatur CropBox (jika diatur di file asli)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // Mengatur sudut rotasi halaman
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // Simpan file keluaran
        pdfDocument.save(_dataDir);
    }    
}
```