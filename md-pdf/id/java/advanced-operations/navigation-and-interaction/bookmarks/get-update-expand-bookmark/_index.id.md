---
title: Get, Update and Expand a Bookmark 
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Artikel ini menjelaskan cara menggunakan bookmark dalam file PDF. Dengan pustaka Java kami, Anda dapat mengambil bookmark dari file PDF, mendapatkan nomor halaman bookmark, memperbarui bookmark dalam Dokumen PDF, dan memperluas bookmark saat melihat dokumen.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Bookmark

Koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) berisi semua bookmark dari file PDF. Artikel ini menjelaskan cara mendapatkan bookmark dari file PDF, dan cara mendapatkan halaman mana yang ditandai oleh bookmark tertentu.

Untuk mendapatkan bookmark, lakukan iterasi melalui koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) dan dapatkan setiap bookmark dalam OutlineItemCollection.
 The OutlineItemCollection menyediakan akses ke semua atribut penanda buku. Cuplikan kode berikut menunjukkan cara mendapatkan penanda buku dari file PDF.

```java
    public static void GettingBookmarks() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Loop melalui semua penanda buku
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Judul :- " + outlineItem.getTitle());
            System.out.println("Miring :- " + outlineItem.getItalic());
            System.out.println("Tebal :- " + outlineItem.getBold());
            System.out.println("Warna :- " + outlineItem.getColor());
        }
    }
```

## Mendapatkan Nomor Halaman Penanda Buku

Setelah Anda menambahkan penanda buku, Anda dapat mengetahui halaman mana yang terdapat penanda buku tersebut dengan mendapatkan PageNumber tujuan yang terkait dengan objek Penanda Buku.

```java
    public static void GettingBookmarksPageNumber() {
        // Buat PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Buka file PDF
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Ekstrak penanda buku
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Judul :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Nomor Halaman :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Aksi Halaman :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Memperbarui Penanda Buku dalam Dokumen PDF

Untuk memperbarui penanda buku dalam file PDF, pertama, dapatkan penanda buku tertentu dari koleksi OutlineCollection objek Dokumen dengan menentukan indeks penanda buku. Setelah Anda mendapatkan penanda buku ke dalam objek [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection), Anda dapat memperbarui propertinya dan kemudian menyimpan file PDF yang telah diperbarui menggunakan metode Save. Potongan kode berikut menunjukkan bagaimana memperbarui penanda buku dalam dokumen PDF.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Dapatkan objek penanda buku
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Perbarui objek penanda buku
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Tetapkan halaman tujuan sebagai 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Simpan output
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Memperbarui Bookmark Anak dalam Dokumen PDF

Untuk memperbarui bookmark anak:

1. Ambil bookmark anak yang ingin Anda perbarui dari file PDF dengan terlebih dahulu mendapatkan bookmark induk dan kemudian bookmark anak menggunakan nilai indeks yang sesuai.
1. Simpan file PDF yang telah diperbarui menggunakan metode Save.

{{% alert color="primary" %}}

Dapatkan bookmark dari koleksi OutlineCollection objek Document dengan menentukan indeks bookmark, dan kemudian dapatkan bookmark anak dengan menentukan indeks dari bookmark induk ini.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara memperbarui bookmark anak dalam dokumen PDF.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Buka dokumen
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Dapatkan objek bookmark
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Dapatkan objek bookmark anak
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Perbarui objek bookmark
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Tetapkan halaman target sebagai 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Simpan output
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Bookmark Diperluas saat melihat dokumen

Bookmark disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) dari objek Dokumen, yang merupakan bagian dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Namun, kita mungkin memiliki persyaratan untuk memperluas semua bookmark saat melihat file PDF.

Untuk memenuhi persyaratan ini, kita dapat mengatur status terbuka untuk setiap item outline/bookmark sebagai Terbuka. Cuplikan kode berikut menunjukkan cara mengatur status terbuka untuk setiap bookmark sebagai diperluas dalam dokumen PDF.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // atur mode tampilan halaman yaitu tampilkan thumbnail, layar penuh, tampilkan panel lampiran
        doc.setPageMode(PageMode.UseOutlines);
        // cetak jumlah total Bookmark dalam file PDF
        System.out.println(doc.getOutlines().size());
        // menelusuri setiap item Outline dalam koleksi outline file PDF
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // atur status terbuka untuk item outline
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // simpan file PDF
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```