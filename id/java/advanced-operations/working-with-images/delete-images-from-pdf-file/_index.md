---
title: Hapus Gambar dari File PDF
linktitle: Hapus Gambar
type: docs
weight: 20
url: id/java/delete-images-from-pdf-file/
description: Bagian ini menjelaskan bagaimana menghapus gambar dari file PDF menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
---

Untuk menghapus gambar dari file PDF, cukup gunakan metode delete(..) dari koleksi Gambar.

1. Buat objek Dokumen dan buka file PDF input.
1. Dapatkan Halaman yang menyimpan gambar dari koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Gambar disimpan dalam koleksi Gambar, yang ditemukan dalam koleksi [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) halaman.
1. Hapus gambar dengan metode Delete dari koleksi Gambar.
1. Simpan output seperti menggunakan metode Save dari objek Dokumen.

Cuplikan kode berikut menunjukkan cara menghapus gambar dari file PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Buat nomor halaman stempel
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Apakah stempel adalah latar belakang
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Setel properti teks
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Tambahkan stempel ke halaman tertentu
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir);

    }
}
```