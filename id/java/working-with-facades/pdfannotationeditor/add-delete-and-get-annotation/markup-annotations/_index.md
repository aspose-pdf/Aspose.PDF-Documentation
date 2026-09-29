---
title: Anotasi Markup menggunakan Java
linktitle: Anotasi Markup
type: docs
weight: 20
url: /id/java/pdfannotationeditor-class/markup-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi sorot, garis bawah, bergelombang, dan coret pada dokumen PDF menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi markup dalam file PDF menggunakan Java
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi markup teks dalam dokumen PDF menggunakan Java. Ini mencakup anotasi sorot, garis bawah, bergelombang, dan coret berdasarkan contoh Java di repositori.
---
## Tambahkan anotasi sorot, garis bawah, bergelombang, atau coret

1. Buka file PDF input dan pilih area halaman tempat anotasi markup harus muncul.
2. Buat jenis anotasi yang diperlukan dan konfigurasikan metadata atau properti visualnya.
3. Tambahkan anotasi ke koleksi halaman dan simpan dokumen.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
