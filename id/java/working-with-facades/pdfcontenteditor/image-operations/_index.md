---
title: "Operasi gambar"
linktitle: "Operasi gambar"
type: docs
weight: 50
url: /id/java/pdfcontenteditor-image-operations/
description: Pelajari cakupan operasi gambar Java saat ini yang tersedia di fasad PdfContentEditor pada Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Alur kerja pengeditan gambar di Java dengan PdfContentEditor
Abstract: Bagian ini mencakup alur kerja terkait gambar yang saat ini didukung oleh set contoh Java PdfContentEditor. Repositori menyertakan contoh langsung untuk mengganti gambar, sementara topik penghapusan gambar yang tidak didukung dipertahankan sebagai catatan lingkup eksplisit.
---
Java saat ini kelas `PdfContentEditorExamples` secara langsung mendukung `replaceImage(...)`.

## Mengganti gambar

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Panggil `replaceImage(...)` dengan nomor halaman, indeks gambar, dan jalur gambar pengganti.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
