---
title: Buat File PDF dalam Java
linktitle: Buat Dokumen PDF
type: docs
weight: 10
url: /id/java/create-pdf-document/
description: Pelajari cara membuat file PDF dan membangun PDF yang dapat dicari dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat file PDF dan dokumen PDF yang dapat dicari dengan Java
Abstract: Artikel ini menunjukkan cara membuat dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup pembuatan PDF baru dari awal dan mengonversi dokumen berbasis gambar menjadi PDF yang dapat dicari dengan menyediakan output HOCR dari mesin OCR eksternal.
---
Aspose.PDF for Java mendukung baik pembuatan dokumen sederhana maupun alur kerja PDF yang dapat dicari dengan bantuan OCR.

## Buat dokumen PDF baru

Gunakan pendekatan ini ketika Anda perlu membuat file PDF sederhana dari awal.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dan tambahkan ke halaman.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Buat PDF yang dapat dicari

{"translatedText":""} `createSearchablePdf` contoh penggunaan `Document.convert(...)` dengan a `CallBackGetHocr` implementasi. Callback menulis gambar sumber ke file sementara, memanggil Tesseract dengan `hocr` opsi, membaca markup HOCR yang dihasilkan, dan mengembalikannya ke Aspose.PDF.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat `CallBackGetHocr` panggilan balik dan mengonversi dokumen sumber menjadi konten PDF yang dapat dicari.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## Dapatkan pengaturan jendela dokumen

Gunakan contoh ini untuk memeriksa preferensi penampil saat ini yang disimpan dalam dokumen PDF yang ada.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Atur preferensi jendela dokumen

Contoh ini memperbarui cara PDF harus ditampilkan ketika dibuka di penampil yang kompatibel.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Atur preferensi jendela, tata letak, dan mode halaman yang diperlukan.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Sematkan font dalam PDF yang ada

Gunakan pendekatan ini ketika sebuah dokumen harus membawa font yang diperlukan untuk rendering yang lebih andal pada sistem lain.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Aktifkan penyematan font standar dan iterasi melalui font yang digunakan oleh masing-masing [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Tandai semua yang tidak tertanam [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objek untuk disematkan.
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

## Sematkan font saat membuat PDF baru

Contoh ini membuat PDF baru dan menetapkan font yang disematkan ke konten teks sejak awal.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Buat yang diperlukan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), dan [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Menyelesaikan target [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) dari repositori dan tandai sebagai tersemat.
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

## Tetapkan font default untuk output PDF

Gunakan pola ini ketika dokumen yang disimpan harus kembali ke font tertentu selama pembuatan output.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) dan tetapkan nama font default.
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

## Dapatkan semua font yang digunakan dalam PDF

Contoh ini menampilkan semua font yang terdeteksi dalam dokumen sehingga Anda dapat memeriksa penggunaan font sebelum mengekspor atau memperbarui file.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerasikan font yang dikembalikan oleh utilitas font dokumen.
1. Keluarkan nama masing-masing yang terdeteksi [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Meningkatkan penyematan font dengan melakukan subset font

Gunakan pendekatan ini ketika Anda ingin mengurangi beban font sambil mempertahankan data font yang disematkan tetap selaras dengan penggunaan dokumen.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Jalankan subsetting font melalui utilitas font dokumen dengan yang diperlukan [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) nilai.
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

## Atur faktor zoom saat membuka dokumen

Contoh ini mengonfigurasi tingkat zoom awal yang harus diterapkan saat PDF dibuka.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) dengan sebuah [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Tetapkan tindakan sebagai tindakan pembukaan dokumen dan simpan hasilnya.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Dapatkan faktor zoom saat dokumen dibuka

Gunakan contoh ini untuk memeriksa apakah PDF sudah mendefinisikan tingkat zoom eksplisit untuk aksi buka-nya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Periksa apakah aksi buka adalah [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) dengan sebuah [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Keluarkan nilai zoom yang dikonfigurasi atau laporkan bahwa tidak ada zoom yang disetel.

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
