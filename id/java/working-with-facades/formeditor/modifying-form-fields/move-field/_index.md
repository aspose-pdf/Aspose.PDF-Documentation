---
title: Pindahkan Field
linktitle: Pindahkan Field
type: docs
weight: 30
url: /id/java/move-field/
description: Pelajari cara memindahkan field formulir yang ada dalam dokumen PDF di Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Pindahkan field formulir PDF ke posisi baru di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, memindahkan field ke koordinat baru, dan menyimpan dokumen yang diperbarui menggunakan facade FormEditor di Aspose.PDF for Java.
---
## Pindahkan field

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggilan `moveField(...)` dengan nama bidang target dan koordinat persegi panjang baru.
3. Simpan dokumen yang diperbarui.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
