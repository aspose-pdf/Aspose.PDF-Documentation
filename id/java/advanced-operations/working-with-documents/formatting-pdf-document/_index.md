---
title: "Format dokumen PDF dalam Java"
linktitle: "Memformat dokumen PDF"
type: docs
weight: 11
url: /id/java/formatting-pdf-document/
description: Pelajari cara memformat dokumen PDF, menyematkan font, mengontrol pengaturan penampil, dan menyesuaikan opsi tampilan di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format jendela dokumen, font, dan perilaku zoom dalam file PDF dengan Java
Abstract: Artikel ini menjelaskan cara memformat dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup membaca dan memperbarui pengaturan jendela dokumen, menyematkan font, mengatur font default, mendaftar font, membuat subset font yang disematkan, dan mengontrol faktor zoom awal.
---
Pemformatan di Aspose.PDF for Java mencakup perilaku penampil, penyematan font, dan pengaturan tampilan.

## Mendapatkan pengaturan jendela dokumen

Gunakan contoh ini untuk memeriksa preferensi penampil saat ini yang disimpan dalam dokumen PDF yang ada.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Baca properti jendela dan tampilan yang diperlukan dari dokumen.
1. Keluarkan pengaturan saat ini untuk inspeksi atau debugging.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## Mengatur preferensi jendela dokumen

Contoh ini memperbarui cara PDF harus ditampilkan ketika dibuka di penampil yang kompatibel.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Atur preferensi jendela, tata letak, dan mode halaman yang diperlukan.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## Menyematkan font dalam PDF yang ada

Gunakan pendekatan ini ketika dokumen harus menyertakan font yang diperlukan untuk memastikan rendering yang lebih dapat diandalkan di sistem lain.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Aktifkan penyematan font standar dan iterasi melalui font yang digunakan oleh masing-masing [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Tandai semua yang tidak tersemat objek [`Font`](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) untuk disematkan.
1. Simpan dokumen yang diperbarui.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Menyematkan font saat membuat PDF baru

Contoh ini membuat PDF baru dan menetapkan font yang disematkan ke konten teks sejak awal.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Buat yang diperlukan [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [`TextSegment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), dan [`TextState`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Selesaikan [`Font`](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) target dari repositori dan tandai sebagai tertanam.
1. Tambahkan konten teks ke halaman dan simpan dokumen output.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## Mengatur font default untuk output PDF

Gunakan pola ini ketika dokumen yang disimpan harus kembali ke font tertentu selama pembuatan output.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`PdfSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) dan atur nama font default.
1. Simpan dokumen dengan opsi penyimpanan yang dikonfigurasi.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Mendapatkan semua font yang digunakan dalam PDF

Contoh ini mencantumkan setiap font yang terdeteksi dalam dokumen sehingga Anda dapat mengaudit penggunaan font sebelum mengekspor atau memperbarui file.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerasikan font yang dikembalikan oleh utilitas font dokumen.
1. Keluarkan nama setiap yang terdeteksi [`Font`](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Meningkatkan penyematan font dengan menyubset font

Gunakan pendekatan ini ketika Anda ingin mengurangi payload font sambil menjaga data font tersemat tetap selaras dengan penggunaan dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Jalankan subsetting font melalui utilitas font dokumen dengan yang diperlukan [`FontSubsetStrategy`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) nilai.
1. Simpan dokumen yang dioptimalkan.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Mengatur faktor zoom saat membuka dokumen

Contoh ini mengkonfigurasi tingkat zoom awal yang harus diterapkan saat PDF dibuka.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GoToAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) dengan sebuah [`XYZExplicitDestination`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Tetapkan tindakan sebagai tindakan buka dokumen dan simpan hasilnya.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan faktor zoom saat dokumen dibuka

Gunakan contoh ini untuk memeriksa apakah PDF sudah menentukan tingkat zoom eksplisit untuk aksi bukaannya.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Periksa apakah aksi buka adalah a [`GoToAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) dengan sebuah [`XYZExplicitDestination`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Keluarkan nilai zoom yang dikonfigurasi atau laporkan bahwa tidak ada zoom yang diatur.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
