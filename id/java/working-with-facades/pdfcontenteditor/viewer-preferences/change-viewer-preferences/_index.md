---
title: "Mengubah preferensi penampil"
linktitle: "Mengubah preferensi penampil"
type: docs
weight: 20
url: /id/java/change-viewer-preferences/
description: Pelajari cara mengubah preferensi penampil dokumen PDF di Java menggunakan fasad PdfContentEditor dalam Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengubah preferensi penampil PDF di Java"
Abstract: Artikel ini menunjukkan cara mengaitkan PDF, memodifikasi nilai preferensi penampil saat ini, dan menyimpan dokumen yang diperbarui menggunakan fasad PdfContentEditor dalam Aspose.PDF for Java.
---
## Mengubah preferensi penampil

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Baca nilai preferensi penampil saat ini.
3. Gabungkan dengan flag tambahan yang diinginkan dan kirimkan hasilnya ke `changeViewerPreference(...)`.
4. Simpan dokumen PDF yang diperbarui.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
