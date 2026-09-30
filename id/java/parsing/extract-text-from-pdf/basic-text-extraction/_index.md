---
title: "Ekstraksi teks dasar menggunakan Java"
linktitle: "Ekstraksi teks dasar"
type: docs
weight: 10
url: /id/java/basic-text-extraction/
description: Pelajari cara mengekstrak teks dari dokumen PDF dalam Java dengan Aspose.PDF dari semua halaman, dari halaman tertentu, atau berdasarkan struktur paragraf.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Ekstraksi teks dasar adalah titik awal untuk membaca konten PDF dalam Java. Aspose.PDF menyediakan dua pendekatan umum:

- Gunakan `TextAbsorber` ketika Anda membutuhkan hasil teks biasa dari dokumen atau halaman.
- Gunakan `ParagraphAbsorber` ketika Anda perlu mempertahankan pengelompokan halaman, bagian, paragraf, baris, dan fragmen.

Halaman PDF tidak menyimpan teks seperti dokumen pengolah kata, sehingga urutan yang diekstrak bergantung pada aliran konten halaman dan tata letaknya. Untuk ekstraksi spesifik wilayah, detail geometri, tata letak multi‑kolom, anotasi, teks yang disorot, atau deteksi superskrip dan subskrip, gunakan artikel ekstraksi terkait dalam bagian ini.

## Mengekstrak teks dari semua halaman

Gunakan `TextAbsorber` untuk mengumpulkan aliran teks datar dari seluruh dokumen dan menuliskannya ke sebuah file. Ini adalah opsi paling sederhana ketika Anda hanya membutuhkan konten teks yang dapat dibaca dan tidak memerlukan batas paragraf atau koordinat.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) untuk mengumpulkan teks di seluruh dokumen.
1. Panggil `document.getPages().accept(textAbsorber)` sehingga setiap [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dikunjungi oleh penyerap.
1. Tuliskan buffer teks yang diekstrak ke file output.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Mengekstrak teks dari halaman tertentu

Terapkan absorber hanya pada halaman yang Anda butuhkan. Nomor halaman dalam `Document` koleksi halaman dimulai dari 1, jadi `get_Item(1)` membaca halaman pertama.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) untuk ekstraksi satu halaman.
1. Panggil `accept(textAbsorber)` pada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dipilih berdasarkan nomor halaman.
1. Tuliskan buffer teks yang diekstrak ke file output.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Mengekstrak teks berdasarkan struktur paragraf

Gunakan `ParagraphAbsorber` ketika Anda membutuhkan pengelompokan struktural alih-alih aliran teks polos tunggal. Ini mengembalikan markup halaman dengan bagian, paragraf, baris, dan objek `TextFragment`, yang berguna ketika output harus mempertahankan blok logis teks.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`ParagraphAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) dan kunjungi seluruh dokumen untuk membangun hasil markup halaman.
1. Iterasikan melalui penandaan halaman, bagian, paragraf, baris, dan objek [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) yang diungkapkan oleh absorber.
1. Bangun teks keluaran dengan penomoran halaman, bagian, dan paragraf yang eksplisit sehingga pengelompokan struktural dipertahankan.
1. Tuliskan teks paragraf yang diekstrak ke file output.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
