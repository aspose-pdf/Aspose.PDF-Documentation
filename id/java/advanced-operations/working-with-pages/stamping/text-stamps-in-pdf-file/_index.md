---
title: Tambahkan Stempel Teks di PDF secara Programatis
linktitle: Stempel Teks di File PDF
type: docs
weight: 20
url: /id/java/text-stamps-in-the-pdf-file/
description: Tambahkan stempel teks ke file PDF menggunakan kelas TextStamp dengan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Teks dengan Java

Aspose.PDF untuk Java menyediakan kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) untuk menambahkan stempel teks dalam file PDF.
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) class menyediakan metode yang diperlukan untuk menentukan ukuran font, gaya font, dan warna font dll untuk objek cap. Untuk menambahkan cap teks, pertama-tama Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) menggunakan metode yang diperlukan. Setelah itu, Anda dapat memanggil metode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) untuk menambahkan cap ke dalam dokumen PDF.

Cuplikan kode berikut menunjukkan cara menambahkan cap teks ke dalam file PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // buka dokumen
        Document pdfDocument = new Document("input.pdf");
        // buat cap teks
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // atur apakah cap adalah latar belakang
        textStamp.setBackground(true);
        // atur asal
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // putar cap
        textStamp.setRotate(Rotation.on90);
        // atur properti teks
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // tambahkan cap ke halaman tertentu
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // simpan dokumen keluaran
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Menentukan perataan untuk objek TextStamp

Menambahkan watermark ke dokumen PDF adalah salah satu fitur yang sering diminta dan Aspose.PDF untuk Java sepenuhnya mampu menambahkan watermark Gambar serta Teks. Kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) menyediakan fitur untuk menambahkan stempel teks pada file PDF. Baru-baru ini ada permintaan untuk mendukung fitur menentukan perataan teks saat menggunakan objek [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Jadi untuk memenuhi kebutuhan ini, kami telah memperkenalkan metode setTextAlignment(..) dalam kelas [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Dengan menggunakan metode ini, Anda dapat menentukan perataan teks horizontal.

Cuplikan kode berikut menunjukkan contoh tentang cara memuat dokumen PDF yang sudah ada dan menambahkan [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) di atasnya.

```java
    public static void DefineAlignmentTextStamp() {
        // Membuat objek Dokumen dengan file input
        Document pdfDocument = new Document("input.pdf");
        // Membuat objek FormattedText dengan string contoh
        FormattedText text = new FormattedText("This");
        
        // menambahkan baris teks baru ke FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // membuat objek TextStamp menggunakan FormattedText
        TextStamp stamp = new TextStamp(text);
        // menentukan Perataan Horizontal teks stempel sebagai rata tengah
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // menentukan Perataan Vertikal teks stempel sebagai rata tengah
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // menentukan Perataan Teks Horizontal dari TextStamp sebagai rata tengah
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // menetapkan margin atas untuk objek stempel
        stamp.setTopMargin(20);
        // menambahkan stempel ke semua halaman file PDF
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // menyimpan dokumen keluaran
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## Isi Teks Stroke sebagai Stempel dalam File PDF

Kami telah mengimplementasikan pengaturan mode rendering untuk skenario penambahan dan pengeditan teks. Untuk merender teks stroke, silakan buat objek [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) dan atur RenderingMode ke TextRenderingMode.StrokeText dan juga pilih warna untuk properti StrokingColor. Kemudian, ikat TextState ke stempel menggunakan metode BindTextState().

Cuplikan kode berikut menunjukkan penambahan Isi Teks Stroke:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Buat objek TextState untuk mentransfer properti lanjutan
        TextState ts = new TextState();
        
        // Atur warna untuk stroke
        ts.setStrokingColor(Color.getGray());
        
        // Atur mode rendering teks
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Muat dokumen PDF masukan
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Ikat TextState
        stamp.bindTextState(ts);
        // Atur asal X,Y
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Tambahkan Stempel
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```