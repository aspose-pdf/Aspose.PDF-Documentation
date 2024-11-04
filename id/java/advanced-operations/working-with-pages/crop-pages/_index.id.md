---
title: Pangkas Halaman PDF secara programatik
linktitle: Pangkas Halaman
type: docs
weight: 80
url: /java/crop-pages/
description: Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF untuk Java memungkinkan Anda mengakses properti ini.

- **Kotak media**: Kotak media adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih saat dokumen dicetak ke PostScript atau PDF. Dengan kata lain, kotak media menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Kotak bleed**: Jika dokumen memiliki bleed, PDF juga akan memiliki kotak bleed.
 Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("dipangkas"), tinta akan mencapai tepi halaman. Bahkan jika halaman dipotong tidak tepat - dipotong sedikit di luar tanda pangkas - tidak akan ada tepi putih yang muncul di halaman.

- **Trim box**: Kotak trim menunjukkan ukuran akhir dokumen setelah dicetak dan dipangkas.
- **Art box**: Kotak seni adalah kotak yang digambar di sekitar konten sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Kotak potong adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari kotak potong yang ditampilkan di Adobe Acrobat. Untuk deskripsi mendetail tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Batas Halaman.
- **Page.Rect**: perpotongan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti-properti ini.  
Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Cuplikan di bawah ini menunjukkan cara memotong halaman:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // Buat Kotak Baru Rectagle
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Awalnya halaman kami terlihat seperti yang ditunjukkan pada Gambar 1.
![Figure 1. Cropped Page](crop_page.png)

Setelah perubahan, halaman akan terlihat seperti Gambar 2.
![Figure 2. Cropped Page](crop_page2.png)