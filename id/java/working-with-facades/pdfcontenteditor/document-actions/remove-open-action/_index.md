---
title: Hapus Aksi Buka
linktitle: Hapus Aksi Buka
type: docs
weight: 20
url: /id/java/remove-open-action/
description: Pelajari cara menghapus aksi buka dokumen dari PDF di Java menggunakan fasad PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Hapus aksi buka dokumen PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF, menghapus aksi buka dokumen, dan menyimpan dokumen yang diperbarui menggunakan fasad PdfContentEditor di Aspose.PDF for Java.
---
## Hapus aksi buka dokumen

1. Ikat PDF sumber ke `PdfContentEditor` fasad.
2. Panggil `removeDocumentOpenAction()`.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
