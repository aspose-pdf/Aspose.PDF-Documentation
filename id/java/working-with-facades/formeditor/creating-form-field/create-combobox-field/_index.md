---
title: "Membuat bidang ComboBox"
linktitle: "Membuat bidang ComboBox"
type: docs
weight: 30
url: /id/java/create-combobox-field/
description: "Pelajari cara menambahkan bidang combo box ke dokumen PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membuat bidang combo box dalam PDF dengan Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF yang ada, menambahkan bidang combo box, mengisinya dengan item, dan menyimpan dokumen yang dimodifikasi menggunakan fasad FormEditor di Aspose.PDF for Java."
---
Gunakan `FormEditorExamples.createComboBoxField(...)` untuk membuat kotak kombo dan menambahkan item yang dapat dipilih.

## Membuat bidang combo box

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Tambahkan bidang combo box dengan nilai default dan persegi targetnya.
3. Tambahkan item combo box yang dapat dipilih.
4. Simpan dokumen yang telah diperbarui.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
