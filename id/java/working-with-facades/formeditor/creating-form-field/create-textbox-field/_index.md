---
title: "Membuat bidang TextBox"
linktitle: "Membuat bidang TextBox"
type: docs
weight: 10
url: /id/java/create-textbox-field/
description: Pelajari cara menambahkan bidang kotak teks ke dokumen PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membuat bidang formulir teks dalam PDF dengan Java"
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menambahkan bidang teks dengan nilai default, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java.
---
Gunakan `FormEditorExamples.createTextBoxField(...)` untuk menambahkan bidang teks ke formulir PDF.

## Membuat bidang kotak teks

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Tambahkan setiap bidang teks dengan `FieldType.Text`, nama bidang, nilai default, nomor halaman, dan persegi panjang.
3. Simpan dokumen yang diperbarui.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
