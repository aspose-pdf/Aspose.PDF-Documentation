---
title: Remover Cabeçalhos e Rodapés de PDF em Java
linktitle: Remover Cabeçalhos e Rodapés
type: docs
weight: 110
url: /pt/java/remove-headers-footers/
description: Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Cabeçalhos e Rodapés em Java
Abstract: Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Java.
---
Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Java.

## Excluir artefatos de cabeçalho e rodapé

Use esta abordagem quando artefatos de cabeçalho e rodapé existentes devem ser removidos da página.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Percorra a coleção de artefatos de página em ordem reversa.
1. Exclua artefatos de paginação cujo subtipo é cabeçalho ou rodapé, e salve o documento.

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

## Tópicos relacionados

- [Adicionar Cabeçalhos e Rodapés](/pdf/pt/java/artifacts-header-footer/)
- [Trabalhar com Artefatos PDF em Java](/pdf/pt/java/artifacts/)
