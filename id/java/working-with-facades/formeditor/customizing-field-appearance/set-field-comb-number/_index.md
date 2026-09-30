---
title: "Mengatur nomor comb Field"
linktitle: "Mengatur nomor comb Field"
type: docs
weight: 60
url: /id/java/set-field-comb-number/
description: "Pelajari cara mengatur nomor comb untuk bidang formulir PDF di Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengatur nomor comb untuk bidang formulir PDF di Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, mengatur nomor comb untuk sebuah bidang, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Mengatur nomor comb bidang

1. Sambungkan PDF sumber ke fasad `FormEditor`.
2. Panggil `setFieldCombNumber(...)` untuk bidang target dan nilai comb.
3. Simpan dokumen yang diperbarui.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
