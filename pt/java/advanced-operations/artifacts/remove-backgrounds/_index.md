---
title: Remover fundos de PDF em Java
linktitle: Remover fundos
type: docs
weight: 80
url: /pt/java/remove-backgrounds/
description: Remover artefatos de fundo da primeira página de um PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover fundos em Java
Abstract: Remover artefatos de fundo da primeira página de um PDF em Java.
---
Remover artefatos de fundo da primeira página de um PDF em Java.

## Remover artefatos de fundo

Use esta abordagem quando os artefatos de fundo existentes devem ser excluídos da página.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Percorra a coleção de artefatos de página em ordem reversa.
1. Exclua artefatos cujo tipo seja paginação e subtipo seja plano de fundo, então salve o documento.

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

## Tópicos relacionados

- [Adicionar planos de fundo](/pdf/pt/java/add-backgrounds/)
- [Trabalhar com Artefatos PDF em Java](/pdf/pt/java/artifacts/)
