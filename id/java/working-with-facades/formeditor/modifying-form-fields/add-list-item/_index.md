---
title: Tambahkan Item Daftar
linktitle: Tambahkan Item Daftar
type: docs
weight: 10
url: /id/java/add-list-item/
description: Pelajari cara menambahkan item ke bidang daftar dalam dokumen PDF menggunakan Java dengan façade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Tambahkan item daftar ke bidang formulir PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengaitkan PDF yang ada, menambahkan item baru ke bidang daftar, dan menyimpan dokumen yang diperbarui menggunakan façade FormEditor di Aspose.PDF for Java.
---
## Tambahkan item ke bidang daftar

1. Mengikat PDF sumber ke `FormEditor` fasad.
2. Panggilan `addListItem(...)` untuk bidang target dan pasangan tampilan/nilai baru.
3. Simpan dokumen yang diperbarui.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
