---
title: "Anotasi keamanan menggunakan Java"
linktitle: "Anotasi keamanan"
type: docs
weight: 75
url: /id/java/security-annotations/
description: Pelajari cara menandai teks untuk redaksi, menerapkan anotasi redaksi, dan menghapus area halaman yang dipilih dalam file PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus konten PDF sensitif dalam Java dengan anotasi keamanan"
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi redaksi dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penandaan teks yang cocok dengan anotasi redaksi, penerapan redaksi secara permanen, serta melakukan redaksi pada area yang dipilih berdasarkan persegi panjang penempatan gambar yang terdeteksi.
---
Alur kerja anotasi keamanan dalam bagian ini fokus pada menyiapkan dan menerapkan redaksi pada konten PDF yang sensitif.

## Menandai teks dengan anotasi redaksi

Gunakan contoh ini ketika teks yang cocok harus ditutupi oleh anotasi redaksi sebelum redaksi diterapkan secara permanen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cari teks target dan buat sebuah [`RedactionAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) untuk setiap kecocokan.
1. Konfigurasikan tampilan redaksi dan simpan dokumen.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## Menerapkan redaksi yang ada

Contoh ini secara permanen menerapkan anotasi redaksi yang sudah ada di halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi tipe [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Panggil `redact()` pada setiap anotasi yang dikumpulkan dan simpan file yang telah diperbarui.

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## Menyensor area halaman yang dipilih

Gunakan pendekatan ini ketika konten target diidentifikasi berdasarkan posisi daripada dengan mencocokkan teks.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deteksi persegi panjang target pada halaman, misalnya dari penempatan gambar.
1. Buat sebuah [`RedactionAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) untuk area itu dan simpan dokumen.

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## Topik anotasi terkait

- [Anotasi interaktif](/pdf/id/java/interactive-annotations/)
- [Anotasi markup](/pdf/id/java/markup-annotations/)
- [Anotasi bentuk](/pdf/id/java/shape-annotations/)
- [Anotasi teks](/pdf/id/java/text-based-annotations/)
- [Anotasi watermark](/pdf/id/java/watermark-annotations/)
- [Anotasi Impor dan ekspor](/pdf/id/java/import-export-annotations/)
