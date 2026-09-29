---
title: Ekstraksi Berbasis Wilayah menggunakan Java
linktitle: Ekstraksi Berbasis Wilayah
type: docs
weight: 20
url: /id/java/region-based-extraction/
description: Pelajari cara mengekstrak teks dari wilayah halaman tertentu atau memeriksa geometri paragraf dalam dokumen PDF dengan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Ekstrak teks dari wilayah halaman persegi panjang

Gunakan `TextSearchOptions` dengan `Rectangle` untuk membatasi ekstraksi ke area yang ditentukan pada halaman.

1. Buka PDF sumber dalam sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Buat sebuah [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) untuk mengumpulkan teks dari area halaman yang dipilih.
1. Buat [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) untuk target [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) dan aktifkan `setLimitToPageBounds(true)` sehingga ekstraksi tetap berada di dalam kotak halaman yang terlihat.
1. Terapkan opsi pencarian yang dikonfigurasi ke absorber dan kunjungi target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Tulis buffer teks yang diekstrak ke file output.

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## Ekstrak paragraf dengan informasi geometris

Gunakan `ParagraphAbsorber` untuk memeriksa persegi panjang bagian dan poligon paragraf bersama dengan teks yang diekstrak.

1. Buka PDF sumber dalam sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instansi.
1. Buat sebuah [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) dan kunjungi target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) untuk membangun informasi markup halaman.
1. Baca hasil markup halaman pertama dan iterasi melalui bagian serta paragrafnya.
1. Kumpulkan setiap persegi panjang bagian, poligon paragraf, dan teks paragraf yang direkonstruksi darinya. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) baris.
1. Bangun laporan keluaran dengan geometri dan detail teks yang diekstrak.
1. Tuliskan detail yang diekstrak ke file keluaran.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
