---
title: "Menghapus gambar dari file PDF menggunakan Java"
linktitle: "Menghapus gambar"
type: docs
weight: 20
url: /id/java/delete-images-from-pdf-file/
description: Pelajari cara menghapus gambar tersemat dari file PDF dengan Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menghapus gambar tersemat dari file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara menghapus gambar dari dokumen PDF menggunakan Aspose.PDF for Java. Contoh tersebut menghapus sumber gambar dari halaman pertama berdasarkan indeksnya dalam koleksi gambar halaman dan kemudian menyimpan dokumen yang telah dimodifikasi.
---
Gunakan koleksi sumber gambar halaman ketika Anda perlu menghapus gambar tersemat dari halaman PDF.

## Menghapus gambar tersemat berdasarkan indeks

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses sumber daya gambar pada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Hapus gambar target dari koleksi sumber daya halaman berdasarkan indeksnya.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
