---
title: Tambah dan Hapus Penanda Buku
linktitle: Tambah dan Hapus Penanda Buku
type: docs
weight: 10
url: /id/java/add-and-delete-bookmark/
description: Anda dapat menambahkan penanda buku ke dokumen PDF dengan Java. Dimungkinkan untuk menghapus semua atau penanda buku tertentu dari dokumen PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambah Penanda Buku ke Dokumen PDF

Penanda buku disimpan dalam koleksi objek Dokumen [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), yang ada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Untuk menambahkan penanda buku ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Buat penanda buku dan definisikan propertinya.
1. Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) ke koleksi Outlines.

Cuplikan kode berikut menunjukkan cara menambahkan penanda buku dalam dokumen PDF.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Buat objek bookmark
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Atur nomor halaman tujuan
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Tambahkan bookmark dalam koleksi outline dokumen.
        pdfDocument.getOutlines().add(pdfOutline);

        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## Tambahkan Penanda Anak ke Dokumen PDF

Penanda dapat dinestifikasi, menunjukkan hubungan hierarki dengan penanda induk dan anak. Artikel ini menjelaskan cara menambahkan penanda anak, yaitu penanda tingkat kedua, ke PDF.

Untuk menambahkan penanda anak ke file PDF, pertama tambahkan penanda induk:

1. Buka dokumen.
1. Tambahkan penanda ke [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), mendefinisikan properti-propertinya.
1. Tambahkan OutlineItemCollection ke koleksi objek Dokumen [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Penanda anak dibuat sama seperti penanda induk, dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines penanda induk.

Cuplikan kode berikut menunjukkan cara menambahkan penanda anak ke dokumen PDF.

```java
    public static void AddChildBookmark() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Buat objek penanda induk
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Buat objek penanda anak
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Tambahkan penanda anak ke koleksi penanda induk
        pdfOutline.add(pdfChildOutline);
        // Tambahkan penanda induk ke koleksi outline dokumen.
        pdfDocument.getOutlines().add(pdfOutline);

        // Simpan output
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## Hapus Semua Penanda dari Dokumen PDF

Semua penanda dalam PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Artikel ini menjelaskan cara menghapus semua penanda dari file PDF.

Untuk menghapus semua penanda dari file PDF:

1. Panggil metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Simpan file yang telah dimodifikasi menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara menghapus semua penanda dari dokumen PDF.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Hapus semua penanda
        pdfDocument.getOutlines().delete();

        // Simpan file yang telah diperbarui
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```


## Hapus Penanda Tertentu dari Dokumen PDF

[Delete All Attachments from PDF document](https://docs.aspose.com/pdf/java/working-with-attachments/) menunjukkan cara menghapus semua lampiran dari file PDF. Juga dimungkinkan untuk hanya menghapus lampiran tertentu.

Untuk menghapus penanda buku tertentu dari file PDF:

1. Masukkan judul penanda buku sebagai parameter ke metode [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. Kemudian simpan file yang diperbarui dengan metode Save dari objek Document.

Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Metode [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) menghapus penanda buku apa pun dengan judul yang diteruskan ke metode tersebut.

Cuplikan kode berikut menunjukkan cara menghapus penanda buku tertentu dari dokumen PDF.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Hapus outline tertentu berdasarkan Judul
        pdfDocument.getOutlines().delete("Child Outline");

        // Simpan file yang diperbarui
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```