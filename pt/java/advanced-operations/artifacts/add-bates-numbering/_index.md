---
title: Adicionar numeração Bates ao PDF em Java
linktitle: Adicionar numeração Bates
type: docs
weight: 10
url: /pt/java/add-bates-numbering/
description: Adicionar identificadores sequenciais Bates às páginas de PDF em Java com o auxiliar dedicado de numeração Bates ou a API genérica de paginação.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar numeração Bates em Java
Abstract: Adicionar identificadores sequenciais Bates às páginas de PDF em Java com o auxiliar dedicado de numeração Bates ou a API genérica de paginação.
---
Os artefatos de numeração Bates são úteis em fluxos de trabalho jurídicos, arquivísticos e de controle de documentos, onde cada página precisa de um identificador persistente ao nível da página.

## Adicionar numeração Bates com o auxiliar dedicado

Use este exemplo quando quiser aplicar a numeração Bates por meio do assistente dedicado de coleção de páginas.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione quaisquer páginas extras exigidas pelo exemplo.
1. Configure um objeto [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Aplique a numeração Bates à coleção de páginas e salve o arquivo de saída.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Adicionar numeração Bates através de artefatos de paginação

Este exemplo aplica numeração Bates passando o artefato Bates através da API genérica de paginação.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione as páginas necessárias.
1. Crie o [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) e adicione-o a uma lista de artefatos de paginação.
1. Aplique os artefatos de paginação à coleção de páginas e salve o documento.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados

- [Remover numeração Bates](/pdf/pt/java/remove-bates-numbering/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
