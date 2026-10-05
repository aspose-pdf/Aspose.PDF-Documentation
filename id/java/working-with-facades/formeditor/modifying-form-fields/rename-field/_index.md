---
title: "Mengubah nama Field"
linktitle: "Mengubah nama Field"
type: docs
weight: 50
url: /id/java/rename-field/
description: "Pelajari cara mengganti nama bidang formulir yang ada dalam dokumen PDF di Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengganti nama bidang formulir PDF di Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, mengganti nama bidang yang ditentukan, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Mengganti nama bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Panggil `renameField(...)` dengan nama bidang saat ini dan nama bidang baru.
3. Simpan dokumen yang telah diperbarui.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
