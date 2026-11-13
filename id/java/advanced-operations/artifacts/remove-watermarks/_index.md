---
title: Menghapus tanda air dari PDF dengan Java
linktitle: Menghapus tanda air
type: docs
weight: 90
url: /id/java/remove-watermarks/
description: Hapus artefak tanda air dari halaman pertama PDF di Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus tanda air dari PDF dengan Java
Abstract: Hapus artefak tanda air dari halaman pertama PDF di Java.
---
Hapus artefak tanda air dari halaman pertama PDF di Java.

## Menghapus artefak tanda air

Contoh ini hanya menghapus artefak bertipe `Pagination` dan bersubtipe `Watermark` dari halaman pertama. Tanda air yang terlihat dan tersimpan sebagai teks biasa pada halaman, gambar, atau anotasi tetap ada dalam PDF.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Telusuri koleksi artefak halaman secara terbalik.
1. Hapus artefak paginasi yang subtipenya adalah tanda air.
1. Simpan dokumen.

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

## Topik terkait

- [Menambahkan tanda air](/pdf/id/java/add-watermarks/)
- [Mengekstrak detail tanda air](/pdf/id/java/extract-watermarks/)
- [Artefak PDF](/pdf/id/java/artifacts/)
