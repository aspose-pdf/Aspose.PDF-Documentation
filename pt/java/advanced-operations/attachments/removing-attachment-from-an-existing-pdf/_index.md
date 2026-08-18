---
title: Remover anexos de PDF em Java
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Aprenda como remover um ou todos os anexos incorporados de documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exclua anexos de PDF programaticamente com Java
Abstract: Este artigo mostra como remover anexos de arquivos PDF usando Aspose.PDF para Java. Os exemplos demonstram a exclusão de um arquivo incorporado por chave e a limpeza de toda a coleção EmbeddedFiles antes de salvar o documento atualizado.
---
Os anexos armazenados em um documento PDF podem ser removidos individualmente ou todos de uma vez por meio da coleção `EmbeddedFiles`.

## Remover um único anexo

Use este exemplo quando um arquivo incorporado nomeado precisar ser excluído do PDF.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua o anexo pela chave da coleção de arquivos incorporados.
1. Salve o documento de saída atualizado.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Remover todos os anexos

Use esta abordagem quando toda a coleção de arquivos incorporados precisar ser limpa.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua todos os itens da coleção de arquivos incorporados.
1. Salve o documento de saída limpo.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
