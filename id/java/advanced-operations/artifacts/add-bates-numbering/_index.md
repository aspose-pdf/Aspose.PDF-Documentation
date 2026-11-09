---
title: Menambahkan penomoran Bates pada PDF dengan Java
linktitle: Menambahkan penomoran Bates
type: docs
weight: 10
url: /id/java/add-bates-numbering/
description: Tambahkan pengidentifikasi Bates berurutan ke halaman PDF dalam Java dengan bantuan penomoran Bates khusus atau API paginasi umum.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan penomoran Bates pada PDF dengan Java
Abstract: Tambahkan pengidentifikasi Bates berurutan ke halaman PDF dalam Java dengan bantuan penomoran Bates khusus atau API paginasi umum.
---
Artefak penomoran Bates berguna dalam alur kerja hukum, arsip, dan kontrol dokumen di mana setiap halaman memerlukan pengidentifikasi tingkat halaman yang tetap.

## Menambahkan penomoran Bates dengan metode khusus

Gunakan contoh ini ketika Anda ingin menerapkan penomoran Bates melalui pembantu koleksi halaman khusus.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman ekstra apa pun yang diperlukan oleh contoh.
1. Konfigurasikan objek [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Terapkan penomoran Bates pada koleksi halaman.
1. Simpan file keluaran.

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

Contoh ini menerapkan penomoran Bates dengan mengirimkan artefak Bates melalui API paginasi generik.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman yang diperlukan.
1. Buat [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) dan tambahkan ke dalam daftar artefak paginasi.
1. Terapkan artefak paginasi ke koleksi halaman.
1. Simpan dokumen.

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

## Topik terkait

- [Menghapus penomoran Bates](/pdf/id/java/remove-bates-numbering/)
- [Artefak PDF](/pdf/id/java/artifacts/)
