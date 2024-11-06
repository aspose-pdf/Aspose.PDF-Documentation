---
title: Menghapus Tabel dari PDF yang Ada
linktitle: Hapus Tabel
type: docs
weight: 40
url: id/java/remove-tables-from-existing-pdf/
description: Aspose.PDF untuk Java memungkinkan Anda menghapus tabel dan beberapa tabel dari dokumen PDF Anda.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF untuk Java menawarkan kemampuan untuk memasukkan/membuat Tabel di dalam dokumen PDF saat sedang dibuat dari awal atau Anda juga dapat menambahkan objek tabel dalam dokumen PDF yang sudah ada. Namun Anda mungkin memiliki persyaratan untuk [Memanipulasi Tabel dalam PDF yang Ada](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) di mana Anda dapat memperbarui konten dalam sel tabel yang ada. Namun Anda mungkin menghadapi persyaratan untuk menghapus objek tabel dari dokumen PDF yang ada.

{{% /alert %}}

Untuk menghapus tabel, kita perlu menggunakan kelas [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) untuk mendapatkan tabel dalam PDF yang ada dan kemudian memanggil metode [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-).

## Menghapus Tabel dari Dokumen PDF

Kami telah menambahkan fungsi baru yaitu Remove() ke dalam Kelas [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) yang ada untuk menghapus tabel dari dokumen PDF. Setelah absorber berhasil menemukan tabel di halaman, ia dapat menghapusnya. Silakan periksa cuplikan kode berikut yang menunjukkan cara menghapus tabel dari dokumen PDF:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Memuat dokumen PDF yang ada
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Membuat objek TableAbsorber untuk menemukan tabel
        TableAbsorber absorber = new TableAbsorber();

        // Kunjungi halaman pertama dengan absorber
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Mendapatkan tabel pertama di halaman
        AbsorbedTable table = absorber.getTableList().get(0);

        // Hapus tabel
        absorber.remove(table);

        // Simpan PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## Hapus Beberapa Tabel dari Dokumen PDF

Terkadang sebuah dokumen PDF mungkin berisi lebih dari satu tabel dan Anda mungkin memiliki persyaratan untuk menghapus beberapa tabel darinya. Untuk menghapus beberapa tabel dari dokumen PDF, silakan gunakan potongan kode berikut:

```java
    public static void RemoveMultipleTable() {
        // Muat dokumen PDF yang ada
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Buat objek TableAbsorber untuk menemukan tabel
        TableAbsorber absorber = new TableAbsorber();

        // Kunjungi halaman kedua dengan absorber
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Loop melalui salinan koleksi dan menghapus tabel
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Simpan dokumen
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```