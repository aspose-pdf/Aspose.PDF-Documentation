---
title: Multimedia
linktitle: Multimedia
type: docs
weight: 70
url: /id/java/pdfcontenteditor-multimedia/
description: "Pelajari cakupan multimedia terkini yang tersedia di fasad Java PdfContentEditor dalam Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Alur kerja anotasi multimedia di Java dengan PdfContentEditor
Abstract: Bagian ini mencakup alur kerja terkait multimedia yang saat ini didukung oleh set contoh Java PdfContentEditor. Repositori mencakup contoh anotasi film langsung, sementara topik suara yang tidak didukung dipertahankan sebagai catatan lingkup eksplisit.
---
Java saat ini kelas `PdfContentEditorExamples` secara langsung mendukung `addMovieAnnotation(...)`.

## Menambahkan anotasi film

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Panggil `createMovie(...)` dengan persegi panjang anotasi, jalur file film, dan nomor halaman.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
