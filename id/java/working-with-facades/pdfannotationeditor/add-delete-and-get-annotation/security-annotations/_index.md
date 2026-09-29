---
title: Anotasi Keamanan menggunakan Java
linktitle: Anotasi Keamanan
type: docs
weight: 60
url: /id/java/pdfannotationeditor-class/security-annotations/
description: Pelajari cara menandai teks untuk redaksi, menerapkan anotasi redaksi, dan meredaksi area halaman yang dipilih dalam file PDF menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Redaksi konten PDF sensitif di Java dengan anotasi keamanan
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi redaksi dalam dokumen PDF menggunakan Java. Artikel ini mencakup penandaan teks yang cocok dengan anotasi redaksi, penerapan redaksi secara permanen, dan meredaksi area yang dipilih berdasarkan persegi panjang penempatan gambar yang terdeteksi.
---
## Tandai teks untuk redaksi

1. Muat PDF dan cari semua halaman untuk teks yang harus disamarkan.
2. Buat sebuah `RedactionAnnotation` untuk setiap fragmen teks yang cocok dan mengonfigurasi penampilannya.
3. Tambahkan anotasi penyamaran ke halaman mereka dan simpan dokumen.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
