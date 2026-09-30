---
title: "Menghapus Field"
linktitle: "Menghapus Field"
type: docs
weight: 40
url: /id/java/remove-field/
description: "Pelajari cara menghapus bidang form yang ada dari dokumen PDF di Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menghapus bidang form PDF di Java"
Abstract: "Artikel ini menunjukkan cara mengaitkan PDF yang ada, menghapus bidang yang ditentukan, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Menghapus bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Panggil `removeField(...)` untuk nama bidang target.
3. Simpan dokumen yang diperbarui.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
