---
title: "Anotasi watermark menggunakan Java"
linktitle: "Anotasi watermark"
type: docs
weight: 70
url: /id/java/watermark-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi watermark dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Bekerja dengan anotasi watermark dalam file PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi watermark dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penambahan anotasi watermark teks dengan keadaan teks khusus dan opasitas, membaca area anotasi watermark yang ada, serta menghapus anotasi watermark.
---
Anotasi watermark memungkinkan Anda menempatkan konten overlay yang dapat digunakan kembali pada sebuah halaman sambil tetap mengelolanya melalui koleksi anotasi.

## Menambahkan anotasi watermark

Gunakan contoh ini ketika Anda membutuhkan anotasi watermark teks dengan pengaturan font khusus dan opasitas.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`WatermarkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) dan tambahkan ke halaman.
1. Konfigurasikan [`TextState`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), teks watermark, dan opasitas, lalu simpan dokumen.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi watermark

Contoh ini memindai koleksi anotasi dan mencetak persegi panjang setiap anotasi watermark.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi pada halaman target.
1. Filter anotasi berdasarkan [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` dan cetak persegi panjang mereka.

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## Menghapus anotasi watermark

Gunakan pendekatan ini ketika anotasi watermark yang ada harus dihapus dari dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi jenis [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Hapus anotasi yang terkumpul dan simpan file output.

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## Topik anotasi terkait

- [Anotasi interaktif](/pdf/id/java/interactive-annotations/)
- [Anotasi markup](/pdf/id/java/markup-annotations/)
- [Anotasi keamanan](/pdf/id/java/security-annotations/)
- [Anotasi bentuk](/pdf/id/java/shape-annotations/)
- [Anotasi teks](/pdf/id/java/text-based-annotations/)
- [Mengimpor dan mengekspor anotasi](/pdf/id/java/import-export-annotations/)
