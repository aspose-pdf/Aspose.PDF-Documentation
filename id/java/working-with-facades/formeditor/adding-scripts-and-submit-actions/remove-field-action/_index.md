---
title: "Menghapus aksi Field"
linktitle: "Menghapus aksi Field"
type: docs
weight: 50
url: /id/java/remove-field-action/
description: "Pelajari cara menghapus aksi bidang dari bidang formulir PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menghapus aksi bidang formulir PDF dalam Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, menghapus aksi yang terkait dengan bidang tertentu, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java."
---
## Menghapus aksi bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Panggil `removeFieldAction(...)` untuk bidang target.
3. Simpan dokumen yang diperbarui.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
