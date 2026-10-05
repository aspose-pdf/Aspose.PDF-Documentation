---
title: "Mengatur skrip Field"
linktitle: "Mengatur skrip Field"
type: docs
weight: 20
url: /id/java/set-field-script/
description: Pelajari cara menetapkan atau memperbarui aksi JavaScript pada bidang formulir PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengatur aksi JavaScript pada bidang formulir PDF dalam Java"
Abstract: Artikel ini menunjukkan cara mengaitkan PDF yang ada, menambahkan skrip awal, menggantinya dengan skrip yang diperbarui, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java.
---
## Mengatur skrip bidang

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Tambahkan aksi JavaScript awal ke bidang.
3. Ganti dengan teks skrip yang diperbarui.
4. Simpan dokumen yang diperbarui.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
