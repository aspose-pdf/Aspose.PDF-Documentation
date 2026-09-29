---
title: Cari dan Ekstrak Teks PDF dalam Java
linktitle: Cari dan Dapatkan Teks
type: docs
weight: 60
url: /id/java/search-and-get-text-from-pdf/
description: Pelajari cara mencari, memeriksa, dan mengekstrak teks dari dokumen PDF di Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cari teks PDF dan periksa fragmen yang diekstrak di Java
Abstract: Artikel ini menjelaskan cara mencari dan mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup TextAbsorber dan TextFragmentAbsorber, termasuk ekstraksi berbasis wilayah, pencarian spesifik halaman, pencocokan regex dan frasa, penyisipan hyperlink, inspeksi teks bergaya, dan penyorotan fragmen.
---
Aspose.PDF for Java mendukung ekstraksi teks mentah dan pencarian tingkat fragmen dengan koordinat, gaya, dan pencocokan regex.

## Ekstrak teks dari semua halaman dengan TextAbsorber

Gunakan contoh ini ketika Anda memerlukan teks yang diekstrak secara polos dari wilayah dokumen yang dipilih di semua halaman.

1. Buka dokumen PDF sumber.
1. Buat `TextExtractionOptions` dan berbasis wilayah `TextSearchOptions`.
1. Jalankan `TextAbsorber` pada semua halaman dan keluarkan teks yang diekstrak.

```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## Ekstrak teks dari satu halaman dengan TextAbsorber

Gunakan contoh ini ketika ekstraksi teks biasa harus dibatasi hanya satu halaman.

1. Buka dokumen PDF sumber.
1. Konfigurasikan ekstraksi teks dan opsi pencarian dengan wilayah target.
1. Jalankan `TextAbsorber` pada halaman yang dipilih dan keluarkan hasilnya.

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## Periksa semua fragmen teks dalam dokumen

Gunakan contoh ini ketika Anda membutuhkan konten teks bersamaan dengan metadata font, posisi, dan warna.

1. Buka dokumen PDF sumber.
1. Jalankan `TextFragmentAbsorber` di semua halaman.
1. Iterasi melalui fragmen dan keluarkan metadata mereka.

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## Cari satu frasa pada halaman tertentu

Gunakan contoh ini ketika kata target harus ditemukan hanya pada halaman yang dipilih.

1. Buka dokumen PDF sumber.
1. Buat `TextFragmentAbsorber` dengan frasa target.
1. Kunjungi halaman yang dipilih dan keluarkan posisi fragmen yang cocok.

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Lanjutkan pencarian berurutan di seluruh halaman

Gunakan contoh ini ketika Anda ingin menggunakan kembali satu absorber saat berpindah dari pencarian satu halaman ke halaman berikutnya.

1. Buka dokumen PDF sumber dan buat absorber yang dapat digunakan kembali.
1. Cari halaman pertama dan periksa hasilnya.
1. Lanjutkan pencarian halaman tambahan dan tinjau kecocokan yang diperbarui.

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## Cari frasa di dalam persegi panjang terpilih

Gunakan contoh ini ketika pencocokan frasa harus dibatasi pada suatu wilayah di satu halaman.

1. Buka dokumen PDF sumber.
1. Buat `TextFragmentAbsorber` dengan frasa target dan berbasis persegi panjang `TextSearchOptions`.
1. Kunjungi halaman dan keluarkan posisi fragmen yang cocok.

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Cari teks dengan ekspresi reguler

Gunakan contoh ini ketika pencocokan harus ditemukan dengan pola regex, bukan frasa tetap.

1. Buka dokumen PDF sumber.
1. Buat yang mendukung regex `TextFragmentAbsorber`.
1. Kunjungi halaman target dan keluarkan fragmen yang cocok.

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Cari daftar frasa berdasarkan pola regex

Gunakan contoh ini ketika beberapa frasa target harus ditemukan dalam satu kali proses.

1. Buka dokumen PDF sumber.
1. Buat sebuah array pola regex dan berikan ke `TextFragmentAbsorber`.
1. Kunjungi dokumen dan periksa hasil regex yang dikelompokkan.

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## Temukan teks dan ubah menjadi tautan

Gunakan contoh ini ketika kata yang cocok harus disorot dan diubah menjadi tautan yang dapat diklik.

1. Buka dokumen PDF sumber.
1. Cari kata target dengan pencarian regex diaktifkan.
1. Perbarui gaya teks, lampirkan tautan hiper, dan simpan PDF yang dimodifikasi.

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## Cari teks berdasarkan karakteristik gaya

Gunakan contoh ini ketika Anda perlu memeriksa fragmen berdasarkan pemformatan seperti tebal atau teks tak terlihat.

1. Buka dokumen PDF sumber.
1. Jalankan `TextFragmentAbsorber` pada halaman target.
1. Periksa setiap gaya fragmen dan keluarkan entri yang cocok.

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## Sorot hasil pencarian di pratinjau halaman yang dirender

Gunakan contoh ini ketika kecocokan teks harus dikorelasikan dengan gambar halaman yang dirender untuk pemeriksaan visual.

1. Buat perangkat PNG dengan resolusi yang diperlukan.
1. Cari setiap halaman dengan `TextFragmentAbsorber` dan render halaman ke aliran gambar.
1. Tuliskan gambar pratinjau halaman dan keluarkan koordinat fragmen untuk inspeksi.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
