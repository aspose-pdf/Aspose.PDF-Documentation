---
title: "Memindahkan Field"
linktitle: "Memindahkan Field"
type: docs
weight: 30
url: /id/java/move-field/
description: "Pelajari cara memindahkan bidang formulir yang ada dalam dokumen PDF di Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Memindahkan bidang formulir PDF ke posisi baru di Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, memindahkan bidang ke koordinat baru, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Memindahkan bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Panggil `moveField(...)` dengan nama bidang target dan koordinat persegi panjang baru.
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
