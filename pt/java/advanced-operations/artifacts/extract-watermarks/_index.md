---
title: Extrair detalhes da marca d'água PDF em Java
linktitle: Extrair detalhes da marca d'água
type: docs
weight: 50
url: /pt/java/extract-watermarks/
description: Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair detalhes da marca d'água em Java
Abstract: Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Java.
---
Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Java.

## Extrair artefatos de marca d'água de um PDF

Use este exemplo quando precisar inspecionar artefatos de marca d'água existentes e ler seu texto ou posição.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Percorra a coleção de artefatos da página de destino.
1. Filtre os artefatos de paginação de marca d'água e imprima seu texto e retângulos.

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

## Tópicos relacionados

- [Adicionar marcas d'água](/pdf/pt/java/add-watermarks/)
- [Remover marcas d'água](/pdf/pt/java/remove-watermarks/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
