---
title: Menambahkan latar belakang pada PDF dengan Java
linktitle: Menambahkan latar belakang
type: docs
weight: 20
url: /id/java/add-backgrounds/
description: Tambahkan latar belakang gambar dan warna solid ke halaman PDF dalam Java dan sesuaikan opasitas gambar.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan latar belakang pada PDF dengan Java
Abstract: Tambahkan latar belakang gambar dan warna solid ke halaman PDF dalam Java dan sesuaikan opasitas gambar.
---
Artefak latar belakang memungkinkan Anda menempatkan elemen visual non‑konten di belakang konten utama halaman tanpa mengubah teks logis dokumen.

## Menambahkan gambar latar belakang ke PDF

Gunakan contoh ini ketika halaman harus menampilkan gambar sebagai artefak latar belakang.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buka aliran gambar.
1. Buat objek [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) dan tetapkan aliran gambar.
1. Tambahkan artefak ke halaman target.
1. Simpan PDF keluaran.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan gambar latar belakang dengan opasitas

Contoh ini menempatkan gambar latar belakang semi-transparan di belakang konten halaman.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buka aliran gambar.
1. Buat objek [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), tetapkan gambar, dan atur opasitas.
1. Tambahkan artefak ke halaman.
1. Simpan dokumen.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan warna latar belakang ke PDF

Gunakan contoh ini ketika halaman harus menggunakan warna latar belakang padat alih-alih gambar.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat objek [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) dan tetapkan warna latar belakang.
1. Tambahkan artefak ke halaman.
1. Simpan file keluaran.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Topik terkait

- [Menghapus latar belakang](/pdf/id/java/remove-backgrounds/)
- [Artefak PDF](/pdf/id/java/artifacts/)
