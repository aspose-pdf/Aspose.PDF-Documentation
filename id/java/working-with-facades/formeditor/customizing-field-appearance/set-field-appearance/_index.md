---
title: Atur Penampilan Bidang
linktitle: Atur Penampilan Bidang
type: docs
weight: 40
url: /id/java/set-field-appearance/
description: Pelajari cara mengubah flag penampilan visual dari bidang formulir PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Ubah flag penampilan bidang formulir PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menerapkan flag penampilan ke sebuah bidang, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java.
---
## Atur flag penampilan bidang

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggil `setFieldAppearance(...)` untuk bidang target dan bendera anotasi yang dipilih.
3. Simpan dokumen yang diperbarui.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
