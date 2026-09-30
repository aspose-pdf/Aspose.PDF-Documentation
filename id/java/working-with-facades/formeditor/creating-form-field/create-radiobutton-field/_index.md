---
title: "Membuat Field RadioButton"
linktitle: "Membuat Field RadioButton"
type: docs
weight: 50
url: /id/java/create-radiobutton-field/
description: "Pelajari cara menambahkan bidang radio button ke dokumen PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membuat bidang radio button dalam PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, mengonfigurasi pengaturan tata letak radio button, membuat bidang radio button, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java."
---
Gunakan `FormEditorExamples.createRadioButtonField(...)` untuk membuat bidang tombol radio dengan opsi yang telah ditentukan.

## Membuat bidang radio button

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Konfigurasikan celah tombol radio, orientasi, dan ukuran item.
3. Definisikan item tombol radio.
4. Tambahkan bidang tombol radio dengan pilihan default dan persegi panjangnya.
5. Simpan dokumen yang diperbarui.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
