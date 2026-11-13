---
title: Remover numeração Bates em Java
linktitle: Remover numeração Bates
type: docs
weight: 100
url: /pt/java/remove-bates-numbering/
description: Remover numeração Bates de todas as páginas de um PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover numeração Bates em Java
Abstract: Remover numeração Bates de todas as páginas de um PDF em Java.
---
Remover numeração Bates de todas as páginas de um PDF em Java.

## Excluir numeração Bates

Use esta abordagem quando os artefatos de numeração Bates existentes devem ser removidos do documento.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame o ajudante de coleção de páginas que exclui a numeração Bates.
1. Salve o arquivo de saída limpo.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados

- [Adicionar numeração de Bates](/pdf/pt/java/add-bates-numbering/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
