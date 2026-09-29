---
title: Ganti Teks dalam PDF dengan Java
linktitle: Ganti Teks dalam PDF
type: docs
weight: 40
url: /id/java/replace-text-in-pdf/
description: Pelajari cara mengganti, menyusun ulang, dan menghapus teks dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Ganti, hapus, dan sesuaikan konten teks dalam PDF menggunakan Java
Abstract: Artikel ini menjelaskan alur kerja penggantian teks dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup penggantian teks di seluruh halaman, membatasi penggantian ke daerah yang dipilih, menyesuaikan tata letak penggantian, menggunakan pencocokan berbasis regex, mengganti Font, menghapus semua teks, dan menghapus teks tersembunyi.
---
Aspose.PDF for Java menyediakan fitur penggantian sederhana dan penggantian yang memperhatikan tata letak melalui `TextFragmentAbsorber` dan opsi penggantian.

## Ganti teks pada semua halaman

Gunakan contoh ini ketika frasa yang sama harus diganti di seluruh dokumen.

1. Buka dokumen PDF sumber.
1. Cari semua halaman untuk frasa target dengan `TextFragmentAbsorber`.
1. Ganti teks yang cocok dan simpan PDF yang diperbarui.

```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## Ganti teks pada wilayah halaman tertentu

Gunakan contoh ini ketika penggantian harus dibatasi pada persegi panjang yang dipilih pada satu halaman.

1. Buka dokumen PDF sumber.
1. Konfigurasi `TextSearchOptions` dengan batas halaman dan sebuah persegi panjang target.
1. Ganti teks yang cocok di dalam wilayah tersebut dan simpan dokumen.

```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## Ganti teks dan sesuaikan spasi di dalam persegi panjang yang dipindahkan

Gunakan contoh ini ketika teks pengganti harus tetap berada di halaman dengan spasi yang disesuaikan tetapi ukuran font harus tetap tidak berubah.

1. Buka PDF sumber dan kumpulkan fragmen teks dari halaman target.
1. Ubah persegi panjang pengganti dan pilih `AdjustSpaceWidth` perilaku.
1. Atur teks baru dan simpan dokumen.

```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Ganti teks di dalam persegi panjang paragraf yang lebih besar

Gunakan contoh ini ketika teks pengganti harus memperluas ke area halaman yang lebih besar.

1. Buka PDF sumber dan dapatkan fragmen teks pertama dari halaman target.
1. Bangun kotak pengganti yang lebih besar dari kotak media halaman.
1. Terapkan opsi penggantian dan simpan PDF.

```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Ganti teks dan skala font agar mengisi persegi panjang

Gunakan contoh ini ketika teks pengganti harus diperbesar untuk mengisi area target.

1. Buka PDF sumber dan akses fragmen teks target.
1. Definisikan persegi pengganti dan aktifkan `ScaleToFill` penyesuaian font.
1. Atur teks baru dan simpan dokumen yang diperbarui.

```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Ganti teks dan perkecil agar pas

Gunakan contoh ini ketika teks pengganti harus tetap berada di dalam persegi panjang teks asli.

1. Buka PDF sumber dan pilih fragmen target.
1. Gunakan kembali persegi panjang fragmen saat ini dan aktifkan `ShrinkToFit`.
1. Ganti teks dan simpan dokumen.

```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## Ganti teks dengan ekspresi reguler

Gunakan contoh ini ketika teks yang cocok harus ditemukan oleh pola regex dan diubah gaya selama penggantian.

1. Buka dokumen PDF sumber.
1. Cari halaman dengan regex-enabled `TextFragmentAbsorber`.
1. Ganti setiap kecocokan, perbarui gaya teksnya, dan simpan hasilnya.

```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## Ganti teks placeholder dan biarkan halaman mengatur ulang

Gunakan contoh ini ketika placeholder harus diganti dengan nilai nyata yang lebih panjang sambil mempertahankan tata letak halaman.

1. Buka PDF sumber dan cari teks placeholder.
1. Tetapkan teks pengganti dan perbarui pengaturan fontnya.
1. Simpan dokumen sehingga tata letaknya dihitung ulang.

```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## Ganti satu font dengan yang lain

Gunakan contoh ini ketika teks yang menggunakan font tertanam tertentu harus diganti dengan font lain.

1. Buka PDF sumber dan kumpulkan semua fragmen teks.
1. Periksa nama font setiap fragmen dan ganti font target.
1. Simpan PDF yang diperbarui.

```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Ganti font dan hapus sumber daya font yang tidak terpakai

Gunakan contoh ini ketika dokumen harus dibersihkan setelah penggantian font.

1. Buka PDF sumber dan konfigurasikan `TextEditOptions` untuk menghapus font yang tidak terpakai.
1. Serap fragmen teks dan tetapkan font pengganti.
1. Simpan dokumen yang dioptimalkan.

```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## Hapus semua teks dari dokumen

Gunakan contoh ini ketika semua konten teks harus dihapus dari setiap halaman.

1. Buka dokumen PDF sumber.
1. Buat sebuah `TextFragmentAbsorber` dan panggil `removeAllText(document)`.
1. Simpan PDF yang telah dibersihkan.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## Hapus semua teks dari satu halaman

Gunakan contoh ini ketika semua teks harus dihapus hanya dari halaman tertentu.

1. Buka dokumen PDF sumber.
1. Buat sebuah `TextFragmentAbsorber` dan hapus teks dari halaman target.
1. Simpan dokumen yang diperbarui.

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## Hapus teks dari persegi panjang yang dipilih

Gunakan contoh ini ketika teks harus dihapus hanya di dalam area halaman yang dipilih.

1. Buka dokumen PDF sumber.
1. Buat sebuah `TextFragmentAbsorber` dan tentukan persegi panjang yang akan dibersihkan.
1. Hapus teks dari wilayah itu dan simpan dokumen.

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## Hapus teks tersembunyi

Gunakan contoh ini ketika fragmen teks tak terlihat harus dihapus dari PDF.

1. Buka PDF sumber dan serap semua TextFragment.
1. Periksa setiap fragmen untuk keadaan teks tak terlihat.
1. Hapus teks tersembunyi dan simpan dokumen.

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
