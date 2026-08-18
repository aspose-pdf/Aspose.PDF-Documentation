---
title: Adicionar numeração Bates ao PDF em Java
linktitle: Adicionando numeração de Bates
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Aprenda como adicionar e remover numeração de Bates em documentos PDF usando Java com Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar numeração Bates via Java
Abstract: Este artigo explica como criar e remover artefatos de numeração Bates em documentos PDF usando Aspose.PDF para Java. Ele cobre a configuração de `BatesNArtifact`, sua aplicação por meio de auxiliares de numeração de Bates ou auxiliares de paginação genéricos e a remoção da numeração de Bates de um documento.
---
Os artefatos de numeração Bates são úteis em fluxos de trabalho jurídicos, de arquivamento e de controle de documentos, onde cada página precisa de um identificador persistente em nível de página.

## Adicione numeração Bates com o ajudante dedicado

Use este exemplo quando desejar aplicar a numeração Bates por meio do auxiliar de coleção de páginas dedicado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione quaisquer páginas extras exigidas pela amostra.
1. Crie a configuração [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Aplique a numeração de Bates à coleção de páginas e salve o arquivo de saída.

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

## Adicionar numeração de Bates por meio de artefatos de paginação

Este exemplo aplica a numeração Bates passando o artefato Bates por meio da API de paginação genérica.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione as páginas necessárias.
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

## Excluir numeração de Bates

Use esta abordagem quando artefatos de numeração Bates existentes precisarem ser removidos do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame o auxiliar de coleção de páginas que exclui a numeração de Bates.
1. Salve o arquivo de saída limpo.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
