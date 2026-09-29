---
title: Atur Batas Field
linktitle: Atur Batas Field
type: docs
weight: 50
url: /id/java/set-field-limit/
description: Pelajari cara mengatur batas karakter maksimum untuk field formulir PDF di Java menggunakan façade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Atur batas karakter untuk field formulir PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, mengatur batas karakter maksimum sebuah field, dan menyimpan dokumen yang telah diperbarui menggunakan façade FormEditor di Aspose.PDF for Java.
---
## Atur batas karakter field

1. Mengikat PDF sumber ke `FormEditor` fasad.
2. Panggil `setFieldLimit(...)` untuk bidang target dan jumlah karakter maksimum.
3. Simpan dokumen yang telah diperbarui.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
