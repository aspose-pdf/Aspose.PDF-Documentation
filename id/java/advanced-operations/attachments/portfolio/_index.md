---
title: "Membuat portofolio PDF di Java"
linktitle: Portofolio
type: docs
weight: 20
url: /id/java/portfolio/
description: Pelajari cara membuat dan mengelola portofolio PDF di Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Membangun dan mengedit portofolio PDF dengan file tersemat di Java"
Abstract: Artikel ini menjelaskan cara membuat dan mengelola portofolio PDF menggunakan Aspose.PDF for Java. Pelajari cara mengaktifkan koleksi pada dokumen, menambahkan berbagai jenis file ke portofolio, dan menghapus semua item koleksi dari portofolio PDF yang ada.
---
Portofolio PDF dapat menggabungkan banyak file dalam satu kontainer PDF sekaligus menjaga setiap file dalam format aslinya.

## Membuat portofolio PDF

Gunakan contoh ini ketika Anda perlu mengemas beberapa file ke dalam koleksi portofolio PDF.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan aktifkan [`Collection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. Buat objek [`FileSpecification`](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) untuk setiap file input dan atur deskripsinya.
1. Tambahkan file ke koleksi portofolio dan simpan dokumen output.

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## Menghapus file dari portofolio PDF

Gunakan contoh ini ketika kumpulan portofolio PDF yang ada harus dibersihkan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus entri koleksi dokumen.
1. Simpan dokumen keluaran yang sudah dibersihkan.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
