---
title: Mesclar arquivos PDF em Java
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /java/merge-pdf/
description: Aprenda como mesclar vários arquivos PDF em um único documento em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine páginas PDF usando Java
Abstract: Este artigo explica como mesclar dois documentos PDF em Java usando Aspose.PDF. O exemplo abre dois documentos de origem, anexa as páginas do segundo documento ao primeiro e salva o resultado mesclado como um novo arquivo PDF.
---
A mesclagem de arquivos PDF é útil quando você precisa combinar documentos relacionados em um único arquivo para distribuição, arquivamento ou processamento.

## Exemplo ao vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é um aplicativo online gratuito para testar a fusão de PDF em um navegador.

Este tópico mostra como mesclar vários arquivos PDF em um único documento em Java:

1. Abra ambos os documentos de origem com o construtor [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Anexe a coleção [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do segundo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ao primeiro com `document1.getPages().add(document2.getPages())`.
1. Salve o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) mesclado no caminho de saída.

## Mesclar dois documentos PDF

O exemplo Java a seguir é baseado em `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
