---
title: "Mengoptimalkan file PDF di Java"
linktitle: "Mengoptimalkan PDF"
type: docs
weight: 30
url: /id/java/optimize-pdf/
description: Pelajari cara mengoptimalkan, mengompres, dan mengurangi ukuran file PDF di Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengompresi sumber daya PDF dan mengurangi ukuran file dengan Java"
Abstract: Artikel ini menjelaskan cara mengoptimalkan file PDF menggunakan Aspose.PDF for Java. Ini mencakup optimisasi seluruh dokumen, kompresi sumber daya, pengurangan kualitas gambar, menghapus objek dan stream yang tidak terpakai, menautkan stream duplikat, mengeluarkan font yang ter‑embed, meratakan anotasi dan form, konversi ke skala abu‑abu, dan kompresi gambar Flate.
---
Aspose.PDF for Java mengekspos fitur optimisasi melalui `Document.optimize`, `optimizeResources`, dan `OptimizationOptions`.

## Mengoptimalkan PDF dengan optimisasi dokumen umum

Gunakan contoh ini ketika Anda ingin Aspose.PDF menerapkan rutinitas optimisasi seluruh dokumen bawaan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `optimize()` pada dokumen.
1. Simpan file yang dioptimalkan dan bandingkan ukuran asli serta ukuran output.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Mengurangi ukuran PDF dengan mengoptimalkan sumber daya

Contoh ini berfokus pada optimasi tingkat sumber daya tanpa mengkonfigurasi opsi individual secara manual.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Jalankan `optimizeResources()` untuk mengoptimalkan sumber daya internal.
1. Simpan hasilnya dan cetak ukuran file input serta output.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Mengompresi semua gambar dalam PDF

Gunakan pendekatan ini ketika dokumen yang banyak mengandung gambar membutuhkan ukuran file yang lebih kecil dan beberapa pengurangan kualitas gambar dapat diterima.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) dan aktifkan kompresi gambar dengan tingkat kualitas yang diperlukan.
1. Optimalkan sumber daya dokumen dengan pengaturan tersebut.
1. Simpan file yang dioptimalkan dan bandingkan ukuran file.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Menghapus objek yang tidak terpakai dari PDF

Contoh ini menghapus objek yang tidak terpakai yang mungkin tetap berada dalam struktur dokumen setelah penyuntingan atau penggabungan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) dan mengaktifkan penghapusan objek yang tidak terpakai.
1. Optimalkan sumber daya dan simpan file yang diperbarui.
1. Cetak ukuran file asli dan ukuran file yang diperkecil.

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Menghapus aliran yang tidak terpakai dari PDF

Gunakan pendekatan ini ketika Anda ingin membuang data aliran yang tidak lagi dirujuk oleh dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Konfigurasikan [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) untuk menghapus aliran yang tidak terpakai.
1. Optimalkan sumber daya, simpan dokumen output, dan bandingkan ukuran file.

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Menautkan aliran duplikat dalam PDF

Contoh ini menghilangkan duplikasi aliran yang berulang sehingga konten yang identik hanya dapat disimpan satu kali.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) dan mengaktifkan pengaitan aliran duplikat.
1. Optimalkan sumber daya, simpan dokumen keluaran, dan cetak ukuran file.

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Melepaskan font yang di‑embed dari PDF

Gunakan opsi ini ketika mengurangi ukuran file lebih penting daripada mempertahankan data font yang disematkan dalam output.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Konfigurasikan [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) untuk menghapus embed font.
1. Optimalkan sumber daya, simpan dokumen, dan bandingkan ukuran file.

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Meratakan anotasi dalam PDF

Contoh ini mengubah anotasi menjadi konten halaman statis sehingga mereka tidak lagi menjadi objek interaktif.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui setiap [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan miliknya [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) koleksi.
1. Ratakan setiap anotasi dan simpan dokumen yang diperbarui.

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Meratakan bidang formulir PDF

Gunakan pendekatan ini ketika bidang formulir yang dapat diisi harus menjadi konten tetap sebelum distribusi atau pengarsipan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Periksa apakah dokumen berisi widget formulir.
1. Ratakan masing-masing [`Field`](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) diwakili oleh sebuah [`WidgetAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Simpan file output dan cetak ukuran file.

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Mengubah PDF menjadi skala abu-abu

Contoh ini mengubah setiap halaman menjadi skala abu-abu, yang dapat membantu mengurangi kompleksitas warna dan menstandarisasi output untuk alur kerja pengarsipan atau pencetakan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui setiap [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dalam dokumen.
1. Panggil `makeGrayscale()` pada setiap halaman dan simpan file output.

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## Menggunakan kompresi gambar FlateDecode

Gunakan pola ini ketika Anda ingin menerapkan kompresi berbasis Flate pada gambar selama optimisasi sumber daya PDF.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`OptimizationOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) dan atur pengkodean gambar ke [`ImageEncoding`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. Optimalkan sumber daya dokumen dan simpan file output.

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## Mencetak ukuran file asli dan yang dioptimalkan

Metode pembantu ini melaporkan selisih ukuran antara file sumber dan file output yang dioptimalkan.

1. Baca ukuran file input.
1. Baca ukuran file output.
1. Cetak kedua nilai dalam satu pesan status.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
