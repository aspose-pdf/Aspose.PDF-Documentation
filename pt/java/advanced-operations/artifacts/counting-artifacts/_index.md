---
title: Contar artefatos PDF em Java
linktitle: Contando artefatos
type: docs
weight: 40
url: /pt/java/counting-artifacts/
description: Aprenda como inspecionar e contar artefatos de paginação em documentos PDF usando Java com Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando artefatos em PDF usando Java
Abstract: Este artigo explica como inspecionar e contar artefatos de paginação em documentos PDF usando Aspose.PDF for Java. Ele mostra como iterar pelos artefatos de página e contar subtipos de marca d'água, plano de fundo, cabeçalho e rodapé.
---
## Contar artefatos de paginação em uma página

Use este exemplo quando precisar de uma contagem rápida dos principais subtipos de artefato de paginação em uma página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia o [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) coleção do destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Itere pela página [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) coleção e conte cada subtipo de paginação que você precisa relatar.

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
