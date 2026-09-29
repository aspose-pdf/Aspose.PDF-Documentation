---
title: Buat Field CheckBox
linktitle: Buat Field CheckBox
type: docs
weight: 20
url: /id/java/create-checkbox-field/
description: Pelajari cara menambahkan field form kotak centang ke dokumen PDF dalam Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Buat field kotak centang dalam PDF dengan Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menambahkan field kotak centang pada posisi yang ditentukan, dan menyimpan dokumen yang dimodifikasi menggunakan facade FormEditor di Aspose.PDF for Java.
---
Gunakan `FormEditorExamples.createCheckBoxField(...)` untuk menambahkan bidang kotak centang ke formulir PDF.

## Buat field kotak centang

1. Ikat PDF sumber ke `FormEditor` fasad.
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
