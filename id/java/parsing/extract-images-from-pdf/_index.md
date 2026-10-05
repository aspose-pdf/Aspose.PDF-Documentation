---
title: "Mengekstrak gambar dari PDF menggunakan Java"
linktitle: "Mengekstrak gambar dari PDF"
type: docs
weight: 20
url: /id/java/extract-images-from-the-pdf-file/
description: Pelajari cara mengekstrak gambar yang disematkan dari file PDF dengan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak gambar dari PDF via Java"
Abstract: Artikel ini menjelaskan cara mengekstrak gambar yang disematkan dari dokumen PDF dengan Aspose.PDF for Java. Artikel ini menunjukkan cara membuka PDF sumber, mengakses gambar dari koleksi sumber daya halaman, dan menyimpan XImage yang diekstrak ke file eksternal.
---
Ekstrak gambar dari halaman PDF ketika Anda perlu menggunakan kembali grafik yang disematkan, memeriksa aset dokumen, atau mengekspor gambar untuk proses selanjutnya.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka aliran output untuk file gambar yang diekstrak.
1. Dapatkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dari dokumen dan mengaksesnya `Resources.Images` koleksi.
1. Ambil yang diperlukan objek [`XImage`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) dari koleksi gambar tersebut berdasarkan indeks.
1. Panggil `image.save(outputImage)` untuk menulis byte gambar yang diekstrak ke aliran target.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
