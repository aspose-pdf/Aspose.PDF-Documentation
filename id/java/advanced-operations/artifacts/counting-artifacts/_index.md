---
title: Hitung Artefak PDF dalam Java
linktitle: Menghitung Artefak
type: docs
weight: 40
url: /id/java/counting-artifacts/
description: Pelajari cara memeriksa dan menghitung artefak paginasi dalam dokumen PDF menggunakan Java dengan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghitung Artefak dalam PDF menggunakan Java
Abstract: Artikel ini menjelaskan cara memeriksa dan menghitung artefak paginasi dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini menunjukkan cara mengiterasi artefak halaman dan menghitung subtipe watermark, background, header, dan footer.
---
## Hitung artefak paginasi pada halaman

Gunakan contoh ini ketika Anda membutuhkan hitungan cepat dari subtipe artefak paginasi utama pada sebuah halaman.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Baca [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) koleksi dari target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Iterasi melalui halaman [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) koleksi dan hitung setiap subtipe paginasi yang perlu Anda laporkan.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
