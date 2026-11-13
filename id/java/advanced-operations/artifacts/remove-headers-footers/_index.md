---
title: Menghapus header dan footer dari PDF dengan Java
linktitle: Menghapus header dan footer
type: docs
weight: 110
url: /id/java/remove-headers-footers/
description: Hapus artefak header dan footer dari halaman pertama PDF di Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus header dan footer dari PDF dengan Java
Abstract: Hapus artefak header dan footer dari halaman pertama PDF di Java.
---
Hapus artefak header dan footer dari halaman pertama PDF di Java.

## Menghapus artefak header dan footer

Gunakan pendekatan ini ketika artefak header dan footer yang ada harus dihapus dari halaman.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Telusuri koleksi artefak halaman dalam urutan terbalik.
1. Hapus artefak paginasi yang subtipenya adalah header atau footer.
1. Simpan dokumen.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Topik terkait

- [Menambahkan header dan footer](/pdf/id/java/artifacts-header-footer/)
- [Artefak PDF](/pdf/id/java/artifacts/)
