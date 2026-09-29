---
title: Tambahkan Watermarks ke PDF dalam Java
linktitle: Menambahkan Watermark
type: docs
weight: 30
url: /id/java/add-watermarks/
description: Pelajari cara menambahkan, mengekstrak, dan menghapus artefak watermark dalam file PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan watermark ke PDF dengan Java
Abstract: Artikel ini menjelaskan cara menambahkan, memeriksa, dan menghapus watermark artifacts dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan watermark teks dengan pengaturan perataan, rotasi, opasitas, dan latar belakang, memeriksa watermark artifacts pada sebuah halaman, dan menghapusnya.
---
Watermark artifacts memungkinkan Anda menempatkan penanda visual yang persisten pada sebuah halaman tanpa mencampurkannya ke dalam konten utama dokumen.

## Ekstrak watermark artifacts dari PDF

Gunakan contoh ini ketika Anda perlu memeriksa watermark artifacts yang ada dan membaca teks atau posisinya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasi melalui koleksi artefak halaman target.
1. Filter artefak paginasi watermark dan cetak teks serta persegi panjangnya.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Tambahkan artefak watermark

Gunakan contoh ini ketika halaman harus menampilkan watermark teks terpusat dengan rotasi khusus, opasitas, dan penempatan latar belakang.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) dan konfigurasikan status teks serta pengaturan penempatannya.
1. Tambahkan watermark ke halaman dan simpan file output.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## Hapus artefak watermark

Gunakan pendekatan ini ketika artefak watermark yang ada harus dihapus dari halaman.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasi melalui koleksi artefak halaman dalam urutan terbalik.
1. Hapus artefak paginasi yang subtipe-nya adalah watermark, kemudian simpan dokumen.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
