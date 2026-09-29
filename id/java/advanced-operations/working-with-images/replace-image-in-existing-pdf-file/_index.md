---
title: Ganti Gambar dalam File PDF yang Ada menggunakan Java
linktitle: Ganti Gambar
type: docs
weight: 70
url: /id/java/replace-image-in-existing-pdf-file/
description: Pelajari cara mengganti gambar yang disematkan dalam file PDF yang ada menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Ganti gambar dalam file PDF yang ada dengan Java
Abstract: Artikel ini menunjukkan cara mengganti gambar dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup mengganti gambar berdasarkan indeks sumber daya dan mengganti penempatan gambar pertama yang cocok yang ditemukan dengan ImagePlacementAbsorber.
---
Gunakan koleksi gambar halaman atau pencarian berbasis penempatan tergantung pada seberapa tepat Anda perlu menargetkan gambar.

## Ganti gambar berdasarkan indeks sumber daya

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses sumber daya gambar pada target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Ganti sumber daya gambar target dengan file gambar baru.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Ganti gambar menggunakan `ImagePlacementAbsorber`

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) dan kunjungi target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Dapatkan target [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) dan ganti dengan aliran gambar baru.
1. Simpan PDF yang diperbarui [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
