---
title: Anotasi Berbasis Teks menggunakan Java
linktitle: Anotasi Teks
type: docs
weight: 10
url: /id/java/pdfannotationeditor-class/text-based-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi teks, teks bebas, dan anotasi coret pada dokumen PDF menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF teks di Java
Abstract: Artikel ini menjelaskan cara membuat, membaca, dan menghapus anotasi berbasis teks dalam dokumen PDF menggunakan Java. Ini mencakup anotasi teks, anotasi teks bebas, dan anotasi coret berdasarkan implementasi contoh Java.
---
## Tambahkan anotasi teks

1. Buka PDF input dan targetkan halaman tempat anotasi teks harus ditempatkan.
2. Buat `TextAnnotation`, tentukan segiannya, dan atur judulnya, subjeknya, bendera, dan warnanya.
3. Tambahkan anotasi ke halaman dan simpan dokumen yang diperbarui.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Tambahkan anotasi teks bebas

1. Muat PDF sumber dan pilih halaman target serta persegi panjang untuk catatan teks bebas.
2. Buat `FreeTextAnnotation`, inisialisasi penampilannya default, dan atur judul serta warna.
3. Tambahkan anotasi ke halaman dan simpan hasilnya.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
