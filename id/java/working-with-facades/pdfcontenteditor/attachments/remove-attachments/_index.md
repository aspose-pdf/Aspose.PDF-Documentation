---
title: Hapus Lampiran
linktitle: Hapus Lampiran
type: docs
weight: 50
url: /id/java/remove-attachments/
description: Pelajari cara menghapus semua lampiran dokumen dari PDF di Java menggunakan facade PdfContentEditor dalam Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Hapus semua lampiran PDF di Java
Abstract: Artikel ini menunjukkan cara mengikat PDF, menghapus semua lampiran dokumen, dan menyimpan file yang diperbarui menggunakan facade PdfContentEditor di Aspose.PDF for Java.
---
## Hapus semua lampiran

1. Ikat PDF sumber ke `PdfContentEditor` fasad.
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
