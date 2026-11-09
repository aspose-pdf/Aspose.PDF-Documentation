---
title: Mengekstrak detail tanda air pada PDF dengan Java
linktitle: Mengekstrak detail tanda air
type: docs
weight: 50
url: /id/java/extract-watermarks/
description: Baca teks dan persegi panjang pembatas dari artefak tanda air pada halaman pertama PDF dalam Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengekstrak detail tanda air pada PDF dengan Java
Abstract: Baca teks dan persegi panjang pembatas dari artefak tanda air pada halaman pertama PDF dalam Java.
---
Baca teks dan persegi panjang pembatas dari artefak tanda air pada halaman pertama PDF dalam Java.

## Mengekstrak detail tanda air dari PDF

Gunakan contoh ini ketika Anda perlu memeriksa artefak tanda air yang ada dan membaca teks atau posisinya.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Telusuri koleksi artefak halaman target.
1. Saring artefak paginasi tanda air dan cetak teks serta persegi panjangnya.

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

## Topik terkait

- [Menambahkan tanda air](/pdf/id/java/add-watermarks/)
- [Menghapus tanda air](/pdf/id/java/remove-watermarks/)
- [Artefak PDF](/pdf/id/java/artifacts/)
