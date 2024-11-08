---
title: Tambahkan Header dan Footer PDF 
linktitle: Tambahkan Header dan Footer
type: docs
weight: 70
url: /id/java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk Java memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Stempel PDF sering digunakan dalam kontrak, laporan, dan materi terbatas, untuk membuktikan bahwa dokumen telah ditinjau dan ditandai sebagai "dibaca", "berkualifikasi", atau "rahasia", dll. Artikel ini akan menunjukkan kepada Anda bagaimana kita dapat menambahkan stempel gambar dan stempel teks ke dokumen PDF dengan menggunakan **Aspose.PDF untuk Java**.

Jika Anda membaca potongan kode di atas baris demi baris, Anda harus menemukan bahwa sintaks dan logika kode cukup mudah dipahami.

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) untuk menambahkan teks di header file PDF.
 TextStamp class menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di header PDF.

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

Cuplikan kode berikut menunjukkan cara menambahkan teks di header file PDF dengan Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Buat header
        TextStamp textStamp = new TextStamp("Header Text");

        // Atur properti dari stempel
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Tambahkan header di semua halaman
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di footer, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di footer PDF.

Cuplikan kode berikut menunjukkan cara menambahkan teks di footer file PDF dengan Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Buat footer
        TextStamp textStamp = new TextStamp("Footer Text");
        // Atur properti dari stempel
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Tambahkan footer pada semua halaman
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Simpan file PDF yang diperbarui
        pdfDocument.save(_dataDir);
    }
```


## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat cap berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) dari Page untuk menambahkan gambar di header PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Buka dokumen
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Buat header
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Setel properti dari cap
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Tambahkan header di semua halaman
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Simpan file PDF yang diperbarui
pdfDocument.save(_dataDir);
}
```


Kode cuplikan berikut menunjukkan cara menambahkan gambar di header file PDF dengan Java.

## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas Image Stamp untuk menambahkan gambar di footer file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Halaman untuk menambahkan gambar di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti BottomMargin sedemikian rupa sehingga menyesuaikan gambar di area footer PDF Anda. Anda juga perlu mengatur [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) ke `Center` dan [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) ke `Bottom`.

{{% /alert %}}

Kode cuplikan berikut menunjukkan cara menambahkan gambar di footer file PDF dengan Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Buat footer
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Atur properti dari cap
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Tambahkan footer pada semua halaman
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Simpan file PDF yang diperbarui
        pdfDocument.save(_dataDir);
    }
```

## Menambahkan Header yang berbeda dalam satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF.
 **Aspose.PDF untuk Java** menjelaskan cara melakukan ini.

Untuk memenuhi persyaratan ini, kita akan membuat objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individual (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF. Kita juga dapat menentukan informasi pemformatan yang berbeda untuk setiap objek cap. Dalam contoh berikut, kami telah membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan tiga objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) dan kemudian kami menggunakan metode [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) dari Page untuk menambahkan teks di bagian header PDF. Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan gambar di footer file PDF dengan Aspose.PDF untuk Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // Buka dokumen sumber
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Buat tiga cap
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // Atur penyelarasan cap (tempatkan cap di bagian atas halaman, dipusatkan secara horizontal)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Tentukan gaya font sebagai Bold
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Atur informasi warna latar depan teks sebagai merah
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Tentukan ukuran font sebagai 14
        stamp1.getTextState().setFontSize(14);

        // Sekarang kita perlu mengatur penyelarasan vertikal objek cap ke-2 sebagai Top
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Atur informasi penyelarasan Horizontal untuk cap sebagai Center aligned
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Atur faktor zoom untuk objek cap
        stamp2.setZoom (10);

        // Atur pemformatan objek cap ke-3
        // Tentukan informasi penyelarasan Vertikal untuk objek cap sebagai TOP
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Atur informasi penyelarasan Horizontal untuk objek cap sebagai Center aligned
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // Atur sudut rotasi untuk objek cap
        stamp3.setRotateAngle(35);
        // Atur warna latar belakang cap sebagai merah muda
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // Ubah informasi jenis huruf untuk cap ke Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // Cap pertama ditambahkan pada halaman pertama;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // Cap kedua ditambahkan pada halaman kedua;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // Cap ketiga ditambahkan pada halaman ketiga.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Simpan file PDF yang diperbarui
        pdfDocument.save(_dataDir);
    }

}
```