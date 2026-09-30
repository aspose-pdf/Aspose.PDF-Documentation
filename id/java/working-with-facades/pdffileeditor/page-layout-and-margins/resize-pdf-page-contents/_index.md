---
title: "Mengubah ukuran konten halaman PDF"
linktitle: "Mengubah ukuran konten halaman PDF"
type: docs
weight: 30
url: /id/java/resize-pdf-page-contents/
description: Ubah ukuran konten pada halaman PDF yang dipilih dalam Java dengan antarmuka PdfFileEditor.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengubah ukuran konten halaman yang ada dalam dokumen PDF dengan Java"
Abstract: Pelajari cara mengubah ukuran konten halaman dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk menargetkan halaman tertentu, menerapkan lebar dan tinggi konten baru, dan menghentikan alur kerja jika operasi pengubahan ukuran gagal.
---
## Mengubah ukuran konten halaman PDF

Contoh Java mengubah ukuran area konten pada halaman 1 dan 3 serta memeriksa nilai boolean yang dikembalikan.

### Langkah

1. Buat `PdfFileEditor` contoh.
2. Pilih halaman yang kontennya harus diubah ukurannya.
3. Panggil `resizeContents` dengan lebar dan tinggi target.
4. Periksa nilai kembali dan tangani kegagalan sebelum melanjutkan.
5. Simpan dokumen yang telah diperbarui.

### Contoh Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
