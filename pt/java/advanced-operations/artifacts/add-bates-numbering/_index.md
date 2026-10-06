---
title: Adicionar numeração Bates ao PDF em Java
linktitle: Adicionar numeração Bates
type: docs
weight: 10
url: /pt/java/add-bates-numbering/
description: Aprenda como adicionar e remover numeração Bates em documentos PDF usando Java com Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar numeração Bates via Java
Abstract: Este artigo explica como criar e remover artefatos de numeração Bates em documentos PDF usando Aspose.PDF for Java. Ele aborda a configuração de um `BatesNArtifact`, a aplicação através de auxiliares de numeração Bates ou auxiliares genéricos de paginação, e a remoção da numeração Bates de um documento.
---
Os artefatos de numeração Bates são úteis em fluxos de trabalho jurídicos, arquivísticos e de controle de documentos, onde cada página necessita de um identificador persistente ao nível da página.

## Adicionar numeração Bates com o auxiliar dedicado

Use este exemplo quando quiser aplicar a numeração Bates através do auxiliar dedicado de coleção de páginas.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione quaisquer páginas extras exigidas pela amostra.
1. Crie o [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) configuração.
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

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione as páginas necessárias.
1. Crie o [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) e adicione-o à lista de artefatos de paginação.
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

## Excluir numeração Bates

Use esta abordagem quando artefatos existentes de numeração Bates devem ser removidos do documento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame o helper de coleção de páginas que exclui a numeração Bates.
1. Salve o arquivo de saída limpo.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
