---
title: "Mengekstrak gambar dari file PDF menggunakan Java"
linktitle: "Mengekstrak gambar"
type: docs
weight: 30
url: /id/java/extract-images-from-pdf-file/
description: Pelajari cara mengekstrak gambar yang disematkan dari file PDF dalam Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengekstrak gambar dari file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara mengekstrak gambar dari dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup penyimpanan sumber gambar tertentu dari sebuah halaman dan mengekspor gambar yang berada di dalam wilayah persegi panjang yang dipilih.
---
Aspose.PDF for Java mendukung ekstraksi sumber gambar langsung dan penyaringan berbasis penempatan.

## Mengekstrak gambar tersemat berdasarkan indeks

Gunakan contoh ini ketika Anda perlu menyimpan sumber gambar tertentu dari halaman PDF

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [`XImage`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) target dari sumber daya halaman.
1. Simpan aliran gambar ke file output.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Mengekstrak gambar dari area halaman tertentu

Gunakan contoh ini ketika hanya gambar yang ditempatkan di dalam persegi panjang yang dipilih yang harus diekspor.

1. Tentukan [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) target dan buka PDF sumber.
1. Gunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) untuk memeriksa penempatan gambar pada halaman.
1. Simpan hanya gambar yang penempatannya cocok di dalam wilayah yang dipilih.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
