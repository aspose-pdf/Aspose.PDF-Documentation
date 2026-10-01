---
title: "Memotong halaman PDF dengan Java"
linktitle: "Memotong halaman PDF"
type: docs
weight: 70
url: /id/java/crop-pages/
description: Pelajari cara memotong halaman PDF dan menyesuaikan kotak crop, trim, bleed, dan media dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memotong halaman dan menyesuaikan kotak halaman dalam file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara memotong halaman PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penetapan persegi panjang crop baru ke kotak crop, trim, art, dan bleed, serta memotong halaman secara otomatis berdasarkan konten gambar yang terdeteksi.
---
Aspose.PDF for Java memungkinkan Anda memotong halaman baik dengan koordinat kotak eksplisit atau berdasarkan konten yang terdeteksi.

## Memangkas halaman dengan mengatur kotak halaman

Gunakan contoh ini ketika Anda perlu menerapkan area panggasan yang sama ke kotak halaman utama.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat panggasan baru [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Terapkan persegi panjang pada kotak halaman yang terkait dengan pemotongan dan simpan dokumen.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## Memotong halaman berdasarkan konten yang terdeteksi

Gunakan contoh ini ketika area pemotongan harus diambil dari gambar pertama yang terdeteksi pada halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Gunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) untuk mendeteksi penempatan gambar.
1. Atur kotak pemotongan ke persegi panjang gambar jika ditemukan, kemudian simpan dokumen.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
