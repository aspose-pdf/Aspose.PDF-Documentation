---
title: "Menyalin Field dalam"
linktitle: "Menyalin Field dalam"
type: docs
weight: 70
url: /id/java/copy-inner-field/
description: "Pelajari cara menyalin bidang formulir ke posisi baru dalam dokumen PDF yang sama menggunakan Java dengan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menyalin bidang formulir PDF dalam dokumen yang sama menggunakan Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, menduplikasi bidang ke halaman dan posisi lain, serta menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Menyalin bidang di dalam PDF yang sama

1. Hubungkan PDF sumber ke fasad `FormEditor`.
2. Panggil `copyInnerField(...)` dengan nama bidang sumber, nama bidang baru, halaman, dan koordinat.
3. Simpan dokumen yang telah diperbarui.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
