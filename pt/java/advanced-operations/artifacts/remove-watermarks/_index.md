---
title: Remover marcas d'água PDF em Java
linktitle: Remover marcas d'água
type: docs
weight: 90
url: /pt/java/remove-watermarks/
description: Remover artefatos de marca d'água da primeira página de um PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover marcas d'água em Java
Abstract: Remover artefatos de marca d'água da primeira página de um PDF em Java.
---
Remover artefatos de marca d'água da primeira página de um PDF em Java.

## Excluir artefatos de marca d'água

O exemplo remove da primeira página apenas os artefatos do tipo `Pagination` e do subtipo `Watermark`. As marcas d’água visíveis armazenadas como texto comum da página, imagens ou anotações permanecem no PDF.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Percorra a coleção de artefatos da página em ordem inversa.
1. Exclua os artefatos de paginação cujo subtipo é marca d'água, então salve o documento.

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

## Tópicos relacionados

- [Adicionar marcas d'água](/pdf/pt/java/add-watermarks/)
- [Extrair detalhes da marca d'água](/pdf/pt/java/extract-watermarks/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
