---
title: "Menambahkan latar belakang PDF di Java"
linktitle: Menambahkan latar belakang
type: docs
weight: 20
url: /id/java/add-backgrounds/
description: Pelajari cara menambahkan gambar latar belakang atau warna latar belakang ke halaman PDF di Java menggunakan `BackgroundArtifact` dengan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan latar belakang ke PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan atau menghapus latar belakang halaman PDF di Java menggunakan Aspose.PDF. Artikel ini mencakup menambahkan gambar latar belakang, menyesuaikan opasitas gambar, menerapkan warna latar belakang, dan menghapus artefak latar belakang dari sebuah halaman.
---
Artefak latar belakang memungkinkan Anda menempatkan elemen visual non-konten di belakang konten utama halaman tanpa mengubah teks logis dokumen.

## Menambahkan gambar latar belakang ke PDF

Gunakan contoh ini ketika halaman harus menampilkan gambar sebagai artefak latar belakang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan aliran masukan gambar.
1. Buat sebuah [`BackgroundArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) dan tetapkan aliran gambar.
1. Tambahkan artifact ke halaman target dan simpan PDF output.

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

Contoh ini menempatkan gambar latar belakang setengah transparan di belakang konten halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan aliran gambar.
1. Buat sebuah [`BackgroundArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), tetapkan gambar, dan atur opasitas.
1. Tambahkan artefak ke halaman dan simpan dokumen.

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

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`BackgroundArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) dan tetapkan warna latar belakang.
1. Tambahkan artefak ke halaman dan simpan berkas output.

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

## Menghapus artefak latar belakang

Gunakan pendekatan ini ketika artefak latar belakang yang ada harus dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan koleksi artefak halaman dalam urutan terbalik.
1. Hapus artefak yang tipe-nya pagination dan subtipe-nya background, kemudian simpan dokumen.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
