---
title: "Mengonversi PDF/A dan PDF/UA ke PDF dalam Java"
linktitle: "Mengonversi PDF/A dan PDF/UA ke PDF"
type: docs
weight: 120
url: /id/java/convert-pdf_x-to-pdf/
lastmod: "2026-09-30"
description: Pelajari cara menghapus kepatuhan PDF/A dan PDF/UA dari file PDF berbasis standar dalam Java dan menyimpannya sebagai dokumen PDF standar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Mengonversi PDF/A dan PDF/UA ke PDF standar dalam Java"
Abstract: Artikel ini menjelaskan cara menghapus kepatuhan PDF/A dan PDF/UA dari dokumen PDF berbasis standar menggunakan Aspose.PDF for Java, kemudian menyimpan hasilnya sebagai file PDF standar.
---
Aspose.PDF for Java dapat mengonversi variasi PDF yang mematuhi standar kembali ke dokumen PDF biasa.

## Mengonversi PDF/A ke PDF standar

Gunakan contoh ini ketika dokumen PDF/A arsip harus diturunkan menjadi PDF standar.

1. Buka file PDF/A sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `removePdfaCompliance()` untuk melepaskan profil kepatuhan arsip dari dokumen yang dimuat.
1. Simpan file PDF standar yang dihasilkan tanpa mengatur pembatasan PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Mengonversi PDF/UA ke PDF standar

Gunakan contoh ini ketika dokumen PDF/UA yang dapat diakses harus dikonversi kembali menjadi PDF standar.

1. Buka file PDF/UA sumber di sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `removePdfUaCompliance()` untuk menghapus profil kepatuhan aksesibilitas dari metadata dokumen dan persyaratan struktur.
1. Simpan dokumen PDF hasil sebagai file PDF biasa.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
