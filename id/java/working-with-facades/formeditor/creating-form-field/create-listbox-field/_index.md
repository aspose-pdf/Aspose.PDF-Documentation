---
title: "Membuat bidang ListBox"
linktitle: "Membuat bidang ListBox"
type: docs
weight: 40
url: /id/java/create-listbox-field/
description: "Pelajari cara menambahkan bidang list box ke dokumen PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membuat bidang list box dalam PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, mendefinisikan item daftar, menambahkan bidang list box, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java."
---
Gunakan `FormEditorExamples.createListBoxField(...)` untuk membuat kotak daftar dengan item yang telah ditentukan.

## Membuat bidang list box

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Tentukan item daftar yang tersedia dengan `setItems(...)`.
3. Tambahkan bidang kotak daftar dengan nilai default dan persegi panjangnya.
4. Simpan dokumen yang diperbarui.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
