---
title: Meningkatkan Ekstraksi Teks dari PDF Multi-Kolom
linktitle: Ekstraksi Teks dari PDF Multi-Kolom
type: docs
weight: 30
url: /id/java/text-extraction-from-multi-column-pdf/
description: Pelajari teknik untuk meningkatkan ekstraksi teks dari tata letak PDF multi-kolom dengan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Tata letak multi-kolom sering memerlukan pemrosesan tambahan untuk meningkatkan urutan baca dan kualitas ekstraksi.

## Ekstrak teks setelah mengurangi ukuran Font

Teknik ini memperbarui ukuran Font fragmen teks, menyimpan dokumen yang disesuaikan ke memori, dan kemudian mengekstrak teks dari hasil yang telah diubah.

1. Buka PDF sumber dalam sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Buat sebuah [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) dan kunjungi semua halaman dokumen untuk mengumpulkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objek.
1. Iterasi melalui fragmen dan kurangi ukuran font masing-masing dengan rasio yang diminta sehingga tata letak kolom padat dapat dinormalisasi sebelum ekstraksi.
1. Simpan yang disesuaikan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ke aliran byte dalam memori.
1. Buka kembali kedua [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dari buffer memori itu.
1. Buat sebuah [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), kunjungi semua halaman dokumen yang telah diubah, dan tulis teks yang diekstraksi ke file output.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## Ekstrak teks dengan faktor skala

Gunakan `TextExtractionOptions` dalam mode pemformatan murni dan sesuaikan faktor skala untuk tata letak yang banyak kolom.

1. Buka PDF sumber dalam sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Buat sebuah [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) untuk ekstraksi seluruh dokumen.
1. Buat [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) dalam mode pemformatan murni sehingga perilaku ekstraksi sensitif tata letak digunakan.
1. Setel faktor skala dan terapkan opsi ekstraksi ke absorber sebelum mengunjungi halaman.
1. Kunjungi semua halaman dokumen dan tulis teks yang diekstrak ke file output.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
