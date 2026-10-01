---
title: "Mendapatkan preferensi penampil"
linktitle: "Mendapatkan preferensi penampil"
type: docs
weight: 10
url: /id/java/get-viewer-preferences/
description: Pelajari cara membaca preferensi penampil dokumen PDF dalam Java menggunakan fasad PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membaca preferensi penampil PDF dalam Java"
Abstract: Artikel ini menunjukkan cara mengikat PDF dan mencetak nilai preferensi penampil saat ini menggunakan fasad PdfContentEditor di Aspose.PDF for Java.
---
## Mendapatkan preferensi penampil saat ini

1. Ikat PDF sumber ke `PdfContentEditor` fasade.
2. Panggil `getViewerPreference()` untuk membaca nilai saat ini.
3. Periksa atau cetak flag preferensi yang dikembalikan.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
