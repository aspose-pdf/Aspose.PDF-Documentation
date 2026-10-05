---
title: "Menambahkan Bates numbering ke PDF dalam Java"
linktitle: "Menambahkan Bates numbering"
type: docs
weight: 10
url: /id/java/add-bates-numbering/
description: Pelajari cara menambahkan dan menghapus Bates numbering pada dokumen PDF menggunakan Java dengan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan Bates numbering via Java"
Abstract: Artikel ini menjelaskan cara membuat dan menghapus artefak penomoran Bates dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup konfigurasi `BatesNArtifact`, menerapkannya melalui bantuan penomoran Bates atau bantuan paginasi umum, dan menghapus penomoran Bates dari sebuah dokumen.
---
Artefak penomoran Bates berguna dalam alur kerja hukum, arsip, dan kontrol dokumen di mana setiap halaman membutuhkan pengidentifikasi tingkat halaman yang persisten.

## Menambahkan penomoran Bates dengan bantuan khusus

Gunakan contoh ini ketika Anda ingin menerapkan penomoran Bates melalui bantuan koleksi halaman khusus.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman tambahan yang diperlukan oleh contoh.
1. Buat [`BatesNArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) konfigurasi.
1. Terapkan penomoran Bates ke koleksi halaman dan simpan file output.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan penomoran Bates melalui artefak paginasi

Contoh ini menerapkan penomoran Bates dengan melewatkan artefak Bates melalui API pagination generik.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman yang diperlukan.
1. Buat [`BatesNArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) dan tambahkan ke dalam daftar artefak pagination.
1. Terapkan artefak pagination ke koleksi halaman dan simpan dokumen.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Menghapus penomoran Bates

Gunakan pendekatan ini ketika artefak penomoran Bates yang ada harus dihapus dari dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil helper koleksi halaman yang menghapus penomoran Bates.
1. Simpan file output yang sudah dibersihkan.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
