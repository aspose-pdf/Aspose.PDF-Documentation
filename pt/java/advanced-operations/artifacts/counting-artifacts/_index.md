---
title: Contar artefatos PDF em Java
linktitle: Contando Artefatos
type: docs
weight: 40
url: /pt/java/counting-artifacts/
description: Saiba como inspecionar e contar artefatos de paginação em documentos PDF usando Java com Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando Artefatos em PDF usando Java
Abstract: Este artigo explica como inspecionar e contar artefatos de paginação em documentos PDF usando Aspose.PDF for Java. Ele mostra como iterar pelos artefatos de página e contar os subtipos de marca d'água, plano de fundo, cabeçalho e rodapé.
---
## Contar artefatos de paginação em uma página

Use este exemplo quando precisar de uma contagem rápida dos principais subtipos de artefato de paginação em uma página.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia a coleção de artefatos [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) da página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Percorra a coleção de artefatos [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) da página e conte os artefatos de cada subtipo de paginação que precisa relatar.

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

## Tópicos relacionados

- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
- [Extrair detalhes da marca d'água](/pdf/pt/java/extract-watermarks/)
- [Remover fundos](/pdf/pt/java/remove-backgrounds/)
- [Remover marcas d'água](/pdf/pt/java/remove-watermarks/)
- [Remover numeração Bates](/pdf/pt/java/remove-bates-numbering/)
- [Remover Cabeçalhos e Rodapés](/pdf/pt/java/remove-headers-footers/)
