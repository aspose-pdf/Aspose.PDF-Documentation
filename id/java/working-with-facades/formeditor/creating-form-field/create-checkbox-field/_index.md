---
title: "Membuat Field CheckBox"
linktitle: "Membuat Field CheckBox"
type: docs
weight: 20
url: /id/java/create-checkbox-field/
description: "Pelajari cara menambahkan bidang form kotak centang ke dokumen PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membuat bidang kotak centang dalam PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, menambahkan bidang kotak centang pada posisi yang ditentukan, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java."
---
Gunakan `FormEditorExamples.createCheckBoxField(...)` untuk menambahkan bidang kotak centang ke formulir PDF.

## Membuat bidang kotak centang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Tambahkan bidang kotak centang dengan `FieldType.CheckBox`, nama bidang, keterangan, halaman, dan persegi panjang.
3. Simpan dokumen yang diperbarui.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
