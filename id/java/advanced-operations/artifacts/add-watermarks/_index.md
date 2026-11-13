---
title: Menambahkan tanda air pada PDF dengan Java
linktitle: Menambahkan tanda air
type: docs
weight: 30
url: /id/java/add-watermarks/
description: Tambahkan artefak tanda air teks bergaya ke halaman PDF dalam Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan tanda air pada PDF dengan Java
Abstract: Tambahkan artefak tanda air teks bergaya ke halaman PDF dalam Java.
---
Artefak tanda air memungkinkan Anda menempatkan penanda visual yang persisten pada halaman tanpa mencampurnya ke dalam konten dokumen utama.

## Menambahkan artefak tanda air

Gunakan contoh ini ketika halaman harus menampilkan tanda air teks yang terpusat dengan rotasi khusus, opasitas, dan penempatan latar belakang.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat objek [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) dan konfigurasikan keadaan teks serta pengaturan penempatannya.
1. Tambahkan tanda air ke halaman.
1. Simpan file keluaran.

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

## Topik terkait

- [Mengekstrak detail tanda air](/pdf/id/java/extract-watermarks/)
- [Menghapus tanda air](/pdf/id/java/remove-watermarks/)
- [Artefak PDF](/pdf/id/java/artifacts/)
