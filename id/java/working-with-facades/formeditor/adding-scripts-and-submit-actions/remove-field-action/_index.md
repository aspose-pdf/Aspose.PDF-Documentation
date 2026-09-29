---
title: Hapus Aksi Field
linktitle: Hapus Aksi Field
type: docs
weight: 50
url: /id/java/remove-field-action/
description: Pelajari cara menghapus aksi field dari field formulir PDF dalam Java menggunakan fasad FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Hapus aksi field formulir PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengikat PDF yang ada, menghapus aksi yang terkait dengan field tertentu, dan menyimpan dokumen yang diperbarui menggunakan fasad FormEditor di Aspose.PDF for Java.
---
## Hapus aksi field

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggilan `removeFieldAction(...)` untuk bidang target.
3. Simpan dokumen yang diperbarui.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
