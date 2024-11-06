---
title: Bekerja dengan Heading dalam PDF
type: docs
weight: 70
url: id/java/working-with-headings/
lastmod: "2021-06-05"
description: Buat penomoran dalam heading dokumen PDF Anda dengan Java. Aspose.PDF untuk Java menawarkan berbagai jenis gaya penomoran.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Terapkan Gaya Penomoran dalam Heading

Heading adalah bagian penting dari setiap dokumen. Penulis selalu berusaha membuat heading lebih menonjol dan bermakna bagi pembacanya. Jika ada lebih dari satu heading dalam dokumen, penulis memiliki beberapa opsi untuk mengatur heading tersebut. Salah satu pendekatan paling umum untuk mengatur heading adalah menulis heading dalam Gaya Penomoran.

Aspose.PDF untuk Java menawarkan banyak gaya penomoran yang sudah ditentukan sebelumnya. Gaya penomoran yang sudah ditentukan sebelumnya ini disimpan dalam enumerasi, NumberingStyle. Nilai-nilai yang sudah ditentukan dari enumerasi NumberingStyle dan deskripsi mereka diberikan di bawah ini:

|**Jenis Heading**|**Deskripsi**|
| :- | :- |
|NumeralsArabic|Tipe Arab, misalnya, 1,1.1,...|

|NumeralsRomanUppercase|Tipe Romawi atas, misalnya, I,I.II, ...|
|NumeralsRomanLowercase|Tipe romawi kecil, misalnya, i,i.ii, ...|
|LettersUppercase|Tipe huruf besar bahasa Inggris, misalnya, A,A.B, ...|
|LettersLowercase|Tipe huruf kecil bahasa Inggris, misalnya, a,a.b, ...|
Properti [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dari kelas [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) digunakan untuk mengatur gaya penomoran dari judul.

Kode sumber, untuk mendapatkan output yang ditunjukkan pada gambar di atas, diberikan di bawah dalam contoh.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("Daftar 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("Daftar 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("nilai, pada tanggal efektif rencana, dari properti yang akan didistribusikan di bawah rencana sehubungan dengan setiap yang diizinkan");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```