---
title: Hapus Field
linktitle: Hapus Field
type: docs
weight: 40
url: /id/java/remove-field/
description: Pelajari cara menghapus field form yang ada dari dokumen PDF di Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Hapus field form PDF di Java
Abstract: Artikel ini menunjukkan cara mengaitkan PDF yang ada, menghapus field yang ditentukan, dan menyimpan dokumen yang diperbarui menggunakan facade FormEditor di Aspose.PDF for Java.
---
## Hapus field

1. Ikat PDF sumber ke `FormEditor` fasad.
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
