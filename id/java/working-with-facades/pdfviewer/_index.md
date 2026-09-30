---
title: Kelas PdfViewer
linktitle: Kelas PdfViewer
type: docs
weight: 135
url: /id/java/pdfviewer-class/
description: "Pelajari cara menggunakan fasad PdfViewer dalam Java untuk mendekode halaman PDF dan memeriksa pengaturan yang terkait dengan viewer."
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mendekode halaman PDF dan memeriksa data viewer dalam Java dengan PdfViewer"
Abstract: "Bagian ini menjelaskan cara menggunakan fasad PdfViewer dalam Aspose.PDF for Java untuk tugas dekode halaman dan inspeksi yang terkait dengan viewer. Contoh Java saat ini mencakup rendering semua halaman ke gambar, mendekode halaman tertentu, dan memeriksa jumlah halaman, tipe koordinat, resolusi, serta pengaturan viewer yang terikat."
---
Kelas `PdfViewerExamples` dalam Java menunjukkan alur kerja penampil utama yang tersedia melalui API Facades.

## Mendekode semua halaman PDF

Gunakan alur kerja ini ketika setiap halaman PDF sumber harus dirender sebagai gambar.

### Langkah

1. Buat dan konfigurasikan sebuah instans `PdfViewer`.
2. Ikat PDF sumber dengan `bindPdf`.
3. Panggil `decodeAllPages()` untuk merender dokumen menjadi `BufferedImage` larik.
4. Simpan setiap halaman yang telah didekode ke file gambar output.
5. Tutup file PDF yang terikat.

### Contoh Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Mendekode halaman PDF tertentu

Gunakan alur kerja ini ketika hanya satu halaman yang perlu dirender menjadi gambar.

### Langkah

1. Buat dan konfigurasikan sebuah instans `PdfViewer`.
2. Ikat PDF sumber.
3. Panggil `decodePage()` untuk halaman yang ingin Anda render.
4. Simpan halaman yang telah didekode ke file gambar output.
5. Tutup penampil.

### Contoh Java

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## Memeriksa metadata PDF

Gunakan alur kerja ini ketika Anda memerlukan informasi dokumen terkait penampil sebelum merender atau mencetak.

### Langkah

1. Buat dan konfigurasikan sebuah instans `PdfViewer`.
2. Ikat PDF sumber.
3. Baca jumlah halaman, tipe koordinat, dan resolusi rendering.
4. Gunakan atau cetak nilai yang diambil.
5. Tutup file PDF yang terikat.

### Contoh Java

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## Memeriksa pengaturan penampil yang terikat

Gunakan alur kerja ini ketika Anda perlu mengonfirmasi atau menyesuaikan perilaku penampil setelah mengikat PDF.

### Langkah

1. Buat dan konfigurasikan sebuah instans `PdfViewer`.
2. Ikat PDF sumber.
3. Atur opsi penampil seperti otomatis-ubah ukuran, otomatis-putar, dan visibilitas dialog cetak.
4. Baca pengaturan penampil aktif dan jumlah halaman.
5. Tutup penampil.

### Contoh Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
