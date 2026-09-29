---
title: Gabungkan File PDF dalam Java
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/java/merge-pdf-documents/
description: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen dalam Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan dokumen penuh, rentang yang dipilih, dan halaman bergantian dengan Java
Abstract: Artikel ini menjelaskan cara menggabungkan dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup menggabungkan dua file, menggabungkan beberapa dokumen, memilih rentang halaman, menyisipkan satu dokumen ke dokumen lain pada posisi tertentu, mengalternasikan halaman, dan membangun output gabungan dengan bookmark bagian.
---
Aspose.PDF for Java mendukung beberapa strategi penggabungan tergantung pada bagaimana output harus disusun.

## Gabungkan dua dokumen PDF

Gunakan pendekatan ini ketika Anda membutuhkan alur penggabungan paling sederhana dan ingin menambahkan satu dokumen lengkap ke dokumen lain.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) koleksi dari dokumen kedua ke dokumen pertama.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Salin rentang halaman yang dipilih antara dokumen

Metode pembantu ini menjaga logika penggabungan rentang halaman di satu tempat sehingga contoh lain dapat menggunakan kembali prosedur penyalinan yang telah divalidasi yang sama.

1. Buka atau terima PDF sumber dan tujuan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Normalisasi rentang halaman yang diminta sehingga tetap berada dalam yang tersedia [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) koleksi.
1. Tambahkan setiap halaman dari rentang yang divalidasi ke dokumen tujuan.

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## Gabungkan beberapa dokumen PDF menjadi satu file

Gunakan pola ini ketika Anda perlu menggabungkan daftar file input menjadi satu dokumen output secara berurutan.

1. Buat PDF output kosong [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buka setiap file input satu per satu dan salin seluruhnya [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rentang ke dalam dokumen keluaran.
1. Simpan hasil gabungan setelah semua file sumber diproses.

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## Gabungkan rentang halaman terpilih dari dua dokumen

Contoh ini membuat file output khusus dengan mengambil hanya rentang halaman tertentu dari setiap dokumen sumber.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek dan buat dokumen output baru.
1. Tambahkan hanya yang diperlukan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rentang dari setiap dokumen sumber.
1. Simpan dokumen output yang dirakit.

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## Sisipkan satu dokumen PDF ke dalam dokumen lain pada posisi tertentu

Gunakan pendekatan ini ketika satu dokumen harus muncul di dalam dokumen lain, bukan hanya sebelum atau sesudahnya.

1. Buka PDF dasar dan PDF yang disisipkan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek dan buat dokumen output baru.
1. Salin bagian pertama dari dokumen dasar, kemudian tambahkan seluruh dokumen yang disisipkan, dan akhirnya tambahkan sisa dokumen dasar [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rentang.
1. Simpan hasil yang diurutkan kembali ke file baru.

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## Gabungkan dua dokumen PDF dengan cara menukar halaman secara bergantian

Contoh ini menumpuk halaman dari dua dokumen secara berselang-seling, yang berguna ketika kedua masukan harus berkontribusi halaman demi halaman ke output akhir.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek dan buat dokumen output baru.
1. Lakukan loop melalui jumlah halaman maksimum yang tersedia dan tambahkan masing‑masing yang tersedia [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dari dokumen pertama dan kedua secara berurutan.
1. Simpan dokumen output yang terinterleaved.

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## Gabungkan dokumen dengan halaman pemisah dan penanda

Gunakan pola ini ketika file gabungan harus tetap mudah dinavigasi dan jelas menunjukkan di mana setiap dokumen sumber dimulai.

1. Buat PDF output kosong [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka masing-masing file sumber secara berurutan.
1. Tambahkan pemisah [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dengan judul, lalu buat sebuah [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) penanda untuk bagian itu.
1. Tambahkan halaman sumber, secara opsional tambahkan bookmark yang mengarah ke halaman konten pertama, dan simpan dokumen gabungan akhir.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
