---
title: Manipulasi Tabel di PDF yang Ada
linktitle: Manipulasi Tabel
type: docs
weight: 30
url: /id/java/manipulate-tables-in-existing-pdf/
description: Manipulasi tabel dalam file PDF yang ada dan ganti tabel lama dengan yang baru dalam dokumen PDF dengan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipulasi tabel di PDF yang ada

Salah satu fitur paling awal yang didukung oleh Aspose.PDF untuk Java adalah kemampuannya untuk Bekerja dengan Tabel dan menyediakan dukungan yang luar biasa untuk menambahkan tabel dalam file PDF yang dihasilkan dari awal atau file PDF yang sudah ada.
 You juga mendapatkan kemampuan untuk Mengintegrasikan Tabel dengan Database (DOM) untuk membuat tabel dinamis berdasarkan isi database. Dalam rilis baru ini, kami telah menerapkan fitur baru pencarian dan parsing tabel sederhana yang sudah ada di halaman dokumen PDF. Sebuah kelas baru bernama **Aspose.PDF.Text.TableAbsorber** menyediakan kemampuan ini. Penggunaan TableAbsorber sangat mirip dengan kelas TextFragmentAbsorber yang ada.

Cuplikan kode berikut menunjukkan langkah-langkah untuk memperbarui konten dalam sel tabel tertentu.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // Muat file PDF yang ada
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Buat objek TableAbsorber untuk menemukan tabel
        TableAbsorber absorber = new TableAbsorber();

        // Kunjungi halaman pertama dengan absorber
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Dapatkan akses ke tabel pertama di halaman, sel pertama mereka dan fragmen teks di dalamnya
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Ubah teks dari fragmen teks pertama di sel
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Ganti Tabel Lama dengan yang Baru dalam Dokumen PDF

Jika Anda perlu menemukan tabel tertentu dan menggantinya dengan yang diinginkan, Anda dapat menggunakan metode Replace() dari Kelas [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) untuk melakukannya.

Contoh berikut menunjukkan fungsionalitas untuk mengganti tabel di dalam dokumen PDF:

```java
public static void ReplaceOldTableWithNew() {

        // Muat dokumen PDF yang ada
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Buat objek TableAbsorber untuk menemukan tabel
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Kunjungi halaman pertama dengan absorber
        absorber.visit(page);

        // Dapatkan tabel pertama di halaman
        AbsorbedTable table = absorber.getTableList().get(0);

        // Buat tabel baru
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Kolom 1");
        row.getCells().add("Kolom 2");
        row.getCells().add("Kolom 3");

        // Ganti tabel dengan yang baru
        absorber.replace(page, table, newTable);

        // Simpan dokumen
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```