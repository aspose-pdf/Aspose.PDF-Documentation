---
title: Tambahkan Nomor Halaman ke PDF
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: id/java/add-page-number/
description: Aspose.PDF untuk Java memungkinkan Anda menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen.
**Aspose.PDF untuk Java** memungkinkan Anda menambahkan nomor halaman dengan PageNumberStamp.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) untuk menambahkan stempel nomor halaman dalam dokumen PDF.
 The [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class menyediakan metode untuk membuat stempel berbasis nomor halaman seperti format, margin, penyelarasan, nomor awal, dll. Untuk menambahkan stempel nomor halaman, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) dengan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan stempel ke file PDF. Anda juga dapat mengatur atribut font dari stempel nomor halaman.

Cuplikan kode berikut menunjukkan cara menambahkan nomor halaman dalam file PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Buat stempel nomor halaman
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Apakah stempel adalah latar belakang
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Halaman # dari " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Atur properti teks
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