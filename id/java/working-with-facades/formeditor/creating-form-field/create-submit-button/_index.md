---
title: Buat Tombol Kirim
linktitle: Buat Tombol Kirim
type: docs
weight: 60
url: /id/java/create-submit-button/
description: Pelajari cara menambahkan tombol kirim ke dokumen PDF dalam Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Buat tombol kirim PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menambahkan bidang tombol kirim dengan URL target, dan menyimpan dokumen yang dimodifikasi menggunakan facade FormEditor di Aspose.PDF for Java.
---
Gunakan `FormEditorExamples.createSubmitButton(...)` untuk membuat tombol yang mengirim data formulir.

## Buat tombol kirim

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggil `addSubmitBtn(...)` dengan nama tombol, halaman, label, URL target, dan persegi panjang.
3. Simpan dokumen yang diperbarui.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
