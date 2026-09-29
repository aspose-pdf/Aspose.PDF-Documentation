---
title: Membagi File PDF dalam Java
linktitle: Membagi file PDF
type: docs
weight: 60
url: /id/java/split-pdf/
description: Pelajari cara membagi PDF menjadi file PDF satu halaman dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membagi halaman PDF menggunakan Java
Abstract: Artikel ini menunjukkan cara membagi dokumen PDF menjadi file PDF satu halaman terpisah dalam Java menggunakan Aspose.PDF. Contoh ini membuka dokumen sumber, mengiterasi halamannya, membuat dokumen baru untuk setiap halaman, dan menyimpan setiap halaman sebagai file PDF individual.
---
Membagi PDF menjadi file terpisah berguna ketika Anda perlu mengekspor setiap halaman untuk peninjauan, penyimpanan, atau pemrosesan lanjutan.

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi online gratis untuk menguji pemisahan PDF di peramban.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Contoh ini menggunakan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) kelas untuk membuka file PDF dan mengiterasi halamannya. Untuk setiap [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), ia membuat dokumen baru, menambahkan halaman itu, dan menyimpan hasilnya sebagai file PDF terpisah.

Untuk memisahkan PDF menjadi file halaman individual dalam Java:

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) konstruktor.
1. Iterasikan melalui [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objek yang dikembalikan oleh `document.getPages()`.
1. Buat yang kosong baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk setiap halaman.
1. Tambahkan yang saat ini [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke yang baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan yang baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan nama file unik.
1. Tutup keduanya [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek ketika pemrosesan selesai.

## Pisahkan PDF menjadi file satu halaman

Contoh Java berikut didasarkan pada `SplitDocumentExamples.java` dan menyimpan halaman sebagai `Page_1.pdf`, `Page_2.pdf`, dan seterusnya.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
