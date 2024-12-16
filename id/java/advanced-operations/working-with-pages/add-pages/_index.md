---
title: Tambahkan Halaman dalam PDF 
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /id/java/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan pustaka Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan atau Sisipkan Halaman dalam File PDF

Aspose.PDF untuk Java memungkinkan Anda menyisipkan halaman ke dalam dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF. Anda perlu memberikan lokasi di mana Anda ingin menyisipkan halaman kosong ke metode insert. Bagian ini menunjukkan cara menambahkan halaman ke PDF dengan Aspose.PDF untuk Java.

### Sisipkan Halaman Kosong dalam File PDF di Lokasi yang Diinginkan

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong ke dalam file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF input.

1. Panggil metode Insert dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) dengan indeks yang ditentukan.
1. Simpan PDF keluaran menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman dalam file PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Tambahkan halaman
        document.getPages().add();

        // Sisipkan halaman kosong ke dalam PDF
        document.getPages().insert(2);

        // Simpan PDF yang diperbarui
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

Pada contoh di atas, kami menambahkan halaman kosong dengan parameter default. Jika Anda perlu membuat ukuran halaman sama dengan halaman lain dalam dokumen, Anda harus menambahkan beberapa baris kode:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Tambahkan halaman
        Page page1 = document.getPages().add();

        // Sisipkan halaman kosong ke dalam PDF
        Page page2 = document.getPages().insert(2);
        ;
        // salin parameter halaman dari halaman 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Simpan PDF yang diperbarui
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir pada halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF input.
1. Panggil metode Add koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection), tanpa parameter apapun.
1. Simpan PDF output menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Tambahkan halaman
        document.getPages().add();

        // Sisipkan halaman kosong di akhir file PDF
        document.getPages().add();

        // Simpan PDF yang diperbarui
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```