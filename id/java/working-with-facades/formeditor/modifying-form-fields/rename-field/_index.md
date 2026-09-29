---
title: Ubah Nama Field
linktitle: Ubah Nama Field
type: docs
weight: 50
url: /id/java/rename-field/
description: Pelajari cara mengganti nama field formulir yang ada dalam dokumen PDF di Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Ganti nama field formulir PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, mengganti nama field yang ditentukan, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java.
---
## Ganti nama field

1. Mengikat PDF sumber ke `FormEditor` fasad.
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
