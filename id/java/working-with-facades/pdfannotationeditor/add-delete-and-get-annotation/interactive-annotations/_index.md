---
title: Anotasi Interaktif menggunakan Java
linktitle: Anotasi Interaktif
type: docs
weight: 30
url: /id/java/pdfannotationeditor-class/interactive-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi tautan dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF interaktif di Java
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi tautan interaktif dalam file PDF menggunakan Java. Ini mencakup menemukan teks, membuat anotasi tautan di atas area teks yang cocok, membaca anotasi tautan yang ada, dan menghapusnya.
---
## Tambah anotasi tautan

1. Muat dokumen PDF sumber dan cari teks target pada halaman pertama.
2. Gunakan persegi panjang teks yang cocok untuk membuat sebuah `LinkAnnotation` dan tetapkan URI tujuan.
3. Tambahkan anotasi ke halaman dan simpan PDF yang diperbarui.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
