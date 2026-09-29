---
title: Hapus Item Daftar
linktitle: Hapus Item Daftar
type: docs
weight: 20
url: /id/java/del-list-item/
description: Pelajari cara menghapus item dari bidang list dalam dokumen PDF di Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Hapus item list dari bidang formulir PDF di Java.
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menghapus item tertentu dari bidang list, dan menyimpan dokumen yang diperbarui menggunakan facade FormEditor di Aspose.PDF for Java.
---
## Hapus item dari bidang list.

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggil `delListItem(...)` untuk bidang target dan item yang akan dihapus.
3. Simpan dokumen yang diperbarui.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
