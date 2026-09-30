---
title: "Mengganti teks dengan status"
linktitle: "Mengganti teks dengan status"
type: docs
weight: 20
url: /id/java/replace-text-with-state/
description: "Pelajari cara mengganti teks dengan format khusus di Java menggunakan fasad `PdfContentEditor` dalam Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengganti teks PDF dengan format khusus di Java"
Abstract: "Artikel ini menunjukkan cara mengaitkan PDF, mengkonfigurasi TextState khusus, mengganti semua kemunculan teks yang cocok, dan menyimpan dokumen yang diperbarui menggunakan fasad `PdfContentEditor` dalam Aspose.PDF for Java."
---
## Mengganti teks dengan TextState khusus

1. Hubungkan PDF sumber ke fasad `PdfContentEditor`.
2. Buat dan konfigurasikan sebuah `TextState` dengan warna dan ukuran font yang diperlukan.
3. Atur ruang lingkup replace-text ke `ReplaceAll`.
4. Panggil `replaceText(...)` dengan teks pencarian, teks pengganti, dan dikonfigurasi `TextState`.
5. Simpan dokumen PDF yang telah diperbarui.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
