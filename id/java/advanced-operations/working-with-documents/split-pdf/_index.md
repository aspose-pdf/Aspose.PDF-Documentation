---
title: "Memisahkan file PDF dalam Java"
linktitle: "Memisahkan file PDF"
type: docs
weight: 60
url: /id/java/split-pdf-document/
description: Pelajari cara membagi halaman PDF menjadi file PDF terpisah dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Membagi dokumen PDF berdasarkan halaman, rentang, grup, dan pola nama file menggunakan Java"
Abstract: Artikel ini menjelaskan cara memecah dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pemecahan menjadi halaman tunggal, dua atau tiga bagian, halaman ganjil dan genap, potongan berukuran tetap, rentang khusus, halaman pertama atau terakhir ditambah sisanya, kelompok halaman khusus, dan pembuatan nama file yang stabil.
---
Aspose.PDF for Java mendukung beberapa pola pemisahan selain output satu halaman per file.

## Memisahkan PDF menjadi file satu halaman

Gunakan pendekatan ini ketika setiap halaman sumber harus menjadi dokumen keluaran terpisah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) untuk setiap [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) Anda ingin mengekspor.
1. Tambahkan yang dipilih [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen baru.
1. Simpan setiap output PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## Memisahkan PDF menjadi dua bagian

Contoh ini membagi dokumen sumber menjadi dua file output berurutan berdasarkan titik tengah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hitung titik tengah yang tersedia [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) koleksi.
1. Salin setengah pertama halaman ke dalam satu dokumen keluaran dan halaman yang tersisa ke dokumen lain.
1. Simpan kedua dokumen hasil.

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## Memisahkan PDF menjadi grup halaman berukuran tetap

Gunakan pola ini ketika setiap file output harus berisi jumlah halaman yang sama, kecuali mungkin bagian terakhir.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lakukan perulangan melalui [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) koleksi dalam grup `pagesPerPart`.
1. Buat dokumen output baru untuk setiap grup dan salin rentang halaman yang dihitung ke dalamnya.
1. Simpan setiap bagian dengan nama file yang dihasilkan.

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## Memisahkan PDF berdasarkan rentang halaman khusus

Contoh ini memungkinkan Anda menentukan halaman awal dan akhir secara eksplisit untuk setiap dokumen output.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tentukan yang diperlukan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rentang dalam array atau koleksi lain.
1. Validasi setiap rentang terhadap jumlah halaman sumber dan salin halaman yang cocok ke dalam dokumen baru.
1. Simpan setiap file output berbasis rentang.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## Memisahkan halaman pertama dan halaman-halaman yang tersisa

Gunakan pendekatan ini ketika halaman sampul harus diekspor secara terpisah dari sisa dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan konfirmasikan bahwa itu berisi halaman.
1. Buat satu dokumen output untuk yang pertama [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Buat dokumen lain untuk rentang halaman yang tersisa ketika lebih dari satu halaman tersedia.
1. Simpan kedua hasil.

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## Memisahkan halaman terakhir dan halaman-halaman sebelumnya

Contoh ini memisahkan halaman terakhir dari sisa dokumen, yang berguna untuk mengekstrak halaman ringkasan atau tanda tangan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan periksa bahwa tidak kosong.
1. Salin yang terakhir [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dalam dokumen output baru.
1. Hapus halaman itu dari dokumen asli ketika halaman sebelumnya masih ada.
1. Simpan halaman terakhir dan halaman lainnya sebagai file terpisah.

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## Memisahkan PDF menjadi tiga bagian

Gunakan pola ini ketika dokumen harus dibagi menjadi tiga bagian berurutan dengan ukuran kira-kira sama.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tentukan total jumlah halaman.
1. Hitung perkiraan ukuran masing-masing bagian output.
1. Buat hingga tiga dokumen dan salin yang cocok [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rentang.
1. Simpan setiap bagian yang dihasilkan.

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## Membagi PDF menjadi grup halaman khusus

Contoh ini menunjukkan cara membuat file output dari kumpulan halaman yang tidak berurutan alih-alih rentang berkelanjutan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Definisikan grup khusus [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) angka.
1. Buat dokumen output baru untuk setiap grup dan tambahkan hanya halaman yang valid dari grup tersebut.
1. Simpan setiap dokumen grup yang tidak kosong.

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## Memisahkan PDF menjadi halaman tunggal dengan nama file yang stabil

Gunakan versi ini ketika nama output harus tetap dapat diurutkan secara leksikal, misalnya dalam pipeline otomatis.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat satu dokumen output untuk setiap [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Simpan setiap file dengan nomor halaman yang diisi nol di depan.

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## Memisahkan PDF menjadi halaman ganjil dan genap

Contoh ini membuat dua output dengan memisahkan halaman menurut paritas nomor halaman mereka.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat satu dokumen keluaran untuk ganjil [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) angka dan yang lain untuk nomor halaman genap.
1. Iterasikan halaman sumber dengan kenaikan yang diperlukan untuk setiap dokumen output.
1. Simpan hasil halaman ganjil dan halaman genap secara terpisah.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```
