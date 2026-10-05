---
title: "Menghapus lampiran"
linktitle: "Menghapus lampiran"
type: docs
weight: 50
url: /id/java/remove-attachments/
description: "Pelajari cara menghapus semua lampiran dokumen dari PDF di Java menggunakan fasad PdfContentEditor dalam Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menghapus semua lampiran PDF di Java"
Abstract: "Artikel ini menunjukkan cara mengikat PDF, menghapus semua lampiran dokumen, dan menyimpan file yang diperbarui menggunakan fasad PdfContentEditor di Aspose.PDF for Java."
---
## Menghapus semua lampiran

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Panggil `deleteAttachments()` untuk menghapus setiap lampiran tersemat.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
