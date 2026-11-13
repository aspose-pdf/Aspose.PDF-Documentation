---
title: Menghitung artefak paginasi pada PDF dengan Java
linktitle: Menghitung artefak paginasi
type: docs
weight: 40
url: /id/java/counting-artifacts/
description: Pelajari cara memeriksa dan menghitung artefak paginasi dalam dokumen PDF menggunakan Java dengan Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghitung artefak paginasi pada PDF dengan Java
Abstract: Artikel ini menjelaskan cara memeriksa dan menghitung artefak paginasi dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini menunjukkan cara mengulangi artefak halaman dan menghitung subtipe tanda air, background, header, dan footer.
---
## Menghitung artefak paginasi pada halaman

Gunakan contoh ini ketika Anda membutuhkan hitungan cepat subtipe artefak paginasi utama pada sebuah halaman.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Baca koleksi artefak [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) pada halaman tujuan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Telusuri koleksi artefak [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) pada halaman dan hitung jumlah artefak untuk setiap subtipe paginasi yang perlu dilaporkan.

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

## Topik terkait

- [Artefak PDF](/pdf/id/java/artifacts/)
- [Mengekstrak detail tanda air](/pdf/id/java/extract-watermarks/)
- [Menghapus latar belakang](/pdf/id/java/remove-backgrounds/)
- [Menghapus tanda air](/pdf/id/java/remove-watermarks/)
- [Menghapus penomoran Bates](/pdf/id/java/remove-bates-numbering/)
- [Menghapus header dan footer](/pdf/id/java/remove-headers-footers/)
