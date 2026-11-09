---
title: Menghapus latar belakang dari PDF dengan Java
linktitle: Menghapus latar belakang
type: docs
weight: 80
url: /id/java/remove-backgrounds/
description: Hapus artefak latar belakang dari halaman pertama PDF di Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus latar belakang dari PDF dengan Java
Abstract: Hapus artefak latar belakang dari halaman pertama PDF di Java.
---
Hapus artefak latar belakang dari halaman pertama PDF di Java.

## Menghapus artefak latar belakang

Gunakan pendekatan ini ketika artefak latar belakang yang ada harus dihapus dari halaman.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Telusuri koleksi artefak halaman dalam urutan terbalik.
1. Hapus artefak yang tipenya pagination dan subtipenya background.
1. Simpan dokumen.

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

## Topik terkait

- [Menambahkan latar belakang](/pdf/id/java/add-backgrounds/)
- [Artefak PDF](/pdf/id/java/artifacts/)
